# IMPORT QT CORE
from qt_core import *

# IMPORT MODULES
import os


class MenuBtn(QPushButton):
    def __init__(
        self,
        parent=None,
        text="",
        height=40,
        minimum_width=50,
        text_padding=55,
        # ICON UI
        icon_path="",
        icon_color="#303841",
        is_active=False,
    ):
        super().__init__()

        # SET DEFALT PARAMETERS
        self.setParent(parent)
        self.setText(text)
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)

        # SET CUSTOME PARAMETERS
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.is_active = is_active

        # SET STYLE
        self.set_style(is_active=self.is_active)

    # SET ACTIVE
    # -------------------------------------------------------- #
    def set_active(self, is_menu_active):
        self.set_style(is_active=is_menu_active)

    # SET STYLE
    # ================================================================== #
    def set_style(self, is_active):
        active_style = f""" 
            QPushButton {{
                background-color: #f5f6f7;
                padding-left: {self.text_padding - 5}px;
                border-left: 5px solid #2196F3;
            }}
         """
        if is_active:
            self.setStyleSheet(active_style)
        else:
            self.setStyleSheet("")

    # PAINT EVENT
    # ================================================================== #
    def paintEvent(self, evnt):
        # RESTORE DEFAULT STYLE
        super().paintEvent(evnt)

        # Parent Painter
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        # pen
        qp.setPen(Qt.NoPen)
        # Draw
        rect = QRect(0, 0, self.minimum_width, self.height())
        qp.drawRect(rect)

        # FORMAT "ICONS" PATH
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, self.icon_path))

        # DRAW ICON
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), self.icon_color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2, (rect.height() - icon.height()) / 2, icon
        )

        # END ICON PAINTER
        painter.end()

        # ------------------ END PARENT PAINTER ------------------ #
        qp.end()
