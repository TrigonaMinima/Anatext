import sys
from PyQt4 import QtCore, QtGui
from main import Ui_MainWindow
from about import Ui_About


class StartQT4(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # self.ui_about = Ui_About()
        # self.ui_about.setupUi(self)

        self.ui_main_window = Ui_MainWindow()
        self.ui_main_window.setupUi(self)

        # self.setCentralWidget(self)

        self.connect_slots()

        # QtCore.QObject.connect(self.ui_main_window.actionAbout_AnaText, QtCore.SIGNAL("triggered()"), self.about_show)
        self.ui_main_window.cancel_button.setEnabled(False)
        self.ui_main_window.start_button.setEnabled(False)

    def connect_slots(self):
        # Signals and Slots
        self.ui_main_window.actionOpen.triggered.connect(self.file_dialog)
        self.ui_main_window.actionAbout_AnaText.triggered.connect(
            self.about_dialog)

    def file_dialog(self):

        fd = QtGui.QFileDialog(self)
        self.files = fd.getOpenFileNamesAndFilter(
            self, 'Open file', '/home', "Excel Files (*.xls *.xlsx)")

    def about_dialog(self):
        ui_about = Ui_About()
        ui_about.setupUi()
        # self.ui_about.retranslateUi(self)

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
