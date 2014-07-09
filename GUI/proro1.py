import sys
from PyQt4 import QtGui, QtCore, uic


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):

        

        # self.text = 'AnaText'
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        about = QtGui.QAction(QtGui.QIcon('about.png'), 'About', self)
        # about.setShortcut('Ctrl+O')
        about.setStatusTip('About AnaText')
        about.triggered.connect(self.paintEvent)

        documentation = QtGui.QAction(QtGui.QIcon('doc.png'), 'Documentation', self)
        # documentation.setShortcut('Ctrl+O')
        documentation.setStatusTip('Documentation')
        # documentation.triggered.connect(self.showDialog)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(exitAction)

        fileMenu = menubar.addMenu('&View')

        fileMenu = menubar.addMenu('&Tools')

        fileMenu = menubar.addMenu('&Help')
        fileMenu.addAction(documentation)
        fileMenu.addAction(about)

        self.resize(700, 400)
        self.center()
        
        self.setWindowTitle('AnaText v1.0')
        self.show()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def showDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
                '/home')



def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()