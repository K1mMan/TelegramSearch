from PyQt6.QtWidgets import QPushButton


class CButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.bool = True
        self.setStyleSheet('background: rgb(42, 117, 65); color: white;')

    def click(self):
        self.bool = not self.bool
        if self.bool:
            self.setStyleSheet('background: rgb(42, 117, 65); color: white;')
        else:
            self.setStyleSheet("background: rgb(33, 33, 33); color: white;")

    def mousePressEvent(self, mouseEvent):
        super().mousePressEvent(mouseEvent)
        self.click()
