# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImageRenderer.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QProgressBar, QPushButton,
    QSizePolicy, QWidget)
# import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(771, 440)
        Form.setMinimumSize(QSize(771, 440))
        Form.setMaximumSize(QSize(771, 440))
        Form.setSizeIncrement(QSize(771, 440))
        icon = QIcon()
        icon.addFile(u":/Icons/Screenshot_from_2023-01-14_05-34-41-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(0.930000000000000)
        Form.setStyleSheet(u"QWidget {\n"
"    background-color: #333333;\n"
"    color: rgb(136, 138, 133);\n"
"    font-family: \"Open Sans\", sans-serif;\n"
"    font-size: 14px;\n"
"}")
        self.RenderButton = QPushButton(Form)
        self.RenderButton.setObjectName(u"RenderButton")
        self.RenderButton.setGeometry(QRect(610, 270, 121, 31))
        self.RenderButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #4d91ea;\n"
"    color: #ffffff;\n"
"    padding: 10px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font-family: \"Open Sans\", sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3f7ab7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3f7ab7;\n"
"}")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 151, 16))
        self.label.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #333333;\n"
"}")
        self.AddButton = QPushButton(Form)
        self.AddButton.setObjectName(u"AddButton")
        self.AddButton.setGeometry(QRect(700, 170, 41, 31))
        font = QFont()
        font.setFamilies([u"Open Sans"])
        font.setBold(True)
        font.setItalic(True)
        self.AddButton.setFont(font)
        self.AddButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #4d91ea;\n"
"    color: #ffffff;\n"
"    padding: 10px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font-family: \"Open Sans\", sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3f7ab7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3f7ab7;\n"
"}")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 190, 151, 16))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #333333;\n"
"}")
        self.SelectedFrameTest = QLineEdit(Form)
        self.SelectedFrameTest.setObjectName(u"SelectedFrameTest")
        self.SelectedFrameTest.setGeometry(QRect(30, 210, 161, 31))
        self.SelectedFrameTest.setStyleSheet(u"QLineEdit {\n"
"    background-color: #444444;\n"
"    color: #ffffff;\n"
"    border: 1px solid rgb(85, 87, 83);\n"
"    padding: 5px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4d91ea;\n"
"}")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 190, 101, 16))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #333333;\n"
"}")
        self.ExportTypeSelector = QComboBox(Form)
        self.ExportTypeSelector.addItem("")
        self.ExportTypeSelector.addItem("")
        self.ExportTypeSelector.addItem("")
        self.ExportTypeSelector.addItem("")
        self.ExportTypeSelector.addItem("")
        self.ExportTypeSelector.addItem("")
        self.ExportTypeSelector.addItem("")
        self.ExportTypeSelector.addItem("")
        self.ExportTypeSelector.addItem("")
        self.ExportTypeSelector.addItem("")
        self.ExportTypeSelector.setObjectName(u"ExportTypeSelector")
        self.ExportTypeSelector.setGeometry(QRect(210, 210, 111, 31))
        self.ExportTypeSelector.setStyleSheet(u"QComboBox {\n"
"    background-color: #444444;\n"
"    color: #ffffff;\n"
"    border: 1px solid rgb(85, 87, 83);\n"
"    padding: 6px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(down_arrow.png);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #4d91ea;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #4d91ea;\n"
"}")
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 320, 711, 23))
        font1 = QFont()
        font1.setFamilies([u"Open Sans"])
        self.progressBar.setFont(font1)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"    color: rgb(238, 238, 236);\n"
