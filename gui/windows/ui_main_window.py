# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowUBXrXX.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(703, 495)
        MainWindow.setStyleSheet(u"")
        self.action_Select_Files = QAction(MainWindow)
        self.action_Select_Files.setObjectName(u"action_Select_Files")
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setObjectName(u"main_layout")
        self.main_tab_widget = QTabWidget(self.centralwidget)
        self.main_tab_widget.setObjectName(u"main_tab_widget")
        self.home_tab = QWidget()
        self.home_tab.setObjectName(u"home_tab")
        self.verticalLayout = QVBoxLayout(self.home_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.home_tab)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.methods_list = QComboBox(self.frame)
        self.methods_list.addItem("")
        self.methods_list.addItem("")
        self.methods_list.setObjectName(u"methods_list")

        self.gridLayout.addWidget(self.methods_list, 0, 1, 1, 1)

        self.word_entry = QLineEdit(self.frame)
        self.word_entry.setObjectName(u"word_entry")
        self.word_entry.setReadOnly(False)

        self.gridLayout.addWidget(self.word_entry, 0, 2, 1, 2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)

        self.letter_num = QSpinBox(self.frame)
        self.letter_num.setObjectName(u"letter_num")

        self.gridLayout.addWidget(self.letter_num, 0, 5, 1, 1)

        self.add_num = QPushButton(self.frame)
        self.add_num.setObjectName(u"add_num")

        self.gridLayout.addWidget(self.add_num, 0, 6, 1, 2)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 9)

        self.remove_file_name = QPushButton(self.frame)
        self.remove_file_name.setObjectName(u"remove_file_name")

        self.gridLayout.addWidget(self.remove_file_name, 2, 0, 1, 2)

        self.empty_table_data_btn = QPushButton(self.frame)
        self.empty_table_data_btn.setObjectName(u"empty_table_data_btn")

        self.gridLayout.addWidget(self.empty_table_data_btn, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.restore_names_btn = QPushButton(self.frame)
        self.restore_names_btn.setObjectName(u"restore_names_btn")

        self.gridLayout.addWidget(self.restore_names_btn, 2, 4, 1, 2)

        self.apply_btn = QPushButton(self.frame)
        self.apply_btn.setObjectName(u"apply_btn")

        self.gridLayout.addWidget(self.apply_btn, 2, 8, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.files_table = QTableWidget(self.home_tab)
        if (self.files_table.columnCount() < 3):
            self.files_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.files_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.files_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.files_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.files_table.setObjectName(u"files_table")
        self.files_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.files_table)

        self.frame_2 = QFrame(self.home_tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.start_rename_btn = QPushButton(self.frame_2)
        self.start_rename_btn.setObjectName(u"start_rename_btn")
        self.start_rename_btn.setMinimumSize(QSize(150, 0))
        self.start_rename_btn.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.start_rename_btn.setFont(font)
        self.start_rename_btn.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.start_rename_btn, 0, Qt.AlignHCenter)

        self.current_file_label = QLabel(self.frame_2)
        self.current_file_label.setObjectName(u"current_file_label")

        self.verticalLayout_3.addWidget(self.current_file_label)

        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_3.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.frame_2)

        self.main_tab_widget.addTab(self.home_tab, "")
        self.settings_tab = QWidget()
        self.settings_tab.setObjectName(u"settings_tab")
        self.verticalLayout_2 = QVBoxLayout(self.settings_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.settings_tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.rename_radio_btn = QRadioButton(self.groupBox)
        self.rename_radio_btn.setObjectName(u"rename_radio_btn")
        self.rename_radio_btn.setChecked(True)

        self.verticalLayout_4.addWidget(self.rename_radio_btn)

        self.copy_radio_btn = QRadioButton(self.groupBox)
        self.copy_radio_btn.setObjectName(u"copy_radio_btn")

        self.verticalLayout_4.addWidget(self.copy_radio_btn)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMaximumSize(QSize(300, 16777215))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.save_location_entry = QLineEdit(self.groupBox)
        self.save_location_entry.setObjectName(u"save_location_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.save_location_entry.sizePolicy().hasHeightForWidth())
        self.save_location_entry.setSizePolicy(sizePolicy1)
        self.save_location_entry.setMinimumSize(QSize(280, 0))
        self.save_location_entry.setMaximumSize(QSize(280, 16777215))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.save_location_entry)

        self.save_location_btn = QToolButton(self.groupBox)
        self.save_location_btn.setObjectName(u"save_location_btn")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.save_location_btn)


        self.verticalLayout_4.addLayout(self.formLayout)


        self.verticalLayout_2.addWidget(self.groupBox, 0, Qt.AlignTop)

        self.main_tab_widget.addTab(self.settings_tab, "")

        self.main_layout.addWidget(self.main_tab_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 703, 22))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_File.addAction(self.action_Select_Files)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_Help.addAction(self.action_About)

        self.retranslateUi(MainWindow)

        self.main_tab_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Py Renamer", None))
        self.action_Select_Files.setText(QCoreApplication.translate("MainWindow", u"&Select Files", None))
#if QT_CONFIG(shortcut)
        self.action_Select_Files.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"&Exit", None))
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"&About", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Method", None))
        self.methods_list.setItemText(0, QCoreApplication.translate("MainWindow", u"Add", None))
        self.methods_list.setItemText(1, QCoreApplication.translate("MainWindow", u"Remove", None))

        self.word_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Word", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Letter:", None))
        self.add_num.setText(QCoreApplication.translate("MainWindow", u"Add Num", None))
        self.remove_file_name.setText(QCoreApplication.translate("MainWindow", u"Remove Files Name", None))
        self.remove_file_name.setProperty("colorBtn", QCoreApplication.translate("MainWindow", u"danger", None))
        self.empty_table_data_btn.setText(QCoreApplication.translate("MainWindow", u"Empty Table", None))
        self.empty_table_data_btn.setProperty("colorBtn", QCoreApplication.translate("MainWindow", u"danger", None))
        self.restore_names_btn.setText(QCoreApplication.translate("MainWindow", u"Restore Names", None))
        self.apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        ___qtablewidgetitem = self.files_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"File Name", None));
        ___qtablewidgetitem1 = self.files_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New File Name", None));
        ___qtablewidgetitem2 = self.files_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Path", None));
        self.start_rename_btn.setText(QCoreApplication.translate("MainWindow", u"Start Rename", None))
        self.start_rename_btn.setProperty("startRename", "")
        self.current_file_label.setText("")
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.home_tab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.rename_radio_btn.setText(QCoreApplication.translate("MainWindow", u"Rename File in Existing Folder", None))
        self.copy_radio_btn.setText(QCoreApplication.translate("MainWindow", u"Copy Files To New Folder", None))
        self.save_location_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Past path here or choose from button", None))
        self.save_location_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.settings_tab), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
    # retranslateUi

