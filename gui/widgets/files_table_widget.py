from qt_core import *

# FILE TABLE WIDGET
# ================================================================== #
class FilesTableWidget(QTableWidget):
    files = []

    def __init__(self, parent=None):
        super().__init__(parent)

        # ENABLE DRAG & DROP
        self.setAcceptDrops(True)

    # def set_files(self, value):
    #     self.files = value

    # def dragEnterEvent(self, event):
    #     if event.mimeData().hasUrls:
    #         event.accept()
    #     else:
    #         event.ignore()

    # def dragMoveEvent(self, event):
    #     if event.mimeData().hasUrls():
    #         event.setDropAction(Qt.CopyAction)
    #         event.accept()
    #     else:
    #         event.ignore()

    # def dropEvent(self, event):
    #     if event.mimeData().hasUrls():
    #         event.setDropAction(Qt.CopyAction)
    #         event.accept()

    #         for url in event.mimeData().urls():
    #             if url.isLocalFile():
    #                 print(str(url.toLocalFile()))
    #                 self.files.append(str(url.toLocalFile()))
    #             else:
    #                 self.files.append(str(url.toString()))
