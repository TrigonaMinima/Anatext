from PyQt4 import QtCore, QtGui

import sys
from about import Ui_About


class StartQT4(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)

        self.ui_about = Ui_About()
        self.ui_about.setupUi(self)



        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
