# IMPORT QT CORE
from qt_core import *

# IMPORT MODULES
import sys

# MAIN WINDOW
# ____________________________________________________________________________ #
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI Changes
        self.ui_changes()

        # SHOW WINDOW
        # ---------------------------------------------------------------------------- #
        self.show()
        # ---------------------------------------------------------------------------- #

    # UI CHANGES
    def ui_changes(self):
        # APP TITLE
        self.setWindowTitle("Py Renamer")

        # RESIZE
        self.resize(950, 550)


# EXCUTE APP
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec())
