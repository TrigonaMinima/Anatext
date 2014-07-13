# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'extras/columns.ui'
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

class Ui_Columns(object):
    def setupUi(self, Columns):
        Columns.setObjectName(_fromUtf8("Columns"))
        Columns.resize(400, 297)
        self.buttonBox = QtGui.QDialogButtonBox(Columns)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit = QtGui.QLineEdit(Columns)
        self.lineEdit.setGeometry(QtCore.QRect(230, 60, 113, 25))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Columns)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 90, 113, 25))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Columns)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 120, 113, 25))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Columns)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 150, 113, 25))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Columns)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 180, 113, 25))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label = QtGui.QLabel(Columns)
        self.label.setGeometry(QtCore.QRect(50, 60, 141, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Columns)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 141, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Columns)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 141, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Columns)
        self.label_4.setGeometry(QtCore.QRect(50, 150, 141, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Columns)
        self.label_5.setGeometry(QtCore.QRect(50, 180, 141, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Columns)
        self.label_6.setGeometry(QtCore.QRect(50, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Columns)
        self.label_7.setGeometry(QtCore.QRect(230, 30, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(Columns)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Columns.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Columns.reject)
        QtCore.QMetaObject.connectSlotsByName(Columns)

    def retranslateUi(self, Columns):
        Columns.setWindowTitle(_translate("Columns", "Columns", None))
        self.lineEdit.setText(_translate("Columns", "1", None))
        self.lineEdit_2.setText(_translate("Columns", "3", None))
        self.lineEdit_3.setText(_translate("Columns", "5", None))
        self.lineEdit_4.setText(_translate("Columns", "6", None))
        self.lineEdit_5.setText(_translate("Columns", "7", None))
        self.label.setText(_translate("Columns", "Company Name", None))
        self.label_2.setText(_translate("Columns", "Transaction Comment", None))
        self.label_3.setText(_translate("Columns", "Account Number", None))
        self.label_4.setText(_translate("Columns", "Credit Amount", None))
        self.label_5.setText(_translate("Columns", "Debit Amount", None))
        self.label_6.setText(_translate("Columns", "Column Name", None))
        self.label_7.setText(_translate("Columns", "Column Number", None))

