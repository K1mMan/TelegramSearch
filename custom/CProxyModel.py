from PyQt6.QtCore import QSortFilterProxyModel, QModelIndex
from PyQt6 import QtCore


class CProxyModel(QSortFilterProxyModel):
    count = QtCore.pyqtSignal()

    def __init__(self):
        super(CProxyModel, self).__init__()
        self.filters = {}

    def setFilterByColumn(self, editText, column):
        self.filters[column] = editText
        self.invalidateFilter()
        self.count.emit()

    def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex):
        for key, value in self.filters.items():
            item = self.sourceModel().index(source_row, key, source_parent)
            if item.isValid():
                text = self.sourceModel().data(item)
                if not text.__contains__(value):
                    return False
        return True