# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowuNIudX.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from gui.widgets.menu_btn import MenuBtn
from gui.widgets.files_table_widget import FilesTableWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(901, 632)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_menu.sizePolicy().hasHeightForWidth())
        self.left_menu.setSizePolicy(sizePolicy)
        self.left_menu.setMinimumSize(QSize(50, 0))
        self.left_menu.setMaximumSize(QSize(50, 16777215))
        self.left_menu.setStyleSheet(u"")
        self.left_menu.setFrameShape(QFrame.NoFrame)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.toggle_btn = MenuBtn(self.left_menu)
        self.toggle_btn.setObjectName(u"toggle_btn")

        self.verticalLayout.addWidget(self.toggle_btn)

        self.home_btn = MenuBtn(self.left_menu)
        self.home_btn.setObjectName(u"home_btn")

        self.verticalLayout.addWidget(self.home_btn)

        self.options_btn = MenuBtn(self.left_menu)
        self.options_btn.setObjectName(u"options_btn")

        self.verticalLayout.addWidget(self.options_btn)

        self.verticalSpacer = QSpacerItem(20, 443, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.about_btn = MenuBtn(self.left_menu)
        self.about_btn.setObjectName(u"about_btn")

        self.verticalLayout.addWidget(self.about_btn)


        self.gridLayout.addWidget(self.left_menu, 0, 0, 1, 1)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.app_pages = QStackedWidget(self.content)
        self.app_pages.setObjectName(u"app_pages")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_4 = QVBoxLayout(self.home_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.home_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.restore_names_btn = QPushButton(self.frame)
        self.restore_names_btn.setObjectName(u"restore_names_btn")
        icon = QIcon()
        icon.addFile(u":/icons/gui/icons/restore.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_names_btn.setIcon(icon)
        self.restore_names_btn.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.restore_names_btn, 3, 6, 1, 3)

        self.apply_btn = QPushButton(self.frame)
        self.apply_btn.setObjectName(u"apply_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/gui/icons/check_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.apply_btn.setIcon(icon1)
        self.apply_btn.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.apply_btn, 3, 11, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 5, 1, 1)

        self.remove_file_name = QPushButton(self.frame)
        self.remove_file_name.setObjectName(u"remove_file_name")
        icon2 = QIcon()
        icon2.addFile(u":/icons/gui/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_file_name.setIcon(icon2)
        self.remove_file_name.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.remove_file_name, 3, 4, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.methods_list = QComboBox(self.frame)
        self.methods_list.addItem("")
        self.methods_list.addItem("")
        self.methods_list.setObjectName(u"methods_list")

        self.gridLayout_2.addWidget(self.methods_list, 0, 2, 1, 1)

        self.empty_table_data_btn = QPushButton(self.frame)
        self.empty_table_data_btn.setObjectName(u"empty_table_data_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/gui/icons/delete_forever.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.empty_table_data_btn.setIcon(icon3)
        self.empty_table_data_btn.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.empty_table_data_btn, 3, 0, 1, 1)

        self.word_entry = QLineEdit(self.frame)
        self.word_entry.setObjectName(u"word_entry")
        self.word_entry.setReadOnly(False)

        self.gridLayout_2.addWidget(self.word_entry, 0, 3, 1, 3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_4, 1, 4, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 6, 1, 1)

        self.letter_num = QSpinBox(self.frame)
        self.letter_num.setObjectName(u"letter_num")

        self.gridLayout_2.addWidget(self.letter_num, 0, 7, 1, 2)

        self.add_files_btn = QPushButton(self.frame)
        self.add_files_btn.setObjectName(u"add_files_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/gui/icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_files_btn.setIcon(icon4)
        self.add_files_btn.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.add_files_btn, 0, 0, 1, 1)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 2, 0, 1, 12)

        self.add_num = QPushButton(self.frame)
        self.add_num.setObjectName(u"add_num")

        self.gridLayout_2.addWidget(self.add_num, 0, 10, 1, 1)


        self.verticalLayout_4.addWidget(self.frame)

        self.files_table = FilesTableWidget(self.home_page)
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

        self.verticalLayout_4.addWidget(self.files_table)

        self.frame_2 = QFrame(self.home_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/gui/icons/rename.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.start_rename_btn.setIcon(icon5)
        self.start_rename_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.start_rename_btn, 0, Qt.AlignHCenter)

        self.current_file_label = QLabel(self.frame_2)
        self.current_file_label.setObjectName(u"current_file_label")

        self.verticalLayout_3.addWidget(self.current_file_label)

        self.total_label = QLabel(self.frame_2)
        self.total_label.setObjectName(u"total_label")

        self.verticalLayout_3.addWidget(self.total_label)

        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_3.addWidget(self.progressBar)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.app_pages.addWidget(self.home_page)
        self.options_page = QWidget()
        self.options_page.setObjectName(u"options_page")
        self.verticalLayout_6 = QVBoxLayout(self.options_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox = QGroupBox(self.options_page)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.rename_radio_btn = QRadioButton(self.groupBox)
        self.rename_radio_btn.setObjectName(u"rename_radio_btn")
        self.rename_radio_btn.setChecked(True)

        self.verticalLayout_5.addWidget(self.rename_radio_btn)

        self.copy_radio_btn = QRadioButton(self.groupBox)
        self.copy_radio_btn.setObjectName(u"copy_radio_btn")

        self.verticalLayout_5.addWidget(self.copy_radio_btn)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setMaximumSize(QSize(300, 16777215))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.save_location_entry = QLineEdit(self.groupBox)
        self.save_location_entry.setObjectName(u"save_location_entry")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.save_location_entry.sizePolicy().hasHeightForWidth())
        self.save_location_entry.setSizePolicy(sizePolicy2)
        self.save_location_entry.setMinimumSize(QSize(280, 0))
        self.save_location_entry.setMaximumSize(QSize(280, 16777215))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.save_location_entry)

        self.save_location_btn = QToolButton(self.groupBox)
        self.save_location_btn.setObjectName(u"save_location_btn")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.save_location_btn)


        self.verticalLayout_5.addLayout(self.formLayout)


        self.verticalLayout_6.addWidget(self.groupBox, 0, Qt.AlignTop)

        self.app_pages.addWidget(self.options_page)

        self.verticalLayout_2.addWidget(self.app_pages)


        self.gridLayout.addWidget(self.content, 0, 1, 1, 1)

        self.bottom_bar = QFrame(self.centralwidget)
        self.bottom_bar.setObjectName(u"bottom_bar")
        self.bottom_bar.setMinimumSize(QSize(0, 25))
        self.bottom_bar.setMaximumSize(QSize(16777215, 25))
        self.bottom_bar.setStyleSheet(u"")
        self.bottom_bar.setFrameShape(QFrame.StyledPanel)
        self.bottom_bar.setFrameShadow(QFrame.Raised)
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setSpacing(0)
        self.bottom_bar_layout.setObjectName(u"bottom_bar_layout")
        self.bottom_bar_layout.setContentsMargins(-1, 0, -1, 0)
        self.author_label = QLabel(self.bottom_bar)
        self.author_label.setObjectName(u"author_label")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.author_label.setFont(font1)

        self.bottom_bar_layout.addWidget(self.author_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottom_bar_layout.addItem(self.horizontalSpacer)

        self.app_version_label = QLabel(self.bottom_bar)
        self.app_version_label.setObjectName(u"app_version_label")
        font2 = QFont()
        font2.setItalic(False)
        self.app_version_label.setFont(font2)

        self.bottom_bar_layout.addWidget(self.app_version_label)


        self.gridLayout.addWidget(self.bottom_bar, 1, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.app_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggle_btn.setText("")
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.options_btn.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.about_btn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.restore_names_btn.setText(QCoreApplication.translate("MainWindow", u"Restore Names", None))
        self.apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.apply_btn.setProperty("colorBtn", QCoreApplication.translate("MainWindow", u"info", None))
        self.remove_file_name.setText(QCoreApplication.translate("MainWindow", u"Remove Files Name", None))
        self.remove_file_name.setProperty("colorBtn", QCoreApplication.translate("MainWindow", u"danger", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Method", None))
        self.methods_list.setItemText(0, QCoreApplication.translate("MainWindow", u"Add", None))
        self.methods_list.setItemText(1, QCoreApplication.translate("MainWindow", u"Remove", None))

        self.empty_table_data_btn.setText(QCoreApplication.translate("MainWindow", u"Empty Table", None))
        self.empty_table_data_btn.setProperty("colorBtn", QCoreApplication.translate("MainWindow", u"danger", None))
        self.word_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Word", None))
        self.label_4.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Letter:", None))
        self.add_files_btn.setText(QCoreApplication.translate("MainWindow", u"Add Files", None))
        self.add_num.setText(QCoreApplication.translate("MainWindow", u"Add Num", None))
        ___qtablewidgetitem = self.files_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"File Name", None));
        ___qtablewidgetitem1 = self.files_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New File Name", None));
        ___qtablewidgetitem2 = self.files_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Path", None));
        self.start_rename_btn.setText(QCoreApplication.translate("MainWindow", u"Start Rename", None))
        self.start_rename_btn.setProperty("startRename", "")
        self.start_rename_btn.setProperty("colorBtn", QCoreApplication.translate("MainWindow", u"success", None))
        self.current_file_label.setText("")
        self.total_label.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.rename_radio_btn.setText(QCoreApplication.translate("MainWindow", u"Rename File in Existing Folder", None))
        self.copy_radio_btn.setText(QCoreApplication.translate("MainWindow", u"Copy Files To New Folder", None))
        self.save_location_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Past path here or choose from button", None))
        self.save_location_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.author_label.setText(QCoreApplication.translate("MainWindow", u"By, Abdelbaset Mansour", None))
        self.app_version_label.setText(QCoreApplication.translate("MainWindow", u"v0.2.0", None))
    # retranslateUi

