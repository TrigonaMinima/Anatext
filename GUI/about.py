# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'extras/about.ui'
#
# Created: Thu Jul 10 20:29:52 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(343, 152)
        self.label = QtGui.QLabel(About)
        self.label.setGeometry(QtCore.QRect(40, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(About)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(About)
        self.label_3.setGeometry(QtCore.QRect(110, 60, 58, 15))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(About)
        self.label_4.setGeometry(QtCore.QRect(40, 80, 301, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(About)
        self.pushButton.setGeometry(QtCore.QRect(120, 120, 87, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(About)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), About.close)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_translate("About", "About AnaText", None))
        self.label.setText(_translate("About", "AnaText", None))
        self.label_2.setText(_translate("About", "Version", None))
        self.label_3.setText(_translate("About", "1.0.0", None))
        self.label_4.setText(_translate("About", "AnaText is a data analytics tool.", None))
        self.pushButton.setText(_translate("About", "Close", None))

