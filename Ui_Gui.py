# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)
import app_icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u":/icon/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(200, 330))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_00 = QCheckBox(self.groupBox)
        self.checkBox_00.setObjectName(u"checkBox_00")
        sizePolicy.setHeightForWidth(self.checkBox_00.sizePolicy().hasHeightForWidth())
        self.checkBox_00.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.checkBox_00.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_00)

        self.checkBox_01 = QCheckBox(self.groupBox)
        self.checkBox_01.setObjectName(u"checkBox_01")
        sizePolicy.setHeightForWidth(self.checkBox_01.sizePolicy().hasHeightForWidth())
        self.checkBox_01.setSizePolicy(sizePolicy)
        self.checkBox_01.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_01)

        self.checkBox_02 = QCheckBox(self.groupBox)
        self.checkBox_02.setObjectName(u"checkBox_02")
        sizePolicy.setHeightForWidth(self.checkBox_02.sizePolicy().hasHeightForWidth())
        self.checkBox_02.setSizePolicy(sizePolicy)
        self.checkBox_02.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_02)

        self.checkBox_03 = QCheckBox(self.groupBox)
        self.checkBox_03.setObjectName(u"checkBox_03")
        sizePolicy.setHeightForWidth(self.checkBox_03.sizePolicy().hasHeightForWidth())
        self.checkBox_03.setSizePolicy(sizePolicy)
        self.checkBox_03.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_03)

        self.checkBox_04 = QCheckBox(self.groupBox)
        self.checkBox_04.setObjectName(u"checkBox_04")
        sizePolicy.setHeightForWidth(self.checkBox_04.sizePolicy().hasHeightForWidth())
        self.checkBox_04.setSizePolicy(sizePolicy)
        self.checkBox_04.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_04)

        self.checkBox_05 = QCheckBox(self.groupBox)
        self.checkBox_05.setObjectName(u"checkBox_05")
        sizePolicy.setHeightForWidth(self.checkBox_05.sizePolicy().hasHeightForWidth())
        self.checkBox_05.setSizePolicy(sizePolicy)
        self.checkBox_05.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_05)

        self.checkBox_06 = QCheckBox(self.groupBox)
        self.checkBox_06.setObjectName(u"checkBox_06")
        sizePolicy.setHeightForWidth(self.checkBox_06.sizePolicy().hasHeightForWidth())
        self.checkBox_06.setSizePolicy(sizePolicy)
        self.checkBox_06.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_06)

        self.checkBox_07 = QCheckBox(self.groupBox)
        self.checkBox_07.setObjectName(u"checkBox_07")
        sizePolicy.setHeightForWidth(self.checkBox_07.sizePolicy().hasHeightForWidth())
        self.checkBox_07.setSizePolicy(sizePolicy)
        self.checkBox_07.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_07)

        self.checkBox_08 = QCheckBox(self.groupBox)
        self.checkBox_08.setObjectName(u"checkBox_08")
        sizePolicy.setHeightForWidth(self.checkBox_08.sizePolicy().hasHeightForWidth())
        self.checkBox_08.setSizePolicy(sizePolicy)
        self.checkBox_08.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_08)

        self.checkBox_09 = QCheckBox(self.groupBox)
        self.checkBox_09.setObjectName(u"checkBox_09")
        sizePolicy.setHeightForWidth(self.checkBox_09.sizePolicy().hasHeightForWidth())
        self.checkBox_09.setSizePolicy(sizePolicy)
        self.checkBox_09.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_09)

        self.checkBox_10 = QCheckBox(self.groupBox)
        self.checkBox_10.setObjectName(u"checkBox_10")
        sizePolicy.setHeightForWidth(self.checkBox_10.sizePolicy().hasHeightForWidth())
        self.checkBox_10.setSizePolicy(sizePolicy)
        self.checkBox_10.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_10)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Button_config = QPushButton(self.centralwidget)
        self.Button_config.setObjectName(u"Button_config")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Button_config.sizePolicy().hasHeightForWidth())
        self.Button_config.setSizePolicy(sizePolicy2)
        self.Button_config.setFont(font)

        self.verticalLayout_2.addWidget(self.Button_config)

        self.Button_start = QPushButton(self.centralwidget)
        self.Button_start.setObjectName(u"Button_start")
        sizePolicy2.setHeightForWidth(self.Button_start.sizePolicy().hasHeightForWidth())
        self.Button_start.setSizePolicy(sizePolicy2)
        self.Button_start.setFont(font)

        self.verticalLayout_2.addWidget(self.Button_start)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.checkBox_mode = QCheckBox(self.centralwidget)
        self.checkBox_mode.setObjectName(u"checkBox_mode")
        sizePolicy2.setHeightForWidth(self.checkBox_mode.sizePolicy().hasHeightForWidth())
        self.checkBox_mode.setSizePolicy(sizePolicy2)
        self.checkBox_mode.setFont(font)
        self.checkBox_mode.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox_mode.setChecked(True)

        self.verticalLayout_4.addWidget(self.checkBox_mode)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setItalic(True)
        font1.setUnderline(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:rgb(98, 98, 98)")

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.label_key = QLabel(self.centralwidget)
        self.label_key.setObjectName(u"label_key")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_key.sizePolicy().hasHeightForWidth())
        self.label_key.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(16)
        font2.setStyleStrategy(QFont.PreferDefault)
        font2.setHintingPreference(QFont.PreferDefaultHinting)
        self.label_key.setFont(font2)
        self.label_key.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_key.setTextFormat(Qt.TextFormat.AutoText)
        self.label_key.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_key.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_key)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label_word = QLabel(self.centralwidget)
        self.label_word.setObjectName(u"label_word")
        sizePolicy3.setHeightForWidth(self.label_word.sizePolicy().hasHeightForWidth())
        self.label_word.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(30)
        self.label_word.setFont(font3)
        self.label_word.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_word.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_word)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy4)
        self.lineEdit.setBaseSize(QSize(0, 0))
        self.lineEdit.setFont(font3)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineEdit)

        self.verticalSpacer_3 = QSpacerItem(20, 208, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 3)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 5)
        self.verticalLayout_3.setStretch(4, 1)
        self.verticalLayout_3.setStretch(5, 1)
        self.verticalLayout_3.setStretch(6, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u53cc\u62fc\u7ec3\u4e60\u8f6f\u4ef6", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.checkBox_00.setText(QCoreApplication.translate("MainWindow", u"\u96f6\uff1aZh/Ch/Sh", None))
        self.checkBox_01.setText(QCoreApplication.translate("MainWindow", u"\u4e00\uff1aan/ian/ao", None))
        self.checkBox_02.setText(QCoreApplication.translate("MainWindow", u"\u4e8c\uff1aing/ang/ui", None))
        self.checkBox_03.setText(QCoreApplication.translate("MainWindow", u"\u4e09\uff1aai/eng/ong", None))
        self.checkBox_04.setText(QCoreApplication.translate("MainWindow", u"\u56db\uff1aiao/uo/ou", None))
        self.checkBox_05.setText(QCoreApplication.translate("MainWindow", u"\u4e94\uff1ain/en/ie", None))
        self.checkBox_06.setText(QCoreApplication.translate("MainWindow", u"\u516d\uff1auan/iang/iu", None))
        self.checkBox_07.setText(QCoreApplication.translate("MainWindow", u"\u4e03\uff1aei/un/\u00fcn/uang", None))
        self.checkBox_08.setText(QCoreApplication.translate("MainWindow", u"\u516b\uff1aia/\u00fcan/ue/\u00fce", None))
        self.checkBox_09.setText(QCoreApplication.translate("MainWindow", u"\u4e5d\uff1aua/iong/uai", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"\u5341\uff1a\u81ea\u5b9a\u4e49", None))
        self.Button_config.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u6570\u636e", None))
        self.Button_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.checkBox_mode.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e\u63d0\u793a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"by: scnf", None))
        self.label_key.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u793a\u6309\u952e", None))
        self.label_word.setText(QCoreApplication.translate("MainWindow", u"\u8bcd", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
    # retranslateUi

