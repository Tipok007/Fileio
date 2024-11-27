import json
import os
import requests
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import filedialog as fd

history_file = "upload_history.json"


def save_history(file_path, download_link):
    history = []
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            history = json.load(file)

    history.append({"file_path": os.path.basename(file_path), "download_link": download_link})

    with open(history_file, "w") as file:
        json.dump(history, file, indent=4)



def show_history():
    if not os.path.exists(history_file):
        messagebox.showinfo("История", "История загрузок пуста")
        return



    history_window = Toplevel(app)
    history_window.title("История Загрузок")

    files_listbox = Listbox(history_window, width=50, height=20)
    files_listbox.grid(row=0, column=0, padx=(10, 0), pady=10)

    links_listbox = Listbox(history_window, width=50, height=20)
    links_listbox.grid(row=0, column=1, padx=(0, 10), pady=10)

    with open(history_file, "r") as file:
        history = json.load(file)
        for item in history:
            files_listbox.insert(END, item['file_path'])
            links_listbox.insert(END, item['download_link'])


def upload_file():
    filepath = fd.askopenfilename()
    if filepath:
        try:
            with open(filepath, 'rb') as file:
                files = {'file': file}
                response = requests.post("https://file.io", files=files)

                if response.status_code == 200:
                    link = response.json().get('link')
                    if link:
                        messagebox.showinfo("Успех", f"Файл загружен! Ссылка: {link}")
                        save_history(filepath, link)
                    else:
                        messagebox.showerror("Ошибка", "Не удалось получить ссылку на файл.")
                else:
                    messagebox.showerror("Ошибка", "Ошибка при загрузке файла.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


app = tk.Tk()
app.title("TempFile Share")

upload_button = ttk.Button(app, text="Загрузить файл", command=upload_file)
upload_button.pack(pady=10)

history_button = ttk.Button(app, text="Показать Историю", command=show_history)
history_button.pack(pady=10)

app.mainloop()




