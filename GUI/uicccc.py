import sys
sys.dont_write_bytecode = True

from PyQt4 import QtCore, QtGui

from main import Ui_MainWindow
from class_about import StartAbout
from class_tools import StartTools


class StartQT4(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui_main_window = Ui_MainWindow()
        self.ui_main_window.setupUi(self)

        self.connect_slots()

        self.ui_main_window.cancel_button.setEnabled(False)
        self.ui_main_window.start_button.setEnabled(False)

    def connect_slots(self):
        # Signals and Slots
        self.ui_main_window.actionOpenFile.triggered.connect(self.file_dialog)
        self.ui_main_window.actionAbout_AnaText.triggered.connect(
            self.about_dialog)
        self.ui_main_window.AddSettings.triggered.connect(
            self.tools_dialog)

    def file_dialog(self):
        # fd = QtGui.QFileDialog(self)
        # self.files = fd.getOpenFileNames(
        #     self, 'Open file', '', "Excel Files (*.xls *.xlsx)")
        # print self.files
        files = []
        for path in QtGui.QFileDialog.getOpenFileNames(self, 'Open Files', '', "Excel Files (*.xls *.xlsx)"):
            print path
            if path not in files:
                files.append(path)
        print files

    def about_dialog(self):
        about_box = StartAbout(self)
        about_box.show()

    def tools_dialog(self):
        tools_box = StartTools(self)
        tools_box.show()

    def enable_button(self, ui, button):
        self.ui.button.setEnabled(True)

    # Asks if user really wants to exit.
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
