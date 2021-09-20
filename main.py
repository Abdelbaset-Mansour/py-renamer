# IMPORT QT CORE
import os
from re import S
from qt_core import *

# IMPORT MODULES
import sys
from pathlib import Path
import shutil

# MAIN WINDOW UI FILE
from gui.windows.ui_main_window import Ui_MainWindow

# GLOBALES
files_names = []

new_file_names = files_names

# MAIN WINDOW
# -------------------------------------------------------- #
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # INIT UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # UI Changes
        self.ui_changes()

        # Menu Actions
        # -------------------------------------------------------- #
        self.ui.action_Select_Files.triggered.connect(self.get_files)

        # #######################
        # START RENAME BUTTON   #
        # #######################
        self.ui.start_rename_btn.clicked.connect(self.start_rename)

        # METHODS
        self.update_word_entry(self.ui.methods_list.currentIndex())
        self.ui.methods_list.currentIndexChanged.connect(self.update_word_entry)

        # WORD ENTRY
        self.ui.word_entry.textChanged.connect(self.add_word_to_name)

        # Letter Num to remove
        self.ui.letter_num.textChanged.connect(self.remove_letter_from_name)

        # EMPTY TABLE DATA
        self.ui.empty_table_data_btn.clicked.connect(self.empty_table_data)

        # APPLLY CHANGES
        self.ui.apply_btn.clicked.connect(self.apply_name_changes)

        # ADD AUTO NUMBER to FILES NAMES
        self.ui.add_num.clicked.connect(self.add_number)

        # REMOVE FILES NAMES
        self.ui.remove_file_name.clicked.connect(self.remove_file_name)

        # RESTORE NAMES
        self.ui.restore_names_btn.clicked.connect(self.restore_names)

        # Files table
        # -------------------------------------------------------- #
        self.ui.files_table.horizontalHeader().setStretchLastSection(True)
        self.ui.files_table.setColumnWidth(0, 250)
        self.ui.files_table.setColumnWidth(1, 250)

        # Disable edit in table
        self.ui.files_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # PROGRESS BAR
        # -------------------------------------------------------- #
        # self.ui.progressBar.setValue(80)

        # -------------------------------------------------------- #
        #                       SETTINGS TAB                       #
        # -------------------------------------------------------- #
        # SAVE LOCATION BTN
        self.ui.save_location_btn.clicked.connect(self.change_save_location)

        # SHOW WINDOW
        # -------------------------------------------------------- #
        self.show()
        # -------------------------------------------------------- #

    # UI CHANGES
    def ui_changes(self):
        # APP TITLE
        self.setWindowTitle("Py Renamer")

        # RESIZE
        self.resize(700, 500)

        # LOAD THEME
        # open qss file
        File = QFile("gui/themes/light.qss")
        if not File.open(QFile.ReadOnly | QFile.Text):
            raise "Error"

        qss = QTextStream(File)
        self.setStyleSheet(qss.readAll())

        # TAB WIDGET
        # -------------------------------------------------------- #
        ## Home TAB
        # Set home tab to default tab
        self.ui.main_tab_widget.setCurrentWidget(self.ui.home_tab)

    # UPDATE METHODS LIST
    def update_word_entry(self, index):
        # Add Method
        if index == 0:
            self.ui.word_entry.setReadOnly(False)
            self.ui.letter_num.setDisabled(True)

        # Remove method
        elif index == 1:
            self.ui.word_entry.setReadOnly(True)
            self.ui.letter_num.setDisabled(False)

    # -------------------------------------------------------- #
    # Handle Menu Actions
    # -------------------------------------------------------- #
    def get_files(self):
        global files_names
        files = QFileDialog.getOpenFileNames(parent=self)
        if files:
            for file in files[0]:
                files_names.append(
                    {
                        "path": Path(file).parent,
                        "name": Path(file).name,
                        "new_name": Path(file).name,
                        "new_path": self.ui.save_location_entry.text(),
                        "edited_name": Path(file).name,
                    }
                )

            # LOAD DATA
            self.load_data()

    # LOAD DATA INTO TABLE
    # -------------------------------------------------------- #
    def load_data(self):

        # CHECK IF FILES NAMES LIST IS EMPTY
        if files_names:
            for row, file in enumerate(files_names):
                # SET ROW COUNT
                self.ui.files_table.setRowCount(len(files_names))

                # INSERT ITEM TO WIDGET
                ## Name Column
                self.ui.files_table.setItem(row, 0, QTableWidgetItem(file["name"]))

                # New Name Column
                self.ui.files_table.setItem(row, 1, QTableWidgetItem(file["new_name"]))

                # PATH COLUMN
                self.ui.files_table.setItem(row, 2, QTableWidgetItem(file["new_path"]))

        # LIST Is EMPTY
        else:
            # CLEAR ALL FILES FROM TABLE
            self.ui.files_table.setRowCount(0)

    # ADD WORD TO NAME
    # -------------------------------------------------------- #
    def add_word_to_name(self):
        # GET WORD FROM WORD ENTRY FEILD
        word = self.ui.word_entry.text()

        # APPLY TO ALL FILES NAME
        for item in files_names:
            old_name = item["edited_name"]
            item["new_name"] = f"{word}{old_name}"
        self.load_data()

    # REMOVE LETTER FROM NAME
    # -------------------------------------------------------- #
    def remove_letter_from_name(self):
        end_pos = self.ui.letter_num.text()

        for item in files_names:
            item["new_name"] = item["edited_name"][int(end_pos) :]

        # LOAD DATA
        self.load_data()

    # EMPTY TABLE DATA
    # -------------------------------------------------------- #
    def empty_table_data(self):
        global files_names
        files_names.clear()
        self.load_data()

    # APPLY CHANGES TO NAME
    # -------------------------------------------------------- #
    def apply_name_changes(self):
        for item in files_names:
            item["edited_name"] = item["new_name"]

    # ADD NUMBER TO ALL FILES NAMES
    # -------------------------------------------------------- #
    def add_number(self):
        for count, item in enumerate(files_names, start=1):
            item["new_name"] = f"{f'{ count }'.zfill(3)}{item['edited_name']}"

        # LAOD DATA
        self.load_data()

    # REMOVE FILES NAMES
    # -------------------------------------------------------- #
    def remove_file_name(self):
        for item in files_names:
            item["new_name"] = Path(item["edited_name"]).suffix

        self.load_data()

    # RESTORE NAMES
    def restore_names(self):
        for item in files_names:
            item["new_name"] = item["name"]

        self.load_data()

    # START RENAME BUTTON
    # -------------------------------------------------------- #
    def start_rename(self):

        self.thread = RenamerWorker(
            files_names, self.ui.rename_radio_btn, self.ui.copy_radio_btn
        )
        self.thread.start()
        self.thread.progress_value.connect(
            lambda val: self.ui.progressBar.setValue(val)
        )
        # Current File
        self.thread.current_file.connect(
            lambda current: self.ui.current_file_label.setText(current)
        )

        # DISABLE "START RENAME BTN"
        self.ui.start_rename_btn.setDisabled(True)

        # RESET PROGRESS BAR
        self.thread.finished.connect(self.finish_rename)

    # FINISH RENAME
    def finish_rename(self):
        QMessageBox.information(self, "Done", "All Files was renamed.", QMessageBox.Ok)
        self.ui.progressBar.setValue(0)
        self.ui.current_file_label.clear()

        # ENABLE "START RENAME BTN"
        self.ui.start_rename_btn.setDisabled(False)
        global files_names
        files_names.clear()
        self.load_data()

    # -------------------------------------------------------- #
    #                       SETTINGS TAB                       #
    # -------------------------------------------------------- #
    # CHNAGE SAVE LOCATION
    def change_save_location(self):
        location = QFileDialog.getExistingDirectory(self)

        # Change path for all files
        if location:
            for file in files_names:
                file["new_path"] = location

            # SET SAVE ENTRY
            self.ui.save_location_entry.setText(location)
            # LOAD DATA
            self.load_data()


