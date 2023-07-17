import threading
from PyQt6 import QtCore
import re
import requests
from bs4 import BeautifulSoup
from threading import Thread


def get_emil(response) -> list:
    soup = BeautifulSoup(response.text, 'lxml')
    body = soup.find('article', class_='tl_article_content')
    email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+[\w:-]+',str(body))
    email = [item for item in email if item != "dmca@telegram.org"]
    return email


def get_video(response) -> int:
    video = response.text.count("<video")
    return video


def get_date(response) -> str:
    soup = BeautifulSoup(response.text, 'lxml')
    date = soup.find('time').contents
    date = str(date[0])
    date = date.split(", ")
    return f"{date[1]} {date[0]}"

def get_img(response) -> int:
    img = response.text.count("<img")
    return img


class scan(QtCore.QThread):
    end_th = QtCore.pyqtSignal(int)
    find = QtCore.pyqtSignal(list)
    def __init__(self, search, *args, parent=None):
        super().__init__(parent)
        self.search = search
        self.all_plugins = [get_emil, get_date, get_img, get_video]
        self.plugins = [self.all_plugins[index] for index, permission in enumerate(args) if permission]

    def isCorrectUrl(self, url) -> int:
        # noinspection PyBroadException
        try:
            response = requests.get(url, timeout=100)
            if response.status_code == 200:
                answers = [func(response) for func in self.plugins]
                answers.insert(0, url)
                self.find.emit(answers)
                self.end_th.emit(threading.active_count())
                return 200
            else:
                self.end_th.emit(threading.active_count())
                return 404
        except Exception:
            self.isCorrectUrl(url)


    def startSearch(self, date) -> None:
        url = f"https://telegra.ph/{self.search}-{'{:02}'.format(date[0])}-{'{:02}'.format(date[1])}"
        if self.isCorrectUrl(url) == 200:
            for page, _ in enumerate(iter(bool, True), start=2):
                if self.isCorrectUrl(f"{url}-{page}") == 404:
                    break


    def run(self) -> None:
        for month in range(1, 13):
            for day in range(1, 32):
                Thread(target=self.startSearch, args={(month, day)}).start()
