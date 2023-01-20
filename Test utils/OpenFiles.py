from PySide6.QtWidgets import QApplication, QFileDialog

app = QApplication()
filenames, _ = QFileDialog.getOpenFileNames()
file_name_list = list(filenames)
print(file_name_list)
app.exec_()