# Renamer Worker Thread
# -------------------------------------------------------- #
class RenamerWorker(QThread):
    progress_value = Signal(int)
    current_file = Signal(str)

    def __init__(self, files_names, rename_radio_btn, copy_radio_btn):
        super().__init__()
        self.files_names = files_names
        self.rename_radio_btn = rename_radio_btn
        self.copy_radio_btn = copy_radio_btn

    def run(self):
        if self.files_names:
            for count, file in enumerate(self.files_names, start=1):
                # Current file
                self.current_file.emit(f"Current File: {file['edited_name']}")

                # RENAME FILE :: TODO
                src = Path(file["path"]).joinpath(file["name"])
                dest = (
                    Path(file["new_path"]).joinpath(file["edited_name"])
                    if file["new_path"]
                    else Path(file["path"]).joinpath(file["edited_name"])
                )

                # CHECK FOR COPY OR RENAME
                if self.rename_radio_btn.isChecked():
                    os.rename(src, dest)

                elif self.copy_radio_btn.isChecked() == True and file["new_path"] != "":
                    shutil.copy2(src, dest)

                precent = (count / len(self.files_names)) * 100
                self.progress_value.emit(precent)

        else:
            print(f"LIST IS EMPTY: {files_names}")


# EXCUTE APP
# -------------------------------------------------------- #
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec())
