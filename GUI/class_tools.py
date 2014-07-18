from PyQt4 import QtCore, QtGui

from tools import Ui_ToolsAdd

class StartTools(QtGui.QDialog):

    def __init__(self, parent=None):
        super(StartTools, self).__init__(parent)

        self.ui_tools = Ui_ToolsAdd()
        self.ui_tools.setupUi(self)
