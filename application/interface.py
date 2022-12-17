# -*- coding: utf-8 -*-

from . import resources_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1161, 920)
        MainWindow.setMinimumSize(QtCore.QSize(1161, 920))
        MainWindow.setMaximumSize(QtCore.QSize(1161, 920))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icon/sigma_bear.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            'font: 9pt "Segoe UI";\n' "background-color: #121212;"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1141, 901))
        self.tabWidget.setStyleSheet(
            "QTabWidget {\n"
            "    background-color: #121212;\n"
            "}\n"
            "\n"
            "QTabBar::tab {\n"
            "    background-color: #14040B;\n"
            "    color: #53fdca;\n"
            "    border: 1px solid #53fdca;\n"
            "    border-bottom-color: #53fdca; \n"
            "    border-top-left-radius: 2px;\n"
            "    border-top-right-radius: 2px;\n"
            "    padding: 3px;\n"
            "}\n"
            "\n"
            "QTabBar::tab::disabled {\n"
            "    background-color: gray;\n"
            "    color: #53fdca;\n"
            "    border: 1px solid #53fdca;\n"
            "    border-bottom-color: #53fdca; \n"
            "    border-top-left-radius: 2px;\n"
            "    border-top-right-radius: 2px;\n"
            "    padding: 3px;\n"
            "}\n"
            "\n"
            "QTabWidget::tab-bar {\n"
            "    alignment: center;\n"
            "}\n"
            "\n"
            "QTabBar::tab:selected {\n"
            "    background-color: #53fdca;\n"
            "    border: 1px solid #14040B;\n"
            "    color: #14040B;\n"
            "}\n"
            "\n"
            "QTabWidget::pane {\n"
            "    border-top: 2px solid #53fdca;\n"
            "    position: absolute;\n"
            "    top: -0.5em;\n"
            "}"
        )
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_main = QtWidgets.QWidget()
        self.tab_main.setObjectName("tab_main")
        self.maindash_groupBox = QtWidgets.QGroupBox(self.tab_main)
        self.maindash_groupBox.setGeometry(QtCore.QRect(350, 160, 471, 601))
        self.maindash_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: #252525;\n"
            "    border: 2px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex;\n"
            "}\n"
            "\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "    padding: 0px;\n"
            "    border-top: 1px solid #53fdca;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: #292929;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background-image: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: #121212;\n"
            "}"
        )
        self.maindash_groupBox.setTitle("")
        self.maindash_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.maindash_groupBox.setFlat(False)
        self.maindash_groupBox.setObjectName("maindash_groupBox")
        self.mconsole_textBrowser = QtWidgets.QTextBrowser(
            self.maindash_groupBox
        )
        self.mconsole_textBrowser.setGeometry(QtCore.QRect(10, 495, 451, 91))
        self.mconsole_textBrowser.setObjectName("mconsole_textBrowser")
        self.mbackout_label = QtWidgets.QLabel(self.maindash_groupBox)
        self.mbackout_label.setGeometry(QtCore.QRect(160, 470, 151, 21))
        self.mbackout_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mbackout_label.setObjectName("mbackout_label")
        self.validarLogin_pushButton = QtWidgets.QPushButton(
            self.maindash_groupBox
        )
        self.validarLogin_pushButton.setEnabled(True)
        self.validarLogin_pushButton.setGeometry(QtCore.QRect(10, 70, 451, 24))
        self.validarLogin_pushButton.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            ""
        )
        self.validarLogin_pushButton.setObjectName("validarLogin_pushButton")
        self.usuario_lineEdit = QtWidgets.QLineEdit(self.maindash_groupBox)
        self.usuario_lineEdit.setGeometry(QtCore.QRect(10, 30, 211, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush
        )
        self.usuario_lineEdit.setPalette(palette)
        self.usuario_lineEdit.setText("")
        self.usuario_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.usuario_lineEdit.setReadOnly(False)
        self.usuario_lineEdit.setObjectName("usuario_lineEdit")
        self.logo_label = QtWidgets.QLabel(self.maindash_groupBox)
        self.logo_label.setGeometry(QtCore.QRect(10, 110, 451, 351))
        self.logo_label.setStyleSheet("background: none;")
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap(":/other/sigmaicon_clean.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        self.password_lineEdit = QtWidgets.QLineEdit(self.maindash_groupBox)
        self.password_lineEdit.setGeometry(QtCore.QRect(250, 30, 211, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush
        )
        self.password_lineEdit.setPalette(palette)
        self.password_lineEdit.setText("")
        self.password_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.password_lineEdit.setReadOnly(False)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.sigma_version_label = QtWidgets.QLabel(self.maindash_groupBox)
        self.sigma_version_label.setGeometry(QtCore.QRect(73, 410, 313, 51))
        self.sigma_version_label.setStyleSheet(
            'font: 25pt "Segoe UI";\n' "color: white;"
        )
        self.sigma_version_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sigma_version_label.setObjectName("sigma_version_label")
        self.tabWidget.addTab(self.tab_main, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.proPersonas_groupBox = QtWidgets.QGroupBox(self.tab)
        self.proPersonas_groupBox.setGeometry(QtCore.QRect(10, 20, 731, 261))
        self.proPersonas_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: #252525;\n"
            "    border: 2px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex;\n"
            "}\n"
            "\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "    padding: 0px;\n"
            "    border-top: 1px solid #53fdca;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    color: white;\n"
            "    background-color: #252525;\n"
            "    border: 1px solid #53fdca;\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QComboBox {\n"
            "    color: white;\n"
            "    border: 1px solid #53fdca;\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "    background-color: #252525;\n"
            "}\n"
            "\n"
            "QListView {\n"
            "    color: white;\n"
            "}"
        )
        self.proPersonas_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.proPersonas_groupBox.setFlat(False)
        self.proPersonas_groupBox.setObjectName("proPersonas_groupBox")
        self.proEmision_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proEmision_output_lineEdit.setGeometry(
            QtCore.QRect(20, 60, 111, 22)
        )
        self.proEmision_output_lineEdit.setText("")
        self.proEmision_output_lineEdit.setReadOnly(True)
        self.proEmision_output_lineEdit.setObjectName(
            "proEmision_output_lineEdit"
        )
        self.emision_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.emision_label.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.emision_label.setObjectName("emision_label")
        self.nroDocumento_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.nroDocumento_label.setGeometry(QtCore.QRect(150, 40, 91, 16))
        self.nroDocumento_label.setObjectName("nroDocumento_label")
        self.proNroDoc_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proNroDoc_output_lineEdit.setGeometry(
            QtCore.QRect(150, 60, 111, 22)
        )
        self.proNroDoc_output_lineEdit.setText("")
        self.proNroDoc_output_lineEdit.setReadOnly(True)
        self.proNroDoc_output_lineEdit.setObjectName(
            "proNroDoc_output_lineEdit"
        )
        self.proApellido_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proApellido_output_lineEdit.setGeometry(
            QtCore.QRect(280, 60, 111, 22)
        )
        self.proApellido_output_lineEdit.setText("")
        self.proApellido_output_lineEdit.setReadOnly(True)
        self.proApellido_output_lineEdit.setObjectName(
            "proApellido_output_lineEdit"
        )
        self.proApellido_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.proApellido_label.setGeometry(QtCore.QRect(280, 40, 91, 16))
        self.proApellido_label.setObjectName("proApellido_label")
        self.proNombre_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.proNombre_label.setGeometry(QtCore.QRect(410, 40, 91, 16))
        self.proNombre_label.setObjectName("proNombre_label")
        self.proNombre_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proNombre_output_lineEdit.setGeometry(
            QtCore.QRect(410, 60, 161, 22)
        )
        self.proNombre_output_lineEdit.setText("")
        self.proNombre_output_lineEdit.setReadOnly(True)
        self.proNombre_output_lineEdit.setObjectName(
            "proNombre_output_lineEdit"
        )
        self.cuil_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.cuil_label.setGeometry(QtCore.QRect(590, 40, 61, 16))
        self.cuil_label.setObjectName("cuil_label")
        self.proCUIL_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proCUIL_output_lineEdit.setGeometry(
            QtCore.QRect(590, 60, 111, 22)
        )
        self.proCUIL_output_lineEdit.setText("")
        self.proCUIL_output_lineEdit.setReadOnly(True)
        self.proCUIL_output_lineEdit.setObjectName("proCUIL_output_lineEdit")
        self.barrio_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.barrio_label.setGeometry(QtCore.QRect(20, 90, 101, 16))
        self.barrio_label.setObjectName("barrio_label")
        self.proBarrio_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proBarrio_output_lineEdit.setGeometry(
            QtCore.QRect(20, 110, 111, 22)
        )
        self.proBarrio_output_lineEdit.setText("")
        self.proBarrio_output_lineEdit.setReadOnly(True)
        self.proBarrio_output_lineEdit.setObjectName(
            "proBarrio_output_lineEdit"
        )
        self.calle_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.calle_label.setGeometry(QtCore.QRect(150, 90, 71, 16))
        self.calle_label.setObjectName("calle_label")
        self.proCalle_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proCalle_output_lineEdit.setGeometry(
            QtCore.QRect(150, 110, 111, 22)
        )
        self.proCalle_output_lineEdit.setText("")
        self.proCalle_output_lineEdit.setReadOnly(True)
        self.proCalle_output_lineEdit.setObjectName("proCalle_output_lineEdit")
        self.altura_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.altura_label.setGeometry(QtCore.QRect(280, 90, 81, 16))
        self.altura_label.setObjectName("altura_label")
        self.proAltura_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proAltura_output_lineEdit.setGeometry(
            QtCore.QRect(280, 110, 111, 22)
        )
        self.proAltura_output_lineEdit.setText("")
        self.proAltura_output_lineEdit.setReadOnly(True)
        self.proAltura_output_lineEdit.setObjectName(
            "proAltura_output_lineEdit"
        )
        self.piso_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.piso_label.setGeometry(QtCore.QRect(590, 90, 101, 16))
        self.piso_label.setObjectName("piso_label")
        self.proDepartamento_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proDepartamento_output_lineEdit.setGeometry(
            QtCore.QRect(410, 110, 161, 22)
        )
        self.proDepartamento_output_lineEdit.setText("")
        self.proDepartamento_output_lineEdit.setReadOnly(True)
        self.proDepartamento_output_lineEdit.setObjectName(
            "proDepartamento_output_lineEdit"
        )
        self.departamento_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.departamento_label.setGeometry(QtCore.QRect(410, 90, 111, 16))
        self.departamento_label.setObjectName("departamento_label")
        self.proPiso_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proPiso_output_lineEdit.setGeometry(
            QtCore.QRect(590, 110, 111, 22)
        )
        self.proPiso_output_lineEdit.setText("")
        self.proPiso_output_lineEdit.setReadOnly(True)
        self.proPiso_output_lineEdit.setObjectName("proPiso_output_lineEdit")
        self.provincia_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.provincia_label.setGeometry(QtCore.QRect(410, 140, 101, 16))
        self.provincia_label.setObjectName("provincia_label")
        self.proProvincia_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proProvincia_output_lineEdit.setGeometry(
            QtCore.QRect(410, 160, 161, 22)
        )
        self.proProvincia_output_lineEdit.setText("")
        self.proProvincia_output_lineEdit.setReadOnly(True)
        self.proProvincia_output_lineEdit.setObjectName(
            "proProvincia_output_lineEdit"
        )
        self.pais_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.pais_label.setGeometry(QtCore.QRect(590, 140, 81, 16))
        self.pais_label.setObjectName("pais_label")
        self.proPais_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proPais_output_lineEdit.setGeometry(
            QtCore.QRect(590, 160, 111, 22)
        )
        self.proPais_output_lineEdit.setText("")
        self.proPais_output_lineEdit.setReadOnly(True)
        self.proPais_output_lineEdit.setObjectName("proPais_output_lineEdit")
        self.monoblock_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.monoblock_label.setGeometry(QtCore.QRect(20, 140, 91, 16))
        self.monoblock_label.setObjectName("monoblock_label")
        self.proMonoblock_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proMonoblock_output_lineEdit.setGeometry(
            QtCore.QRect(20, 160, 111, 22)
        )
        self.proMonoblock_output_lineEdit.setText("")
        self.proMonoblock_output_lineEdit.setReadOnly(True)
        self.proMonoblock_output_lineEdit.setObjectName(
            "proMonoblock_output_lineEdit"
        )
        self.ciudad_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.ciudad_label.setGeometry(QtCore.QRect(150, 140, 101, 16))
        self.ciudad_label.setObjectName("ciudad_label")
        self.proCiudad_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proCiudad_output_lineEdit.setGeometry(
            QtCore.QRect(150, 160, 111, 22)
        )
        self.proCiudad_output_lineEdit.setText("")
        self.proCiudad_output_lineEdit.setReadOnly(True)
        self.proCiudad_output_lineEdit.setObjectName(
            "proCiudad_output_lineEdit"
        )
        self.municipio_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.municipio_label.setGeometry(QtCore.QRect(280, 140, 101, 16))
        self.municipio_label.setObjectName("municipio_label")
        self.proMunicipio_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proMunicipio_output_lineEdit.setGeometry(
            QtCore.QRect(280, 160, 111, 22)
        )
        self.proMunicipio_output_lineEdit.setText("")
        self.proMunicipio_output_lineEdit.setReadOnly(True)
        self.proMunicipio_output_lineEdit.setObjectName(
            "proMunicipio_output_lineEdit"
        )
        self.fechanac_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.fechanac_label.setGeometry(QtCore.QRect(20, 190, 111, 16))
        self.fechanac_label.setObjectName("fechanac_label")
        self.proFechaNacimiento_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proFechaNacimiento_output_lineEdit.setGeometry(
            QtCore.QRect(20, 210, 111, 22)
        )
        self.proFechaNacimiento_output_lineEdit.setText("")
        self.proFechaNacimiento_output_lineEdit.setReadOnly(True)
        self.proFechaNacimiento_output_lineEdit.setObjectName(
            "proFechaNacimiento_output_lineEdit"
        )
        self.proFallecido_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proFallecido_output_lineEdit.setGeometry(
            QtCore.QRect(150, 210, 111, 22)
        )
        self.proFallecido_output_lineEdit.setText("")
        self.proFallecido_output_lineEdit.setReadOnly(True)
        self.proFallecido_output_lineEdit.setObjectName(
            "proFallecido_output_lineEdit"
        )
        self.fallecido_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.fallecido_label.setGeometry(QtCore.QRect(150, 190, 111, 16))
        self.fallecido_label.setObjectName("fallecido_label")
        self.obraSocial_output_comboBox = QtWidgets.QComboBox(
            self.proPersonas_groupBox
        )
        self.obraSocial_output_comboBox.setGeometry(
            QtCore.QRect(280, 210, 421, 22)
        )
        self.obraSocial_output_comboBox.setObjectName(
            "obraSocial_output_comboBox"
        )
        self.obrassociales_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.obrassociales_label.setGeometry(QtCore.QRect(280, 190, 121, 16))
        self.obrassociales_label.setObjectName("obrassociales_label")
        self.prodashboard_groupBox = QtWidgets.QGroupBox(self.tab)
        self.prodashboard_groupBox.setGeometry(QtCore.QRect(760, 20, 371, 851))
        self.prodashboard_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: #252525;\n"
            "    border: 2px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex;\n"
            "}\n"
            "\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "    padding: 0px;\n"
            "    border-top: 1px solid #53fdca;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: #292929;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: #121212;\n"
            "}\n"
            "\n"
            "QComboBox {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: #292929;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QComboBox::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QListView {\n"
            "    color: white;\n"
            "}\n"
            "\n"
            "QListView {\n"
            "    color: white;\n"
            "}\n"
            "\n"
            "QSpinBox {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: #292929;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QSpinBox::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.prodashboard_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.prodashboard_groupBox.setFlat(False)
        self.prodashboard_groupBox.setObjectName("prodashboard_groupBox")
        self.personas_textBrowser = QtWidgets.QTextBrowser(
            self.prodashboard_groupBox
        )
        self.personas_textBrowser.setGeometry(QtCore.QRect(10, 470, 351, 371))
        self.personas_textBrowser.setObjectName("personas_textBrowser")
        self.probackend_label = QtWidgets.QLabel(self.prodashboard_groupBox)
        self.probackend_label.setGeometry(QtCore.QRect(10, 440, 171, 21))
        self.probackend_label.setObjectName("probackend_label")
        self.dnibuscarpro_label = QtWidgets.QLabel(self.prodashboard_groupBox)
        self.dnibuscarpro_label.setGeometry(QtCore.QRect(30, 46, 141, 20))
        self.dnibuscarpro_label.setObjectName("dnibuscarpro_label")
        self.proDniBuscar_lineEdit = QtWidgets.QLineEdit(
            self.prodashboard_groupBox
        )
        self.proDniBuscar_lineEdit.setGeometry(QtCore.QRect(30, 70, 141, 22))
        self.proDniBuscar_lineEdit.setText("")
        self.proDniBuscar_lineEdit.setReadOnly(False)
        self.proDniBuscar_lineEdit.setObjectName("proDniBuscar_lineEdit")
        self.proBuscarDni_pushButton = QtWidgets.QPushButton(
            self.prodashboard_groupBox
        )
        self.proBuscarDni_pushButton.setGeometry(
            QtCore.QRect(30, 110, 301, 24)
        )
        self.proBuscarDni_pushButton.setObjectName("proBuscarDni_pushButton")
        self.proGenero_comboBox = QtWidgets.QComboBox(
            self.prodashboard_groupBox
        )
        self.proGenero_comboBox.setGeometry(QtCore.QRect(210, 70, 121, 22))
        self.proGenero_comboBox.setObjectName("proGenero_comboBox")
        self.proGenero_comboBox.addItem("")
        self.proGenero_comboBox.addItem("")
        self.dnibuscarpro_label_2 = QtWidgets.QLabel(
            self.prodashboard_groupBox
        )
        self.dnibuscarpro_label_2.setGeometry(QtCore.QRect(210, 46, 121, 20))
        self.dnibuscarpro_label_2.setObjectName("dnibuscarpro_label_2")
        self.proEdadbusc_label = QtWidgets.QLabel(self.prodashboard_groupBox)
        self.proEdadbusc_label.setGeometry(QtCore.QRect(190, 290, 171, 21))
        self.proEdadbusc_label.setObjectName("proEdadbusc_label")
        self.proLocalidadBuscar_lineEdit = QtWidgets.QLineEdit(
            self.prodashboard_groupBox
        )
        self.proLocalidadBuscar_lineEdit.setGeometry(
            QtCore.QRect(30, 320, 141, 22)
        )
        self.proLocalidadBuscar_lineEdit.setText("")
        self.proLocalidadBuscar_lineEdit.setReadOnly(False)
        self.proLocalidadBuscar_lineEdit.setObjectName(
            "proLocalidadBuscar_lineEdit"
        )
        self.proProvincia_comboBox = QtWidgets.QComboBox(
            self.prodashboard_groupBox
        )
        self.proProvincia_comboBox.setGeometry(QtCore.QRect(190, 250, 141, 22))
        self.proProvincia_comboBox.setObjectName("proProvincia_comboBox")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.setItemText(0, "")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proBuscarNombre_pushButton = QtWidgets.QPushButton(
            self.prodashboard_groupBox
        )
        self.proBuscarNombre_pushButton.setGeometry(
            QtCore.QRect(30, 360, 301, 24)
        )
        self.proBuscarNombre_pushButton.setObjectName(
            "proBuscarNombre_pushButton"
        )
        self.proNombreBuscar_lineEdit = QtWidgets.QLineEdit(
            self.prodashboard_groupBox
        )
        self.proNombreBuscar_lineEdit.setGeometry(
            QtCore.QRect(30, 250, 141, 22)
        )
        self.proNombreBuscar_lineEdit.setText("")
        self.proNombreBuscar_lineEdit.setReadOnly(False)
        self.proNombreBuscar_lineEdit.setObjectName("proNombreBuscar_lineEdit")
        self.proNombrebusc_label = QtWidgets.QLabel(self.prodashboard_groupBox)
        self.proNombrebusc_label.setGeometry(QtCore.QRect(30, 225, 141, 21))
        self.proNombrebusc_label.setObjectName("proNombrebusc_label")
        self.proEdadMax_spinBox = QtWidgets.QSpinBox(
            self.prodashboard_groupBox
        )
        self.proEdadMax_spinBox.setGeometry(QtCore.QRect(270, 320, 61, 22))
        self.proEdadMax_spinBox.setMinimum(0)
        self.proEdadMax_spinBox.setMaximum(99)
        self.proEdadMax_spinBox.setProperty("value", 0)
        self.proEdadMax_spinBox.setObjectName("proEdadMax_spinBox")
        self.proEdadMin_spinBox = QtWidgets.QSpinBox(
            self.prodashboard_groupBox
        )
        self.proEdadMin_spinBox.setGeometry(QtCore.QRect(190, 320, 61, 22))
        self.proEdadMin_spinBox.setMinimum(0)
        self.proEdadMin_spinBox.setMaximum(99)
        self.proEdadMin_spinBox.setProperty("value", 0)
        self.proEdadMin_spinBox.setObjectName("proEdadMin_spinBox")
        self.proProvinciabusc_label = QtWidgets.QLabel(
            self.prodashboard_groupBox
        )
        self.proProvinciabusc_label.setGeometry(
            QtCore.QRect(190, 225, 151, 21)
        )
        self.proProvinciabusc_label.setObjectName("proProvinciabusc_label")
        self.proLocalidadbusc_label = QtWidgets.QLabel(
            self.prodashboard_groupBox
        )
        self.proLocalidadbusc_label.setGeometry(QtCore.QRect(30, 290, 141, 21))
        self.proLocalidadbusc_label.setObjectName("proLocalidadbusc_label")
        self.panelPersonas_groupBox = QtWidgets.QGroupBox(self.tab)
        self.panelPersonas_groupBox.setGeometry(
            QtCore.QRect(10, 290, 731, 271)
        )
        self.panelPersonas_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: #252525;\n"
            "    border: 2px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
            "}\n"
            "\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "    padding: 0px;\n"
            "    border-top: 1px solid #53fdca;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    color: white;\n"
            "    background-color: #252525;\n"
            "    border: 1px solid #53fdca;\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "}"
        )
        self.panelPersonas_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.panelPersonas_groupBox.setFlat(False)
        self.panelPersonas_groupBox.setObjectName("panelPersonas_groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.panelPersonas_groupBox
        )
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.panelPersonas_groupBox)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 709, 246))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents
        )
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.panelNumeros_groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.panelNumeros_groupBox_3.setGeometry(
            QtCore.QRect(10, 570, 731, 301)
        )
        self.panelNumeros_groupBox_3.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: #252525;\n"
            "    border: 2px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
            "}\n"
            "\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "    padding: 0px;\n"
            "    border-top: 1px solid #53fdca;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    color: white;\n"
            "    background-color: #3B3B3B;\n"
            "    border: 1px solid #53fdca;\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background-color: none;\n"
            "}"
        )
        self.panelNumeros_groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.panelNumeros_groupBox_3.setFlat(False)
        self.panelNumeros_groupBox_3.setObjectName("panelNumeros_groupBox_3")
        self.proVecinos_tableWidget = QtWidgets.QTableWidget(
            self.panelNumeros_groupBox_3
        )
        self.proVecinos_tableWidget.setGeometry(QtCore.QRect(10, 80, 711, 211))
        self.proVecinos_tableWidget.setStyleSheet(
            "QTableWidget {\n"
            "    color: white;\n"
            "    background-color: #121212;\n"
            "    border: 1px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QTableView QTableCornerButton::section  {\n"
            "    background:  #53fdca;\n"
            "}\n"
            "\n"
            "QHeaderView::section {\n"
            "    color: black;\n"
            "    background-color: #53fdca;\n"
            "}"
        )
        self.proVecinos_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.proVecinos_tableWidget.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded
        )
        self.proVecinos_tableWidget.setObjectName("proVecinos_tableWidget")
        self.proVecinos_tableWidget.setColumnCount(8)
        self.proVecinos_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.proVecinos_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.proVecinos_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.proVecinos_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.proVecinos_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.proVecinos_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.proVecinos_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.proVecinos_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.proVecinos_tableWidget.setHorizontalHeaderItem(7, item)
        self.proVecinos_tableWidget.horizontalHeader().setVisible(True)
        self.proVecinos_tableWidget.horizontalHeader().setCascadingSectionResizes(
            False
        )
        self.proVecinos_tableWidget.horizontalHeader().setDefaultSectionSize(
            82
        )
        self.proVecinos_tableWidget.horizontalHeader().setStretchLastSection(
            True
        )
        self.proVecinos_tableWidget.verticalHeader().setVisible(False)
        self.proVecinos_tableWidget.verticalHeader().setCascadingSectionResizes(
            False
        )
        self.proVecinos_tableWidget.verticalHeader().setStretchLastSection(
            False
        )
        self.proBuscarVecinos_pushButton = QtWidgets.QPushButton(
            self.panelNumeros_groupBox_3
        )
        self.proBuscarVecinos_pushButton.setGeometry(
            QtCore.QRect(480, 40, 181, 24)
        )
        self.proBuscarVecinos_pushButton.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            ""
        )
        self.proBuscarVecinos_pushButton.setObjectName(
            "proBuscarVecinos_pushButton"
        )
        self.proDireccionBuscar_lineEdit = QtWidgets.QLineEdit(
            self.panelNumeros_groupBox_3
        )
        self.proDireccionBuscar_lineEdit.setGeometry(
            QtCore.QRect(50, 40, 401, 22)
        )
        self.proDireccionBuscar_lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: #292929;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.proDireccionBuscar_lineEdit.setText("")
        self.proDireccionBuscar_lineEdit.setReadOnly(False)
        self.proDireccionBuscar_lineEdit.setObjectName(
            "proDireccionBuscar_lineEdit"
        )
        self.direccionbuscarpro_label = QtWidgets.QLabel(
            self.panelNumeros_groupBox_3
        )
        self.direccionbuscarpro_label.setGeometry(
            QtCore.QRect(50, 20, 151, 21)
        )
        self.direccionbuscarpro_label.setObjectName("direccionbuscarpro_label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_medium = QtWidgets.QWidget()
        self.tab_medium.setStyleSheet("")
        self.tab_medium.setObjectName("tab_medium")
        self.panel_patentes_groupBox = QtWidgets.QGroupBox(self.tab_medium)
        self.panel_patentes_groupBox.setGeometry(
            QtCore.QRect(20, 20, 1101, 851)
        )
        self.panel_patentes_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: #252525;\n"
            "    border: 2px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex;\n"
            "}\n"
            "\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "    padding: 0px;\n"
            "    border-top: 1px solid #53fdca;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: #292929;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: #121212;\n"
            "}"
        )
        self.panel_patentes_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.panel_patentes_groupBox.setFlat(False)
        self.panel_patentes_groupBox.setObjectName("panel_patentes_groupBox")
        self.patentes_tableWidget = QtWidgets.QTableWidget(
            self.panel_patentes_groupBox
        )
        self.patentes_tableWidget.setGeometry(QtCore.QRect(10, 30, 1081, 561))
        self.patentes_tableWidget.setStyleSheet(
            "QTableWidget {\n"
            "    color: white;\n"
            "    background-color: #121212;\n"
            "    border: 1px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QTableView QTableCornerButton::section  {\n"
            "    background:  #53fdca;\n"
            "}\n"
            "\n"
            "QHeaderView::section {\n"
            "    color: black;\n"
            "    background-color: #53fdca;\n"
            "}"
        )
        self.patentes_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.patentes_tableWidget.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded
        )
        self.patentes_tableWidget.setObjectName("patentes_tableWidget")
        self.patentes_tableWidget.setColumnCount(14)
        self.patentes_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(13, item)
        self.patentes_tableWidget.horizontalHeader().setDefaultSectionSize(74)
        self.patentes_tableWidget.horizontalHeader().setStretchLastSection(
            True
        )
        self.buscarPatente_pushButton = QtWidgets.QPushButton(
            self.panel_patentes_groupBox
        )
        self.buscarPatente_pushButton.setGeometry(
            QtCore.QRect(830, 800, 231, 24)
        )
        self.buscarPatente_pushButton.setObjectName("buscarPatente_pushButton")
        self.mbackoutput_label = QtWidgets.QLabel(self.panel_patentes_groupBox)
        self.mbackoutput_label.setGeometry(QtCore.QRect(30, 600, 161, 21))
        self.mbackoutput_label.setObjectName("mbackoutput_label")
        self.patentes_textBrowser = QtWidgets.QTextBrowser(
            self.panel_patentes_groupBox
        )
        self.patentes_textBrowser.setGeometry(QtCore.QRect(30, 630, 1031, 131))
        self.patentes_textBrowser.setObjectName("patentes_textBrowser")
        self.patenteBuscar_label = QtWidgets.QLabel(
            self.panel_patentes_groupBox
        )
        self.patenteBuscar_label.setGeometry(QtCore.QRect(30, 770, 141, 20))
        self.patenteBuscar_label.setObjectName("patenteBuscar_label")
        self.patenteBuscar_lineEdit = QtWidgets.QLineEdit(
            self.panel_patentes_groupBox
        )
        self.patenteBuscar_lineEdit.setGeometry(QtCore.QRect(30, 800, 771, 22))
        self.patenteBuscar_lineEdit.setText("")
        self.patenteBuscar_lineEdit.setReadOnly(False)
        self.patenteBuscar_lineEdit.setObjectName("patenteBuscar_lineEdit")
        self.tabWidget.addTab(self.tab_medium, "")
        self.tab_profesional = QtWidgets.QWidget()
        self.tab_profesional.setStyleSheet("")
        self.tab_profesional.setObjectName("tab_profesional")
        self.panelNumeros_groupBox = QtWidgets.QGroupBox(self.tab_profesional)
        self.panelNumeros_groupBox.setGeometry(QtCore.QRect(20, 20, 1101, 621))
        self.panelNumeros_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: #252525;\n"
            "    border: 2px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
            "}\n"
            "\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "    padding: 0px;\n"
            "    border-top: 1px solid #53fdca;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    color: white;\n"
            "    border: 1px solid #53fdca;\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: #292929;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: rgb(0, 0, 0);\n"
            "}"
        )
        self.panelNumeros_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.panelNumeros_groupBox.setFlat(False)
        self.panelNumeros_groupBox.setObjectName("panelNumeros_groupBox")
        self.proNumeros_tableWidget = QtWidgets.QTableWidget(
            self.panelNumeros_groupBox
        )
        self.proNumeros_tableWidget.setGeometry(
            QtCore.QRect(10, 30, 1081, 521)
        )
        self.proNumeros_tableWidget.setStyleSheet(
            "QTableWidget {\n"
            "    color: white;\n"
            "    background-color: #121212;\n"
            "    border: 1px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QTableView QTableCornerButton::section  {\n"
            "    background:  #53fdca;\n"
            "}\n"
            "\n"
            "QHeaderView::section {\n"
            "    color: black;\n"
            "    background-color: #53fdca;\n"
            "}"
        )
        self.proNumeros_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.proNumeros_tableWidget.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded
        )
        self.proNumeros_tableWidget.setObjectName("proNumeros_tableWidget")
        self.proNumeros_tableWidget.setColumnCount(8)
        self.proNumeros_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.proNumeros_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.proNumeros_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.proNumeros_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.proNumeros_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.proNumeros_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.proNumeros_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.proNumeros_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.proNumeros_tableWidget.setHorizontalHeaderItem(7, item)
        self.proNumeros_tableWidget.horizontalHeader().setDefaultSectionSize(
            130
        )
        self.proNumeros_tableWidget.horizontalHeader().setStretchLastSection(
            True
        )
        self.proNumeroBuscar_lineEdit = QtWidgets.QLineEdit(
            self.panelNumeros_groupBox
        )
        self.proNumeroBuscar_lineEdit.setGeometry(
            QtCore.QRect(230, 580, 301, 22)
        )
        self.proNumeroBuscar_lineEdit.setText("")
        self.proNumeroBuscar_lineEdit.setReadOnly(False)
        self.proNumeroBuscar_lineEdit.setObjectName("proNumeroBuscar_lineEdit")
        self.proBuscarNum_pushButton = QtWidgets.QPushButton(
            self.panelNumeros_groupBox
        )
        self.proBuscarNum_pushButton.setGeometry(
            QtCore.QRect(590, 580, 281, 24)
        )
        self.proBuscarNum_pushButton.setObjectName("proBuscarNum_pushButton")
        self.pronumbusc_label = QtWidgets.QLabel(self.panelNumeros_groupBox)
        self.pronumbusc_label.setGeometry(QtCore.QRect(230, 555, 141, 21))
        self.pronumbusc_label.setObjectName("pronumbusc_label")
        self.p3panelnumeor_groupBox = QtWidgets.QGroupBox(self.tab_profesional)
        self.p3panelnumeor_groupBox.setGeometry(
            QtCore.QRect(400, 650, 721, 221)
        )
        self.p3panelnumeor_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: #252525;\n"
            "    border: 2px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
            "}\n"
            "\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "    padding: 0px;\n"
            "    border-top: 1px solid #53fdca;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    color: white;\n"
            "    background-color: #252525;\n"
            "    border: 1px solid #53fdca;\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}"
        )
        self.p3panelnumeor_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.p3panelnumeor_groupBox.setFlat(False)
        self.p3panelnumeor_groupBox.setObjectName("p3panelnumeor_groupBox")
        self.p3nombres2_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelnumeor_groupBox
        )
        self.p3nombres2_output_lineEdit.setGeometry(
            QtCore.QRect(40, 60, 301, 22)
        )
        self.p3nombres2_output_lineEdit.setText("")
        self.p3nombres2_output_lineEdit.setReadOnly(True)
        self.p3nombres2_output_lineEdit.setObjectName(
            "p3nombres2_output_lineEdit"
        )
        self.nombres_label = QtWidgets.QLabel(self.p3panelnumeor_groupBox)
        self.nombres_label.setGeometry(QtCore.QRect(40, 40, 71, 16))
        self.nombres_label.setObjectName("nombres_label")
        self.p3email_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelnumeor_groupBox
        )
        self.p3email_output_lineEdit.setGeometry(
            QtCore.QRect(40, 120, 301, 22)
        )
        self.p3email_output_lineEdit.setText("")
        self.p3email_output_lineEdit.setReadOnly(True)
        self.p3email_output_lineEdit.setObjectName("p3email_output_lineEdit")
        self.email_label = QtWidgets.QLabel(self.p3panelnumeor_groupBox)
        self.email_label.setGeometry(QtCore.QRect(40, 100, 51, 16))
        self.email_label.setObjectName("email_label")
        self.p3numero_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelnumeor_groupBox
        )
        self.p3numero_output_lineEdit.setGeometry(
            QtCore.QRect(400, 120, 281, 22)
        )
        self.p3numero_output_lineEdit.setText("")
        self.p3numero_output_lineEdit.setReadOnly(True)
        self.p3numero_output_lineEdit.setObjectName("p3numero_output_lineEdit")
        self.numer_label = QtWidgets.QLabel(self.p3panelnumeor_groupBox)
        self.numer_label.setGeometry(QtCore.QRect(400, 100, 61, 16))
        self.numer_label.setObjectName("numer_label")
        self.p3apellidos2_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelnumeor_groupBox
        )
        self.p3apellidos2_output_lineEdit.setGeometry(
            QtCore.QRect(400, 60, 281, 22)
        )
        self.p3apellidos2_output_lineEdit.setText("")
        self.p3apellidos2_output_lineEdit.setReadOnly(True)
        self.p3apellidos2_output_lineEdit.setObjectName(
            "p3apellidos2_output_lineEdit"
        )
        self.apellido_label = QtWidgets.QLabel(self.p3panelnumeor_groupBox)
        self.apellido_label.setGeometry(QtCore.QRect(400, 40, 71, 16))
        self.apellido_label.setObjectName("apellido_label")
        self.numberoabuscar_label = QtWidgets.QLabel(
            self.p3panelnumeor_groupBox
        )
        self.numberoabuscar_label.setGeometry(QtCore.QRect(40, 160, 171, 16))
        self.numberoabuscar_label.setObjectName("numberoabuscar_label")
        self.p3numeroBuscar_lineEdit = QtWidgets.QLineEdit(
            self.p3panelnumeor_groupBox
        )
        self.p3numeroBuscar_lineEdit.setGeometry(
            QtCore.QRect(40, 180, 301, 22)
        )
        self.p3numeroBuscar_lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: #292929;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.p3numeroBuscar_lineEdit.setText("")
        self.p3numeroBuscar_lineEdit.setReadOnly(False)
        self.p3numeroBuscar_lineEdit.setObjectName("p3numeroBuscar_lineEdit")
        self.p3buscarDato_pushButton = QtWidgets.QPushButton(
            self.p3panelnumeor_groupBox
        )
        self.p3buscarDato_pushButton.setEnabled(True)
        self.p3buscarDato_pushButton.setGeometry(
            QtCore.QRect(400, 180, 281, 24)
        )
        self.p3buscarDato_pushButton.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            ""
        )
        self.p3buscarDato_pushButton.setObjectName("p3buscarDato_pushButton")
        self.pro2dashboard_groupBox = QtWidgets.QGroupBox(self.tab_profesional)
        self.pro2dashboard_groupBox.setGeometry(
            QtCore.QRect(20, 650, 361, 221)
        )
        self.pro2dashboard_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: #252525;\n"
            "    border: 2px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex;\n"
            "}\n"
            "\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "    padding: 0px;\n"
            "    border-top: 1px solid #53fdca;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: #121212;\n"
            "}\n"
            "\n"
            "QComboBox {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QComboBox::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QListView {\n"
            "    color: white;\n"
            "}\n"
            "\n"
            "QSpinBox {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QSpinBox::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.pro2dashboard_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.pro2dashboard_groupBox.setFlat(False)
        self.pro2dashboard_groupBox.setObjectName("pro2dashboard_groupBox")
        self.numeros_textBrowser = QtWidgets.QTextBrowser(
            self.pro2dashboard_groupBox
        )
        self.numeros_textBrowser.setGeometry(QtCore.QRect(10, 60, 341, 141))
        self.numeros_textBrowser.setObjectName("numeros_textBrowser")
        self.pro2backend_label = QtWidgets.QLabel(self.pro2dashboard_groupBox)
        self.pro2backend_label.setGeometry(QtCore.QRect(10, 30, 181, 21))
        self.pro2backend_label.setObjectName("pro2backend_label")
        self.tabWidget.addTab(self.tab_profesional, "")
        self.tab_profesional_5 = QtWidgets.QWidget()
        self.tab_profesional_5.setObjectName("tab_profesional_5")
        self.pro3dashboard_groupBox = QtWidgets.QGroupBox(
            self.tab_profesional_5
        )
        self.pro3dashboard_groupBox.setGeometry(QtCore.QRect(20, 20, 531, 181))
        self.pro3dashboard_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: #252525;\n"
            "    border: 2px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex;\n"
            "}\n"
            "\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "    padding: 0px;\n"
            "    border-top: 1px solid #53fdca;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: #121212;\n"
            "}"
        )
        self.pro3dashboard_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.pro3dashboard_groupBox.setFlat(False)
        self.pro3dashboard_groupBox.setObjectName("pro3dashboard_groupBox")
        self.banking_textBrowser = QtWidgets.QTextBrowser(
            self.pro3dashboard_groupBox
        )
        self.banking_textBrowser.setGeometry(QtCore.QRect(10, 50, 511, 121))
        self.banking_textBrowser.setObjectName("banking_textBrowser")
        self.pro3backend_label = QtWidgets.QLabel(self.pro3dashboard_groupBox)
        self.pro3backend_label.setGeometry(QtCore.QRect(10, 20, 181, 21))
        self.pro3backend_label.setObjectName("pro3backend_label")
        self.p3panelcvu_groupBox = QtWidgets.QGroupBox(self.tab_profesional_5)
        self.p3panelcvu_groupBox.setGeometry(QtCore.QRect(20, 220, 1101, 271))
        self.p3panelcvu_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: #252525;\n"
            "    border: 2px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
            "}\n"
            "\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "    padding: 0px;\n"
            "    border-top: 1px solid #53fdca;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    color: white;\n"
            "    background-color: #252525;\n"
            "    border: 1px solid #53fdca;\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}"
        )
        self.p3panelcvu_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.p3panelcvu_groupBox.setFlat(False)
        self.p3panelcvu_groupBox.setObjectName("p3panelcvu_groupBox")
        self.p3titular_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelcvu_groupBox
        )
        self.p3titular_output_lineEdit.setGeometry(
            QtCore.QRect(310, 60, 221, 22)
        )
        self.p3titular_output_lineEdit.setText("")
        self.p3titular_output_lineEdit.setReadOnly(True)
        self.p3titular_output_lineEdit.setObjectName(
            "p3titular_output_lineEdit"
        )
        self.titular_label = QtWidgets.QLabel(self.p3panelcvu_groupBox)
        self.titular_label.setGeometry(QtCore.QRect(310, 40, 71, 16))
        self.titular_label.setObjectName("titular_label")
        self.p3banco_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelcvu_groupBox
        )
        self.p3banco_output_lineEdit.setGeometry(
            QtCore.QRect(310, 120, 221, 22)
        )
        self.p3banco_output_lineEdit.setText("")
        self.p3banco_output_lineEdit.setReadOnly(True)
        self.p3banco_output_lineEdit.setObjectName("p3banco_output_lineEdit")
        self.banco_label = QtWidgets.QLabel(self.p3panelcvu_groupBox)
        self.banco_label.setGeometry(QtCore.QRect(310, 100, 49, 16))
        self.banco_label.setObjectName("banco_label")
        self.p3cbucvu_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelcvu_groupBox
        )
        self.p3cbucvu_output_lineEdit.setGeometry(
            QtCore.QRect(310, 170, 471, 22)
        )
        self.p3cbucvu_output_lineEdit.setText("")
        self.p3cbucvu_output_lineEdit.setReadOnly(True)
        self.p3cbucvu_output_lineEdit.setObjectName("p3cbucvu_output_lineEdit")
        self.cbucvu_label = QtWidgets.QLabel(self.p3panelcvu_groupBox)
        self.cbucvu_label.setGeometry(QtCore.QRect(310, 150, 81, 16))
        self.cbucvu_label.setObjectName("cbucvu_label")
        self.p3cuit_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelcvu_groupBox
        )
        self.p3cuit_output_lineEdit.setGeometry(QtCore.QRect(560, 60, 221, 22))
        self.p3cuit_output_lineEdit.setText("")
        self.p3cuit_output_lineEdit.setReadOnly(True)
        self.p3cuit_output_lineEdit.setObjectName("p3cuit_output_lineEdit")
        self.cuit_label = QtWidgets.QLabel(self.p3panelcvu_groupBox)
        self.cuit_label.setGeometry(QtCore.QRect(560, 40, 51, 16))
        self.cuit_label.setObjectName("cuit_label")
        self.p3tipocuenta_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelcvu_groupBox
        )
        self.p3tipocuenta_output_lineEdit.setGeometry(
            QtCore.QRect(560, 120, 221, 22)
        )
        self.p3tipocuenta_output_lineEdit.setText("")
        self.p3tipocuenta_output_lineEdit.setReadOnly(True)
        self.p3tipocuenta_output_lineEdit.setObjectName(
            "p3tipocuenta_output_lineEdit"
        )
        self.tipoCuenta_label = QtWidgets.QLabel(self.p3panelcvu_groupBox)
        self.tipoCuenta_label.setGeometry(QtCore.QRect(560, 100, 81, 16))
        self.tipoCuenta_label.setObjectName("tipoCuenta_label")
        self.cbvucvubuscar_label = QtWidgets.QLabel(self.p3panelcvu_groupBox)
        self.cbvucvubuscar_label.setGeometry(QtCore.QRect(310, 210, 171, 16))
        self.cbvucvubuscar_label.setObjectName("cbvucvubuscar_label")
        self.p3buscarcvuTitular_pushButton = QtWidgets.QPushButton(
            self.p3panelcvu_groupBox
        )
        self.p3buscarcvuTitular_pushButton.setEnabled(True)
        self.p3buscarcvuTitular_pushButton.setGeometry(
            QtCore.QRect(560, 230, 221, 24)
        )
        self.p3buscarcvuTitular_pushButton.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            ""
        )
        self.p3buscarcvuTitular_pushButton.setObjectName(
            "p3buscarcvuTitular_pushButton"
        )
        self.p3cbvubuscar_lineEdit = QtWidgets.QLineEdit(
            self.p3panelcvu_groupBox
        )
        self.p3cbvubuscar_lineEdit.setGeometry(QtCore.QRect(310, 230, 221, 22))
        self.p3cbvubuscar_lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: #292929;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.p3cbvubuscar_lineEdit.setText("")
        self.p3cbvubuscar_lineEdit.setReadOnly(False)
        self.p3cbvubuscar_lineEdit.setObjectName("p3cbvubuscar_lineEdit")
        self.panelEmail_groupBox = QtWidgets.QGroupBox(self.tab_profesional_5)
        self.panelEmail_groupBox.setGeometry(QtCore.QRect(560, 20, 561, 181))
        self.panelEmail_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: #252525;\n"
            "    border: 2px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
            "}\n"
            "\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "    padding: 0px;\n"
            "    border-top: 1px solid #53fdca;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    color: white;\n"
            "    background-color: #252525;\n"
            "    border: 1px solid #53fdca;\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}"
        )
        self.panelEmail_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.panelEmail_groupBox.setFlat(False)
        self.panelEmail_groupBox.setObjectName("panelEmail_groupBox")
        self.p3nombres_output_lineEdit = QtWidgets.QLineEdit(
            self.panelEmail_groupBox
        )
        self.p3nombres_output_lineEdit.setGeometry(
            QtCore.QRect(40, 60, 221, 22)
        )
        self.p3nombres_output_lineEdit.setText("")
        self.p3nombres_output_lineEdit.setReadOnly(True)
        self.p3nombres_output_lineEdit.setObjectName(
            "p3nombres_output_lineEdit"
        )
        self.p3nombres_label = QtWidgets.QLabel(self.panelEmail_groupBox)
        self.p3nombres_label.setGeometry(QtCore.QRect(40, 40, 71, 16))
        self.p3nombres_label.setObjectName("p3nombres_label")
        self.p3apellido_output_lineEdit = QtWidgets.QLineEdit(
            self.panelEmail_groupBox
        )
        self.p3apellido_output_lineEdit.setGeometry(
            QtCore.QRect(290, 60, 221, 22)
        )
        self.p3apellido_output_lineEdit.setText("")
        self.p3apellido_output_lineEdit.setReadOnly(True)
        self.p3apellido_output_lineEdit.setObjectName(
            "p3apellido_output_lineEdit"
        )
        self.p3apellido_label = QtWidgets.QLabel(self.panelEmail_groupBox)
        self.p3apellido_label.setGeometry(QtCore.QRect(290, 40, 101, 16))
        self.p3apellido_label.setObjectName("p3apellido_label")
        self.p3emailBuscar_label = QtWidgets.QLabel(self.panelEmail_groupBox)
        self.p3emailBuscar_label.setGeometry(QtCore.QRect(40, 100, 171, 16))
        self.p3emailBuscar_label.setObjectName("p3emailBuscar_label")
        self.p3emailBuscar_lineEdit = QtWidgets.QLineEdit(
            self.panelEmail_groupBox
        )
        self.p3emailBuscar_lineEdit.setGeometry(QtCore.QRect(40, 120, 221, 22))
        self.p3emailBuscar_lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: #292929;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.p3emailBuscar_lineEdit.setText("")
        self.p3emailBuscar_lineEdit.setReadOnly(False)
        self.p3emailBuscar_lineEdit.setObjectName("p3emailBuscar_lineEdit")
        self.p3emailBuscar_pushButton = QtWidgets.QPushButton(
            self.panelEmail_groupBox
        )
        self.p3emailBuscar_pushButton.setEnabled(True)
        self.p3emailBuscar_pushButton.setGeometry(
            QtCore.QRect(290, 120, 221, 24)
        )
        self.p3emailBuscar_pushButton.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            ""
        )
        self.p3emailBuscar_pushButton.setObjectName("p3emailBuscar_pushButton")
        self.mdatabreach_groupBox = QtWidgets.QGroupBox(self.tab_profesional_5)
        self.mdatabreach_groupBox.setGeometry(QtCore.QRect(20, 510, 1101, 361))
        self.mdatabreach_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: #252525;\n"
            "    border: 2px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex;\n"
            "}\n"
            "\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "    padding: 0px;\n"
            "    border-top: 1px solid #53fdca;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: #292929;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: rgb(0, 0, 0);\n"
            "}"
        )
        self.mdatabreach_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.mdatabreach_groupBox.setFlat(False)
        self.mdatabreach_groupBox.setObjectName("mdatabreach_groupBox")
        self.querybreach_label = QtWidgets.QLabel(self.mdatabreach_groupBox)
        self.querybreach_label.setGeometry(QtCore.QRect(310, 26, 71, 20))
        self.querybreach_label.setObjectName("querybreach_label")
        self.queryBreach_lineEdit = QtWidgets.QLineEdit(
            self.mdatabreach_groupBox
        )
        self.queryBreach_lineEdit.setGeometry(QtCore.QRect(310, 50, 221, 22))
        self.queryBreach_lineEdit.setText("")
        self.queryBreach_lineEdit.setReadOnly(False)
        self.queryBreach_lineEdit.setObjectName("queryBreach_lineEdit")
        self.buscarLeaks_pushButton = QtWidgets.QPushButton(
            self.mdatabreach_groupBox
        )
        self.buscarLeaks_pushButton.setGeometry(QtCore.QRect(560, 50, 221, 24))
        self.buscarLeaks_pushButton.setObjectName("buscarLeaks_pushButton")
        self.dataBreachResults_tableWidget = QtWidgets.QTableWidget(
            self.mdatabreach_groupBox
        )
        self.dataBreachResults_tableWidget.setGeometry(
            QtCore.QRect(20, 90, 1061, 241)
        )
        self.dataBreachResults_tableWidget.setStyleSheet(
            "QTableWidget {\n"
            "    color: white;\n"
            "    background-color: #121212;\n"
            "    border: 1px solid #53fdca;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QTableView QTableCornerButton::section  {\n"
            "    background:  #53fdca;\n"
            "}\n"
            "\n"
            "QHeaderView::section {\n"
            "    color: black;\n"
            "    background-color: #53fdca;\n"
            "}"
        )
        self.dataBreachResults_tableWidget.setFrameShape(
            QtWidgets.QFrame.NoFrame
        )
        self.dataBreachResults_tableWidget.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded
        )
        self.dataBreachResults_tableWidget.setObjectName(
            "dataBreachResults_tableWidget"
        )
        self.dataBreachResults_tableWidget.setColumnCount(2)
        self.dataBreachResults_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dataBreachResults_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataBreachResults_tableWidget.setHorizontalHeaderItem(1, item)
        self.dataBreachResults_tableWidget.horizontalHeader().setDefaultSectionSize(
            500
        )
        self.dataBreachResults_tableWidget.horizontalHeader().setStretchLastSection(
            True
        )
        self.tabWidget.addTab(self.tab_profesional_5, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Sigma Credits (Balance: Not logged)")
        )
        self.mconsole_textBrowser.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.mbackout_label.setText(_translate("MainWindow", "Backend output"))
        self.validarLogin_pushButton.setText(_translate("MainWindow", "Login"))
        self.usuario_lineEdit.setPlaceholderText(
            _translate("MainWindow", "Usuario")
        )
        self.password_lineEdit.setPlaceholderText(
            _translate("MainWindow", "Contraseña")
        )
        self.sigma_version_label.setText(
            _translate("MainWindow", "Sigma Credits")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_main),
            _translate("MainWindow", "Main Menu"),
        )
        self.proPersonas_groupBox.setTitle(
            _translate("MainWindow", "Panel de datos por DNI")
        )
        self.emision_label.setText(_translate("MainWindow", "Emision"))
        self.nroDocumento_label.setText(
            _translate("MainWindow", "Nro. Documento")
        )
        self.proApellido_label.setText(_translate("MainWindow", "Apellido"))
        self.proNombre_label.setText(_translate("MainWindow", "Nombres"))
        self.cuil_label.setText(_translate("MainWindow", "CUIL"))
        self.barrio_label.setText(_translate("MainWindow", "Barrio"))
        self.calle_label.setText(_translate("MainWindow", "Calle"))
        self.altura_label.setText(_translate("MainWindow", "Altura"))
        self.piso_label.setText(_translate("MainWindow", "Piso"))
        self.departamento_label.setText(
            _translate("MainWindow", "Departamento")
        )
        self.provincia_label.setText(_translate("MainWindow", "Provincia"))
        self.pais_label.setText(_translate("MainWindow", "Pais"))
        self.monoblock_label.setText(_translate("MainWindow", "Monoblock"))
        self.ciudad_label.setText(_translate("MainWindow", "Ciudad"))
        self.municipio_label.setText(_translate("MainWindow", "Municipio"))
        self.fechanac_label.setText(
            _translate("MainWindow", "Fecha Nacimiento")
        )
        self.fallecido_label.setText(_translate("MainWindow", "Fallecido"))
        self.obrassociales_label.setText(
            _translate("MainWindow", "Obras sociales")
        )
        self.prodashboard_groupBox.setTitle(
            _translate("MainWindow", "Dashboard")
        )
        self.personas_textBrowser.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.probackend_label.setText(
            _translate("MainWindow", "Backend output")
        )
        self.dnibuscarpro_label.setText(
            _translate("MainWindow", "DNI a buscar")
        )
        self.proBuscarDni_pushButton.setText(
            _translate("MainWindow", "Buscar por DNI (Costo: $0.25)")
        )
        self.proGenero_comboBox.setItemText(
            0, _translate("MainWindow", "Masculino")
        )
        self.proGenero_comboBox.setItemText(
            1, _translate("MainWindow", "Femenino")
        )
        self.dnibuscarpro_label_2.setText(
            _translate("MainWindow", "Genero DNI")
        )
        self.proEdadbusc_label.setText(
            _translate("MainWindow", "Edad desde - hasta (Opcional)")
        )
        self.proProvincia_comboBox.setItemText(
            1, _translate("MainWindow", "capital_federal")
        )
        self.proProvincia_comboBox.setItemText(
            2, _translate("MainWindow", "buenos_aires")
        )
        self.proProvincia_comboBox.setItemText(
            3, _translate("MainWindow", "catamarca")
        )
        self.proProvincia_comboBox.setItemText(
            4, _translate("MainWindow", "chaco")
        )
        self.proProvincia_comboBox.setItemText(
            5, _translate("MainWindow", "chubut")
        )
        self.proProvincia_comboBox.setItemText(
            6, _translate("MainWindow", "cordoba")
        )
        self.proProvincia_comboBox.setItemText(
            7, _translate("MainWindow", "corrientes")
        )
        self.proProvincia_comboBox.setItemText(
            8, _translate("MainWindow", "entre_rios")
        )
        self.proProvincia_comboBox.setItemText(
            9, _translate("MainWindow", "formosa")
        )
        self.proProvincia_comboBox.setItemText(
            10, _translate("MainWindow", "jujuy")
        )
        self.proProvincia_comboBox.setItemText(
            11, _translate("MainWindow", "la_pampa")
        )
        self.proProvincia_comboBox.setItemText(
            12, _translate("MainWindow", "la_rioja")
        )
        self.proProvincia_comboBox.setItemText(
            13, _translate("MainWindow", "mendoza")
        )
        self.proProvincia_comboBox.setItemText(
            14, _translate("MainWindow", "misiones")
        )
        self.proProvincia_comboBox.setItemText(
            15, _translate("MainWindow", "neuquen")
        )
        self.proProvincia_comboBox.setItemText(
            16, _translate("MainWindow", "rio_negro")
        )
        self.proProvincia_comboBox.setItemText(
            17, _translate("MainWindow", "salta")
        )
        self.proProvincia_comboBox.setItemText(
            18, _translate("MainWindow", "san_juan")
        )
        self.proProvincia_comboBox.setItemText(
            19, _translate("MainWindow", "san_luis")
        )
        self.proProvincia_comboBox.setItemText(
            20, _translate("MainWindow", "santa_cruz")
        )
        self.proProvincia_comboBox.setItemText(
            21, _translate("MainWindow", "santa_fe")
        )
        self.proProvincia_comboBox.setItemText(
            22, _translate("MainWindow", "santiago_del_estero")
        )
        self.proProvincia_comboBox.setItemText(
            23, _translate("MainWindow", "tierra_del_fuego")
        )
        self.proProvincia_comboBox.setItemText(
            24, _translate("MainWindow", "tucuman")
        )
        self.proBuscarNombre_pushButton.setText(
            _translate("MainWindow", "Buscar por nombre (Costo: $0.25)")
        )
        self.proNombrebusc_label.setText(
            _translate("MainWindow", "Nombre/DNI a buscar")
        )
        self.proProvinciabusc_label.setText(
            _translate("MainWindow", "Provincia (Opcional)")
        )
        self.proLocalidadbusc_label.setText(
            _translate("MainWindow", "Localidad (Opcional)")
        )
        self.panelPersonas_groupBox.setTitle(
            _translate("MainWindow", "Panel de personas")
        )
        self.panelNumeros_groupBox_3.setTitle(
            _translate("MainWindow", "Panel de vecinos")
        )
        self.proVecinos_tableWidget.setWhatsThis(
            _translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>"
            )
        )
        item = self.proVecinos_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Documento"))
        item = self.proVecinos_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.proVecinos_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Telefono"))
        item = self.proVecinos_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Empresa"))
        item = self.proVecinos_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Direccion"))
        item = self.proVecinos_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Localidad"))
        item = self.proVecinos_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Provincia"))
        item = self.proVecinos_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "C. Postal"))
        self.proBuscarVecinos_pushButton.setText(
            _translate("MainWindow", "Buscar vecinos (Costo: $0.25)")
        )
        self.direccionbuscarpro_label.setText(
            _translate("MainWindow", "Direccion a buscar")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            _translate("MainWindow", "Personas"),
        )
        self.panel_patentes_groupBox.setTitle(
            _translate("MainWindow", "Panel de patentes")
        )
        item = self.patentes_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Patente"))
        item = self.patentes_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.patentes_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Vehiculo"))
        item = self.patentes_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Marca"))
        item = self.patentes_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Año"))
        item = self.patentes_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Titular"))
        item = self.patentes_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "%"))
        item = self.patentes_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Calle"))
        item = self.patentes_tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Altura"))
        item = self.patentes_tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Piso"))
        item = self.patentes_tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Depto"))
        item = self.patentes_tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "C. Postal"))
        item = self.patentes_tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Localidad"))
        item = self.patentes_tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Tramite"))
        self.buscarPatente_pushButton.setText(
            _translate("MainWindow", "Buscar por patente (Costo: $0.25)")
        )
        self.mbackoutput_label.setText(
            _translate("MainWindow", "Backend output")
        )
        self.patentes_textBrowser.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.patenteBuscar_label.setText(
            _translate("MainWindow", "Patente a buscar")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_medium),
            _translate("MainWindow", "Patentes"),
        )
        self.panelNumeros_groupBox.setTitle(
            _translate("MainWindow", "Panel de datos por numero")
        )
        self.proNumeros_tableWidget.setWhatsThis(
            _translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>"
            )
        )
        item = self.proNumeros_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Celular"))
        item = self.proNumeros_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Documento"))
        item = self.proNumeros_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.proNumeros_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Direccion"))
        item = self.proNumeros_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Localidad"))
        item = self.proNumeros_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Provincia"))
        item = self.proNumeros_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "C. Postal"))
        item = self.proNumeros_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Empresa"))
        self.proBuscarNum_pushButton.setText(
            _translate("MainWindow", "Buscar por numero (Costo: $0.25)")
        )
        self.pronumbusc_label.setText(
            _translate("MainWindow", "Numero a buscar")
        )
        self.p3panelnumeor_groupBox.setTitle(
            _translate("MainWindow", "Panel de datos por numero II")
        )
        self.nombres_label.setText(_translate("MainWindow", "Nombres"))
        self.email_label.setText(_translate("MainWindow", "Email"))
        self.numer_label.setText(_translate("MainWindow", "Numero"))
        self.apellido_label.setText(_translate("MainWindow", "Apellido"))
        self.numberoabuscar_label.setText(
            _translate("MainWindow", "Numero a buscar")
        )
        self.p3buscarDato_pushButton.setText(
            _translate("MainWindow", "Buscar datos (Costo: $0.25)")
        )
        self.pro2dashboard_groupBox.setTitle(
            _translate("MainWindow", "Dashboard")
        )
        self.numeros_textBrowser.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.pro2backend_label.setText(
            _translate("MainWindow", "Backend output")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_profesional),
            _translate("MainWindow", "Numeros"),
        )
        self.pro3dashboard_groupBox.setTitle(
            _translate("MainWindow", "Dashboard")
        )
        self.banking_textBrowser.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.pro3backend_label.setText(
            _translate("MainWindow", "Backend output")
        )
        self.p3panelcvu_groupBox.setTitle(
            _translate("MainWindow", "Panel de datos por CBU/CVU")
        )
        self.titular_label.setText(_translate("MainWindow", "Titular"))
        self.banco_label.setText(_translate("MainWindow", "Banco"))
        self.cbucvu_label.setText(_translate("MainWindow", "CBU/CVU"))
        self.cuit_label.setText(_translate("MainWindow", "Cuit"))
        self.tipoCuenta_label.setText(
            _translate("MainWindow", "Tipo de cuenta")
        )
        self.cbvucvubuscar_label.setText(
            _translate("MainWindow", "CBU/CVU o alias a buscar")
        )
        self.p3buscarcvuTitular_pushButton.setText(
            _translate("MainWindow", "Buscar titular (Costo: 0.25)")
        )
        self.panelEmail_groupBox.setTitle(
            _translate("MainWindow", "Panel de datos por email")
        )
        self.p3nombres_label.setText(_translate("MainWindow", "Nombres"))
        self.p3apellido_label.setText(_translate("MainWindow", "Apellido"))
        self.p3emailBuscar_label.setText(
            _translate("MainWindow", "Email a buscar")
        )
        self.p3emailBuscar_pushButton.setText(
            _translate("MainWindow", "Buscar por email (Costo: $0.25)")
        )
        self.mdatabreach_groupBox.setTitle(
            _translate("MainWindow", "Data breach")
        )
        self.querybreach_label.setText(_translate("MainWindow", "Query"))
        self.buscarLeaks_pushButton.setText(
            _translate("MainWindow", "Buscar leaks (Costo: 0.25)")
        )
        item = self.dataBreachResults_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Email"))
        item = self.dataBreachResults_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Password"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_profesional_5),
            _translate("MainWindow", "Banking"),
        )
