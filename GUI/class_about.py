from PyQt4 import QtCore, QtGui

from about import Ui_About

class StartAbout(QtGui.QDialog):

    def __init__(self, parent=None):
        super(StartAbout, self).__init__(parent)

        self.ui_about = Ui_About()
        self.ui_about.setupUi(self)
