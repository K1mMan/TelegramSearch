import PyQt6
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QMainWindow, QLabel
from custom.CButton import CButton
from configparser import ConfigParser
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, WEIGHT, HEIGHT):
        super().__init__()
        self.WALLPAPER_GLASS = None
        self.WALLPAPER = None
        self.LABEL_ACTIVE_THREAD = None
        self.LABEL_SCORE_FIND = None
        self.TABLE_IP_MODEL = None
        self.TABLE_FIND_POSTS = None
        self.BUTTON_IMG = None
        self.BUTTON_VIDEO = None
        self.BUTTON_DATE = None
        self.EDITTEXT_SEARCH = None
        self.BUTTON_SCAN = None
        self.BUTTON_EMAIL = None
        self.LAYOUT_ROOT = None
        self.WEIGHT = WEIGHT
        self.HEIGHT = HEIGHT

        self.CONFIG = ConfigParser()
        self.CONFIG.read('config.ini')

    def setupUi(self, Main) -> None:
        Main.setObjectName("MainWindow")
        Main.resize(self.WEIGHT, self.HEIGHT)
        Main.setAutoFillBackground(False)
        Main.setWindowOpacity(0.98)
        Main.setStyleSheet('background: rgba(0, 0, 0, 0);')

        self.LAYOUT_ROOT = QtWidgets.QWidget(Main)
        self.LAYOUT_ROOT.resize(self.WEIGHT, self.HEIGHT)
        self.LAYOUT_ROOT.setStyleSheet("background: rgba(0, 0, 0, 0);")

        self.WALLPAPER = QLabel(self.LAYOUT_ROOT)
        self.WALLPAPER.setGeometry(QtCore.QRect(0, 0, self.WEIGHT - 200, self.HEIGHT))
        self.WALLPAPER.setPixmap(QPixmap(self.CONFIG.get('wallpaper', 'path')))
        self.WALLPAPER.setScaledContents(True)

        self.WALLPAPER_GLASS = QtWidgets.QWidget(self.LAYOUT_ROOT)
        self.WALLPAPER_GLASS.setGeometry(0, 0, self.WEIGHT, self.HEIGHT)
        self.WALLPAPER_GLASS.setStyleSheet(f"background: rgba{self.CONFIG.get('wallpaper', 'color')}")

        self.EDITTEXT_SEARCH = QtWidgets.QLineEdit(self.LAYOUT_ROOT)
        self.EDITTEXT_SEARCH.setStyleSheet("border: 2px solid green; border-radius: 10px; color: white")
        self.EDITTEXT_SEARCH.setGeometry(40, 40, 250, 30)

        self.BUTTON_SCAN = QtWidgets.QPushButton(self.LAYOUT_ROOT)
        self.BUTTON_SCAN.setIcon(QIcon("res/icon/search.png"))
        self.BUTTON_SCAN.setIconSize(QtCore.QSize(30, 30))
        self.BUTTON_SCAN.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BUTTON_SCAN.setGeometry(300, 40, 30, 30)

        self.BUTTON_EMAIL = CButton(self.LAYOUT_ROOT)
        self.BUTTON_EMAIL.setText("Email")
        self.BUTTON_EMAIL.setGeometry(400, 40, 150, 30)

        self.BUTTON_DATE = CButton(self.LAYOUT_ROOT)
        self.BUTTON_DATE.setText("Date")
        self.BUTTON_DATE.setGeometry(550, 40, 150, 30)

        self.BUTTON_IMG = CButton(self.LAYOUT_ROOT)
        self.BUTTON_IMG.setText("Image")
        self.BUTTON_IMG.setGeometry(700, 40, 150, 30)

        self.BUTTON_VIDEO = CButton(self.LAYOUT_ROOT)
        self.BUTTON_VIDEO.setText("Video")
        self.BUTTON_VIDEO.setGeometry(850, 40, 150, 30)

        self.LABEL_SCORE_FIND = QtWidgets.QLabel(self.LAYOUT_ROOT)
        self.LABEL_SCORE_FIND.setGeometry(40, 615, 150, 30)
        self.LABEL_SCORE_FIND.setStyleSheet("color: white")
        self.LABEL_SCORE_FIND.setText("Find Posts: 0")

        self.LABEL_ACTIVE_THREAD = QtWidgets.QLabel(self.LAYOUT_ROOT)
        self.LABEL_ACTIVE_THREAD.setGeometry(190, 615, 150, 30)
        self.LABEL_ACTIVE_THREAD.setStyleSheet("color: white")
        self.LABEL_ACTIVE_THREAD.setText("Active Threads: 0")

        self.TABLE_FIND_POSTS = QtWidgets.QTableView(self.LAYOUT_ROOT)
        self.TABLE_FIND_POSTS.setGeometry(40, 110, 1002, 500)
        self.TABLE_FIND_POSTS.setShowGrid(False)
        self.TABLE_FIND_POSTS.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.TABLE_FIND_POSTS.setSortingEnabled(True)
        self.TABLE_FIND_POSTS.verticalHeader().setVisible(False)
        self.TABLE_FIND_POSTS.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.TABLE_FIND_POSTS.setStyleSheet(open("style/table/TABLE_POST.css").read())
        self.TABLE_FIND_POSTS.horizontalHeader().setStyleSheet(open("style/table/TABLE_POST_HEAD.css").read())
        self.TABLE_FIND_POSTS.verticalScrollBar().setStyleSheet(open("style/table/TABLE_POST_SLIDER.css").read())
        self.TABLE_FIND_POSTS.verticalHeader().setVisible(False)
        self.TABLE_FIND_POSTS.setShowGrid(False)
        self.TABLE_FIND_POSTS.setAlternatingRowColors(True)
        self.TABLE_IP_MODEL = PyQt6.QtGui.QStandardItemModel()
        self.TABLE_FIND_POSTS.setModel(self.TABLE_IP_MODEL)
        self.translateUi(Main)

    def translateUi(self, Main) -> None:
        self.TABLE_IP_MODEL.setHorizontalHeaderLabels(['URL', 'EMAIL', 'DATE', 'IMAGE', 'VIDEO'])
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("C.C.", "Telegram Search"))
        Main.setFixedSize(1100, 650)


    def setSettingTable(self, LABELS) -> None:
        self.TABLE_IP_MODEL.clear()
        self.TABLE_IP_MODEL.setHorizontalHeaderLabels(LABELS)
        self.TABLE_FIND_POSTS.setModel(self.TABLE_IP_MODEL)
