import json
import os

history_file = 'test_save_hisory.json'

def save_history(file_path, download_link):
    history = []
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            history = json.load(file)

    history.append({"file_path": os.path.basename(file_path), "download_link": download_link})

    with open(history_file, "w") as file:
        json.dump(history, file, indent=4)

def test_save_hisory():
    test_file_path = "test_file.txt"
    test_download_link = 'https://file.io/dfgjksdfgjksldfg'

    save_history(test_file_path, test_download_link)

    with open(history_file, 'r') as f:
        history = json.load(f)
        assert len(history) == 1
        assert history[0]['file_path'] == os.path.basename(test_file_path)
        assert history[0]['download_link'] == test_download_link

    os.remove(history_file)  # Удаляем файл после теста

test_save_hisory()