"\n"
"}\n"
"\n"
"QProgressBar:hover {\n"
"    background-color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.progressBar.setValue(0)
        self.RenderStatLabel = QLabel(Form)
        self.RenderStatLabel.setObjectName(u"RenderStatLabel")
        self.RenderStatLabel.setGeometry(QRect(30, 300, 121, 16))
        self.RenderStatLabel.setStyleSheet(u"QLabel {\n"
"    color: rgb(136, 138, 133);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #333333;\n"
"}")
        self.progressBar_2 = QProgressBar(Form)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(30, 370, 711, 23))
        self.progressBar_2.setStyleSheet(u"QProgressBar{\n"
"    color: rgb(238, 238, 236);\n"
"\n"
"}\n"
"\n"
"QProgressBar:hover {\n"
"    background-color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.progressBar_2.setValue(0)
        self.RenderStatLabel_2 = QLabel(Form)
        self.RenderStatLabel_2.setObjectName(u"RenderStatLabel_2")
        self.RenderStatLabel_2.setGeometry(QRect(30, 350, 101, 16))
        self.RenderStatLabel_2.setStyleSheet(u"QLabel {\n"
"    color: rgb(136, 138, 133);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #333333;\n"
"}")
        self.RenderButton_2 = QPushButton(Form)
        self.RenderButton_2.setObjectName(u"RenderButton_2")
        self.RenderButton_2.setGeometry(QRect(480, 270, 121, 31))
        self.RenderButton_2.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(213, 85, 85);\n"
"    color: #ffffff;\n"
"    padding: 10px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font-family: \"Open Sans\", sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #rgb(150 85, 85);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(100, 50, 40);\n"
"}")
        self.listWidget = QListWidget(Form)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 50, 711, 111))
        self.listWidget.setStyleSheet(u"QWidget {\n"
"	background-color: #333333;\n"
"    color: #ffffff;\n"
"    border: 1px solid rgb(85, 87, 83);\n"
"    padding: 5px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"\n"
"QWidget:hover {\n"
"    background-color:#333330;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QWidget:pressed {\n"
"    background-color: #333333;\n"
"    color: #ffffff;\n"
"}")
        self.RemoveButton = QPushButton(Form)
        self.RemoveButton.setObjectName(u"RemoveButton")
        self.RemoveButton.setGeometry(QRect(650, 170, 41, 31))
        font2 = QFont()
        font2.setFamilies([u"Open Sans"])
        font2.setBold(True)
        self.RemoveButton.setFont(font2)
        self.RemoveButton.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(213, 85, 85);\n"
"    color: #ffffff;\n"
"    padding: 10px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font-family: \"Open Sans\", sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #rgb(150 85, 85);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(100, 50, 40);\n"
"}")
        self.ClearButton = QPushButton(Form)
        self.ClearButton.setObjectName(u"ClearButton")
        self.ClearButton.setGeometry(QRect(570, 170, 71, 31))
        self.ClearButton.setFont(font2)
        self.ClearButton.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(213, 85, 85);\n"
"    color: #ffffff;\n"
"    padding: 10px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font-family: \"Open Sans\", sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #rgb(150 85, 85);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(100, 50, 40);\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.RenderButton.setText(QCoreApplication.translate("Form", u"Render", None))
        self.label.setText(QCoreApplication.translate("Form", u"Blender File's Location : ", None))
        self.AddButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Select Frame :", None))
        self.SelectedFrameTest.setText(QCoreApplication.translate("Form", u"200", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Output Type :", None))
        self.ExportTypeSelector.setItemText(0, QCoreApplication.translate("Form", u"PNG", None))
        self.ExportTypeSelector.setItemText(1, QCoreApplication.translate("Form", u"JPEG", None))
        self.ExportTypeSelector.setItemText(2, QCoreApplication.translate("Form", u"BMP", None))
        self.ExportTypeSelector.setItemText(3, QCoreApplication.translate("Form", u"Iris", None))
        self.ExportTypeSelector.setItemText(4, QCoreApplication.translate("Form", u"Targa", None))
        self.ExportTypeSelector.setItemText(5, QCoreApplication.translate("Form", u"Cineon", None))
        self.ExportTypeSelector.setItemText(6, QCoreApplication.translate("Form", u"DPX", None))
        self.ExportTypeSelector.setItemText(7, QCoreApplication.translate("Form", u"OpenEXR", None))
        self.ExportTypeSelector.setItemText(8, QCoreApplication.translate("Form", u"TIFF", None))
        self.ExportTypeSelector.setItemText(9, QCoreApplication.translate("Form", u"Webp", None))

        self.RenderStatLabel.setText(QCoreApplication.translate("Form", u"Copleted 12/40 :", None))
        self.RenderStatLabel_2.setText(QCoreApplication.translate("Form", u"Rendering......", None))
        self.RenderButton_2.setText(QCoreApplication.translate("Form", u"Stop", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"'/media/tenith/2466245A66242ECC/HIFK PNG/HIFK2 Silver/21.blend'", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"'/media/tenith/2466245A66242ECC/HIFK PNG/HIFK2 Silver/21.blend'", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.RemoveButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.ClearButton.setText(QCoreApplication.translate("Form", u"Clear", None))
    # retranslateUi

