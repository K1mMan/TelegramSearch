import PyQt6
import sys
from ui import MainWindow
from utils.scan import scan
from PyQt6 import QtWidgets, QtGui

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = MainWindow(1300, 650)
        self.ui.setupUi(self)
        self.score_posts = 0

        self.activeItem = None
        self.custom_regex = []
        self.lang_convert = {' ': "-", '-': "-", 'a': "a",
                        'b': "b", 'c': "c", 'd': "d", 'e': 'e',
                        'f': "f", 'g': "g", 'h': "h", 'i': "i",
                        'j': "j", 'k': "k", 'l': "l", 'm': "m",
                        'n': "n", 'o': "o", 'p': "p", 'q': "q",
                        'r': "r", 's': "s", 't': "t", 'u': "u",
                        'v': "v", 'w': "w", 'x': "x", 'y': "y",
                        'z': "z", '0': "0", "1": "1", "2": "2",
                        "3": "3", "4": "4", "5": "5", "6": "6",
                        "7": "7", "8": "8", "9": "9"}
        self.ui.BUTTON_SCAN.clicked.connect(self.startScan)
        self.thread_scan = None

    def startScan(self) -> None:
        self.score_posts = 0
        self.ui.LABEL_SCORE_FIND.setText(f"Find Post: {self.score_posts}")
        search = self.ui.EDITTEXT_SEARCH.text()

        search = search.lower()
        search = [char for char in list(search) if self.lang_convert.get(char) is not None]
        search = "".join(list(map(self.lang_convert.get, list(search))))

        self.setLabels()
        self.thread_scan = scan(search, self.ui.BUTTON_EMAIL.bool,
                                        self.ui.BUTTON_DATE.bool,
                                        self.ui.BUTTON_IMG.bool,
                                        self.ui.BUTTON_VIDEO.bool)
        self.thread_scan.find.connect(self.see_find)
        self.thread_scan.end_th.connect(self.setActiveThread)
        self.thread_scan.start()

    def see_find(self, answer) -> None:
        self.score_posts += 1
        self.ui.LABEL_SCORE_FIND.setText(f"Find Post: {self.score_posts}")
        self.ui.TABLE_IP_MODEL.appendRow([PyQt6.QtGui.QStandardItem(str(item)) for item in answer])

    def setLabels(self) -> None:
        LABELS = ['URL']
        if self.ui.BUTTON_EMAIL.bool: LABELS.append('EMAIL')
        if self.ui.BUTTON_DATE.bool: LABELS.append('DATE')
        if self.ui.BUTTON_IMG.bool: LABELS.append('IMAGE')
        if self.ui.BUTTON_VIDEO.bool: LABELS.append('VIDEO')
        self.ui.setSettingTable(LABELS)

    def setActiveThread(self, thread_score) -> None:
        self.ui.LABEL_ACTIVE_THREAD.setText(f"Active Threads: {thread_score - 3}")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('res/icon/icon.png'))
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec())
