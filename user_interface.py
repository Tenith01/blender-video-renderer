from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QFileDialog, QLabel
import Renderer
import time

loader = QUiLoader()
blenderFilePath = ""


class UserInterface(QtCore.QObject):  # An object wrapping around our ui
    def __init__(self):
        super().__init__()
        self.ui = loader.load("ImageRenderer.ui", None)
        self.ui.setWindowTitle("Blender Image Renderer")
        self.ui.AddButton.clicked.connect(self.OpenFileLocaation)
        self.ui.AddButton.clicked.connect(self.ItemChangeInListWiget)

        self.ui.RenderButton.clicked.connect(self.StartImageRenderer)

        self.ui.RemoveButton.clicked.connect(self.RemoveSelectedItems)
        self.ui.RemoveButton.clicked.connect(self.ItemChangeInListWiget)

        self.ui.ClearButton.clicked.connect(self.RemoveAllItems)
        self.ui.ClearButton.clicked.connect(self.ItemChangeInListWiget)

        # self.ui.listWidget.currentItemChanged.connect(self.ItemChangeInListWiget)
        # self.ui.listWidget.itemEntered.connect(self.ItemChangeInListWiget)
        # self.ui.listWidget.itemChanged.connect(self.ItemChangeInListWiget)

    def show(self):
        self.ui.show()
        self.ItemChangeInListWiget()

    def OpenFileLocaation(self):
        filenames, _ = QFileDialog.getOpenFileNames(filter="3D (*.blend)")
        for filename in filenames:
            self.ui.listWidget.addItem(filename)

    def RemoveSelectedItems(self):
        for item in self.ui.listWidget.selectedItems():
            self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

    def RemoveAllItems(self):
        self.ui.listWidget.clear()

    def StartImageRenderer(self):
        max_value = self.ui.listWidget.count()
        value = 0;

        self.ui.progressBar_2.setValue(0)
        self.ui.progressBar.setValue(0)

        for i in range(self.ui.listWidget.count()):

            item = self.ui.listWidget.item(i)
            print(item.text())

            BLENDER_FILE = str(item.text())
            OUTPUT_IMAGE = str(item.text().lstrip('.blend')) + " "

            self.ui.RenderStatLabel_2.setText("Start...")
            for num in Renderer.ImageRenderer(BLENDER_FILE, OUTPUT_IMAGE):
                # num = num.split(',').tolist()
                # print("rendering start")
                self.ui.RenderStatLabel_2.setText(num[0])
                self.ui.progressBar_2.setValue(num[2])
                print(num[2])

            statFrame = 0;
            self.ui.RenderStatLabel_2.setText("complete.")
            self.ui.progressBar_2.setValue(100)

            value += 1
            progressbarValue = int(int(value) / int(max_value) * 100)
            print(progressbarValue)
            self.ui.progressBar.setValue(progressbarValue)
            self.ui.RenderStatLabel.setText("Copleted " + str(value) +"/" + str(max_value) + " :")


    def ItemChangeInListWiget(self):
        max_value = str(self.ui.listWidget.count())
        self.ui.RenderStatLabel.setText("Copleted 0/" + max_value + " :")
