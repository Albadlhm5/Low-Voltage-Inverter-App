# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 662)
        MainWindow.setStyleSheet(u"/* --------------------------------------------------------- */\n"
"/* FONDO GENERAL VENTANA PRINCIPAL                */\n"
"/* --------------------------------------------------------- */\n"
"QMainWindow {\n"
"    background-color: #F5F7FA;\n"
"}\n"
"\n"
"/* --------------------------------------------------------- */\n"
"/* ESTILO GENERAL DE LOS GROUPBOX                      */\n"
"/* Cambio de:\n"
"   - color de fondo de los bloques\n"
"   - borde\n"
"   - esquinas redondeadas\n"
"   - color del t\u00edtulo\n"
"*/\n"
"/* --------------------------------------------------------- */\n"
"QGroupBox {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #D9E1EA;\n"
"    border-radius: 8px;\n"
"    margin-top: 10px;\n"
"    font-weight: 600;\n"
"    color: #1F4E79;\n"
"}\n"
"\n"
"/* --------------------------------------------------------- */\n"
"/* T\u00cdTULO DE LOS GROUPBOX                                    */\n"
"/* Posici\u00f3n y espacio del t\u00edtulo */\n"
"/* -----------------------------------"
                        "---------------------- */\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 4px 0 4px;\n"
"}\n"
"\n"
"/* --------------------------------------------------------- */\n"
"/* ESTILO DE CAJAS DE ENTRADA                                */\n"
"/* Afecta a:\n"
"   - QDoubleSpinBox\n"
"   - QSpinBox\n"
"   - QComboBox\n"
"   - QLineEdit\n"
"   - QPlainTextEdit\n"
"\n"
"   Cambio de:\n"
"   - fondo blanco\n"
"   - borde gris suave\n"
"   - esquinas redondeadas\n"
"   - color del texto\n"
"*/\n"
"/* --------------------------------------------------------- */\n"
"QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QPlainTextEdit {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #C8D2DC;\n"
"    border-radius: 6px;\n"
"    padding: 4px 6px;\n"
"    color: #2F3A45;\n"
"}\n"
"\n"
"/* --------------------------------------------------------- */\n"
"/* EFECTO CUANDO HACES CLIC EN UNA CAJA                      */\n"
"/* Cambia el borde al seleccionar el widget           "
                        "       */\n"
"/* --------------------------------------------------------- */\n"
"QDoubleSpinBox:focus, QSpinBox:focus, QComboBox:focus, QLineEdit:focus, QPlainTextEdit:focus {\n"
"    border: 1px solid #5AA9E6;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"    background-color: #f3f4f6;\n"
"    color: #1f2937;\n"
"    border: 1px solid #d1d5db;\n"
"    border-radius: 7px;\n"
"    padding: 1px 6px;\n"
"    min-height: 22px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e5e7eb;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d1d5db;\n"
"}\n"
"\n"
"/* BOTONES AZULES */\n"
"QPushButton#connectButton,\n"
"QPushButton#startButton,\n"
"QPushButton#startIdentificationButton {\n"
"    background-color: #bfe9f5;\n"
"    color: #0f172a;\n"
"    border: 1px solid #8fd3e8;\n"
"}\n"
"\n"
"QPushButton#connectButton:hover,\n"
"QPushButton#startButton:hover,\n"
"QPushButton#startIdentificationButton:hover {\n"
"    background-color: #a9dfef;\n"
"}\n"
"\n"
"QPushButton#connectButton:pressed,\n"
"QPushButton#startButton:pressed,\n"
"QPushButton#startIdentificationButton:pressed {\n"
"    background-color: #93d4e8;\n"
"}\n"
"\n"
"/* BOTONES ROJOS PASTEL */\n"
"QPushButton#disconnectButton,\n"
"QPushButton#s"
                        "topButton,\n"
"QPushButton#stopIdentificationButton {\n"
"    background-color: #f8c7c7;\n"
"    color: #7f1d1d;\n"
"    border: 1px solid #efb0b0;\n"
"}\n"
"\n"
"QPushButton#disconnectButton:hover,\n"
"QPushButton#stopButton:hover,\n"
"QPushButton#stopIdentificationButton:hover {\n"
"    background-color: #f5b6b6;\n"
"}\n"
"\n"
"QPushButton#disconnectButton:pressed,\n"
"QPushButton#stopButton:pressed,\n"
"QPushButton#stopIdentificationButton:pressed {\n"
"    background-color: #eea4a4;\n"
"}\n"
"\n"
"/* BOTONES GRISES ELEGANTES */\n"
"QPushButton#defaultsButton,\n"
"QPushButton#exportButton,\n"
"QPushButton#applyParametersButton {\n"
"    background-color: #f5f5f5;\n"
"    color: #374151;\n"
"    border: 1px solid #d6d6d6;\n"
"}\n"
"\n"
"QPushButton#defaultsButton:hover,\n"
"QPushButton#exportButton:hover,\n"
"QPushButton#applyParametersButton:hover {\n"
"    background-color: #ebebeb;\n"
"}\n"
"\n"
"QPushButton#defaultsButton:pressed,\n"
"QPushButton#exportButton:pressed,\n"
"QPushButton#applyParametersButto"
                        "n:pressed {\n"
"    background-color: #dfdfdf;\n"
"}\n"
"QProgressBar#identificationProgressBar {\n"
"    background-color: #f1f5f4;\n"
"    border: 1px solid #d8e1df;\n"
"    border-radius: 8px;\n"
"    min-height: 12px;\n"
"    max-height: 12px;\n"
"}\n"
"\n"
"QProgressBar#identificationProgressBar::chunk {\n"
"    background-color: #a8e6b0;\n"
"    border-radius: 8px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_9 = QGroupBox(self.groupBox_5)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.formLayout = QFormLayout(self.groupBox_9)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox_9)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.dcVoltageSpinBox = QDoubleSpinBox(self.groupBox_9)
        self.dcVoltageSpinBox.setObjectName(u"dcVoltageSpinBox")
        self.dcVoltageSpinBox.setMaximumSize(QSize(80, 16777215))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.dcVoltageSpinBox)

        self.label_2 = QLabel(self.groupBox_9)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.currentLimitPeakSpinBox = QDoubleSpinBox(self.groupBox_9)
        self.currentLimitPeakSpinBox.setObjectName(u"currentLimitPeakSpinBox")
        self.currentLimitPeakSpinBox.setMaximumSize(QSize(80, 16777215))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.currentLimitPeakSpinBox)

        self.label_3 = QLabel(self.groupBox_9)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.speedLimitSpinBox = QDoubleSpinBox(self.groupBox_9)
        self.speedLimitSpinBox.setObjectName(u"speedLimitSpinBox")
        self.speedLimitSpinBox.setMaximumSize(QSize(80, 16777215))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.speedLimitSpinBox)

        self.label_4 = QLabel(self.groupBox_9)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.polePairsSpinBox = QDoubleSpinBox(self.groupBox_9)
        self.polePairsSpinBox.setObjectName(u"polePairsSpinBox")
        self.polePairsSpinBox.setMaximumSize(QSize(80, 16777215))

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.polePairsSpinBox)


        self.verticalLayout_2.addWidget(self.groupBox_9)

        self.groupBox_8 = QGroupBox(self.groupBox_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.formLayout_2 = QFormLayout(self.groupBox_8)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_5 = QLabel(self.groupBox_8)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.label_6 = QLabel(self.groupBox_8)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.label_7 = QLabel(self.groupBox_8)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.label_8 = QLabel(self.groupBox_8)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.dAxisCurrentRefSpinBox = QDoubleSpinBox(self.groupBox_8)
        self.dAxisCurrentRefSpinBox.setObjectName(u"dAxisCurrentRefSpinBox")
        self.dAxisCurrentRefSpinBox.setMaximumSize(QSize(80, 16777215))

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.dAxisCurrentRefSpinBox)

        self.qAxisCurrentRefSpinBox = QDoubleSpinBox(self.groupBox_8)
        self.qAxisCurrentRefSpinBox.setObjectName(u"qAxisCurrentRefSpinBox")
        self.qAxisCurrentRefSpinBox.setMaximumSize(QSize(80, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.qAxisCurrentRefSpinBox)

        self.currentKpSpinBox = QDoubleSpinBox(self.groupBox_8)
        self.currentKpSpinBox.setObjectName(u"currentKpSpinBox")
        self.currentKpSpinBox.setMaximumSize(QSize(80, 16777215))

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.currentKpSpinBox)

        self.currentKiSpinBox = QDoubleSpinBox(self.groupBox_8)
        self.currentKiSpinBox.setObjectName(u"currentKiSpinBox")
        self.currentKiSpinBox.setMaximumSize(QSize(80, 16777215))

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.currentKiSpinBox)


        self.verticalLayout_2.addWidget(self.groupBox_8)

        self.groupBox_7 = QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.formLayout_3 = QFormLayout(self.groupBox_7)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_9 = QLabel(self.groupBox_7)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.label_11 = QLabel(self.groupBox_7)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.label_12 = QLabel(self.groupBox_7)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.overcurrentProtectionSpinBox = QDoubleSpinBox(self.groupBox_7)
        self.overcurrentProtectionSpinBox.setObjectName(u"overcurrentProtectionSpinBox")
        self.overcurrentProtectionSpinBox.setMaximumSize(QSize(80, 16777215))

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.overcurrentProtectionSpinBox)

        self.undervoltageProtectionSpinBox = QDoubleSpinBox(self.groupBox_7)
        self.undervoltageProtectionSpinBox.setObjectName(u"undervoltageProtectionSpinBox")
        self.undervoltageProtectionSpinBox.setMaximumSize(QSize(80, 16777215))

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.undervoltageProtectionSpinBox)

        self.overvoltageProtectionSpinBox = QDoubleSpinBox(self.groupBox_7)
        self.overvoltageProtectionSpinBox.setObjectName(u"overvoltageProtectionSpinBox")
        self.overvoltageProtectionSpinBox.setMaximumSize(QSize(80, 16777215))

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.overvoltageProtectionSpinBox)

        self.temperatureLimitSpinBox = QDoubleSpinBox(self.groupBox_7)
        self.temperatureLimitSpinBox.setObjectName(u"temperatureLimitSpinBox")
        self.temperatureLimitSpinBox.setMaximumSize(QSize(80, 16777215))

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.temperatureLimitSpinBox)


        self.verticalLayout_2.addWidget(self.groupBox_7)

        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.connectButton = QPushButton(self.groupBox_6)
        self.connectButton.setObjectName(u"connectButton")

        self.horizontalLayout_2.addWidget(self.connectButton)

        self.defaultsButton = QPushButton(self.groupBox_6)
        self.defaultsButton.setObjectName(u"defaultsButton")

        self.horizontalLayout_2.addWidget(self.defaultsButton)

        self.disconnectButton = QPushButton(self.groupBox_6)
        self.disconnectButton.setObjectName(u"disconnectButton")

        self.horizontalLayout_2.addWidget(self.disconnectButton)


        self.verticalLayout_2.addWidget(self.groupBox_6)


        self.horizontalLayout.addWidget(self.groupBox_5)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_13 = QGroupBox(self.groupBox_4)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.signal1ComboBox = QComboBox(self.groupBox_13)
        self.signal1ComboBox.addItem("")
        self.signal1ComboBox.addItem("")
        self.signal1ComboBox.addItem("")
        self.signal1ComboBox.addItem("")
        self.signal1ComboBox.addItem("")
        self.signal1ComboBox.addItem("")
        self.signal1ComboBox.addItem("")
        self.signal1ComboBox.addItem("")
        self.signal1ComboBox.addItem("")
        self.signal1ComboBox.setObjectName(u"signal1ComboBox")

        self.verticalLayout_4.addWidget(self.signal1ComboBox)

        self.signal2ComboBox = QComboBox(self.groupBox_13)
        self.signal2ComboBox.addItem("")
        self.signal2ComboBox.addItem("")
        self.signal2ComboBox.addItem("")
        self.signal2ComboBox.addItem("")
        self.signal2ComboBox.addItem("")
        self.signal2ComboBox.addItem("")
        self.signal2ComboBox.addItem("")
        self.signal2ComboBox.addItem("")
        self.signal2ComboBox.addItem("")
        self.signal2ComboBox.setObjectName(u"signal2ComboBox")

        self.verticalLayout_4.addWidget(self.signal2ComboBox)


        self.verticalLayout_3.addWidget(self.groupBox_13)

        self.groupBox_12 = QGroupBox(self.groupBox_4)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.plotFrame = QFrame(self.groupBox_12)
        self.plotFrame.setObjectName(u"plotFrame")
        self.plotFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.plotFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_5.addWidget(self.plotFrame)


        self.verticalLayout_3.addWidget(self.groupBox_12)

        self.groupBox_11 = QGroupBox(self.groupBox_4)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.startButton = QPushButton(self.groupBox_11)
        self.startButton.setObjectName(u"startButton")

        self.horizontalLayout_3.addWidget(self.startButton)

        self.stopButton = QPushButton(self.groupBox_11)
        self.stopButton.setObjectName(u"stopButton")

        self.horizontalLayout_3.addWidget(self.stopButton)

        self.exportButton = QPushButton(self.groupBox_11)
        self.exportButton.setObjectName(u"exportButton")

        self.horizontalLayout_3.addWidget(self.exportButton)


        self.verticalLayout_3.addWidget(self.groupBox_11)

        self.groupBox_10 = QGroupBox(self.groupBox_4)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.logPlainTextEdit = QPlainTextEdit(self.groupBox_10)
        self.logPlainTextEdit.setObjectName(u"logPlainTextEdit")

        self.verticalLayout_6.addWidget(self.logPlainTextEdit)


        self.verticalLayout_3.addWidget(self.groupBox_10)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 5)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 2)

        self.horizontalLayout.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_15 = QGroupBox(self.groupBox_3)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget = QWidget(self.groupBox_15)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.modeComboBox = QComboBox(self.widget)
        self.modeComboBox.addItem("")
        self.modeComboBox.addItem("")
        self.modeComboBox.setObjectName(u"modeComboBox")

        self.horizontalLayout_5.addWidget(self.modeComboBox)

        self.modeValueSpinBox = QDoubleSpinBox(self.widget)
        self.modeValueSpinBox.setObjectName(u"modeValueSpinBox")

        self.horizontalLayout_5.addWidget(self.modeValueSpinBox)


        self.verticalLayout_8.addWidget(self.widget)

        self.widget_2 = QWidget(self.groupBox_15)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.runButton = QPushButton(self.widget_2)
        self.runButton.setObjectName(u"runButton")

        self.horizontalLayout_6.addWidget(self.runButton)

        self.stopModeButton = QPushButton(self.widget_2)
        self.stopModeButton.setObjectName(u"stopModeButton")

        self.horizontalLayout_6.addWidget(self.stopModeButton)


        self.verticalLayout_8.addWidget(self.widget_2)


        self.verticalLayout_7.addWidget(self.groupBox_15)

        self.groupBox_16 = QGroupBox(self.groupBox_3)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_16)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.identificationStatusLabel = QLabel(self.groupBox_16)
        self.identificationStatusLabel.setObjectName(u"identificationStatusLabel")

        self.verticalLayout_10.addWidget(self.identificationStatusLabel)

        self.identificationProgressBar = QProgressBar(self.groupBox_16)
        self.identificationProgressBar.setObjectName(u"identificationProgressBar")
        self.identificationProgressBar.setValue(24)

        self.verticalLayout_10.addWidget(self.identificationProgressBar)


        self.verticalLayout_7.addWidget(self.groupBox_16)

        self.groupBox_17 = QGroupBox(self.groupBox_3)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.formLayout_4 = QFormLayout(self.groupBox_17)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_15 = QLabel(self.groupBox_17)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_15)

        self.label_16 = QLabel(self.groupBox_17)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_16)

        self.label_20 = QLabel(self.groupBox_17)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_20)

        self.rsLineEdit = QLineEdit(self.groupBox_17)
        self.rsLineEdit.setObjectName(u"rsLineEdit")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.rsLineEdit)

        self.ldLineEdit = QLineEdit(self.groupBox_17)
        self.ldLineEdit.setObjectName(u"ldLineEdit")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.ldLineEdit)

        self.lqLineEdit = QLineEdit(self.groupBox_17)
        self.lqLineEdit.setObjectName(u"lqLineEdit")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lqLineEdit)


        self.verticalLayout_7.addWidget(self.groupBox_17)

        self.groupBox_14 = QGroupBox(self.groupBox_3)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_14)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.startIdentificationButton = QPushButton(self.groupBox_14)
        self.startIdentificationButton.setObjectName(u"startIdentificationButton")

        self.horizontalLayout_4.addWidget(self.startIdentificationButton)

        self.stopIdentificationButton = QPushButton(self.groupBox_14)
        self.stopIdentificationButton.setObjectName(u"stopIdentificationButton")

        self.horizontalLayout_4.addWidget(self.stopIdentificationButton)


        self.verticalLayout_7.addWidget(self.groupBox_14)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.applyParametersButton = QPushButton(self.groupBox_3)
        self.applyParametersButton.setObjectName(u"applyParametersButton")

        self.verticalLayout_9.addWidget(self.applyParametersButton)


        self.verticalLayout_7.addLayout(self.verticalLayout_9)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 4)

        self.verticalLayout.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Main Area", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Inverter Input", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"DC Voltage", None))
        self.dcVoltageSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Current Limit (Peak)", None))
        self.currentLimitPeakSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" A", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Speed Limit", None))
        self.speedLimitSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" rpm", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pole Pairs (PP)", None))
        self.polePairsSpinBox.setSuffix("")
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Inverter Output", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"d-axis current ref.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"q-axis current ref.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Current Kp", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Current Ki", None))
        self.dAxisCurrentRefSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" A", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Protection Settings ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Overcurrent Protection", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Overvoltage Protection", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Undervoltage Protection", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Temperature Limit", None))
        self.overcurrentProtectionSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" A", None))
        self.undervoltageProtectionSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.overvoltageProtectionSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.temperatureLimitSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" \u03a9", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Actions", None))
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.defaultsButton.setText(QCoreApplication.translate("MainWindow", u"Deafaults", None))
        self.disconnectButton.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Monitoring", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Signals", None))
        self.signal1ComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Signal 1", None))
        self.signal1ComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"DC Bus Voltage (V)", None))
        self.signal1ComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"d-axis Current (A)", None))
        self.signal1ComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"q-axis Current (A)", None))
        self.signal1ComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Phase A Current (A)", None))
        self.signal1ComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Phase B Current (A)", None))
        self.signal1ComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Phase C Current (A)", None))
        self.signal1ComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Temperature (\u00baC)", None))
        self.signal1ComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Duty Cycle (%)", None))

        self.signal2ComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Signal 2", None))
        self.signal2ComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"DC Bus Voltage (V)", None))
        self.signal2ComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"d-axis Current (A)", None))
        self.signal2ComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"q-axis Current (A)", None))
        self.signal2ComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Phase A Current (A)", None))
        self.signal2ComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Phase B Current (A)", None))
        self.signal2ComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Phase C Current (A)", None))
        self.signal2ComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Temperature (\u00baC)", None))
        self.signal2ComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Duty Cycle (%)", None))

        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Plot Area", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Stream Control", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start ", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"Export ", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Log", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Identification Setup", None))
        self.modeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Torque", None))
        self.modeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Speed", None))

        self.runButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.stopModeButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Identification Status", None))
        self.identificationStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Running...", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Estimated Parameters", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Rs", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Ld", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Lq", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Actions", None))
        self.startIdentificationButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stopIdentificationButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.applyParametersButton.setText(QCoreApplication.translate("MainWindow", u"Apply Parameters", None))
    # retranslateUi

