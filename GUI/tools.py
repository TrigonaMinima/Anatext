# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'extras/tools.ui'
#
# Created: Wed Jul 23 03:27:25 2014
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

class Ui_ToolsAdd(object):
    def setupUi(self, ToolsAdd):
        ToolsAdd.setObjectName(_fromUtf8("ToolsAdd"))
        ToolsAdd.resize(591, 448)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(ToolsAdd)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ToolsCloseButton = QtGui.QPushButton(ToolsAdd)
        self.ToolsCloseButton.setObjectName(_fromUtf8("ToolsCloseButton"))
        self.horizontalLayout_2.addWidget(self.ToolsCloseButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.ToolTabs = QtGui.QTabWidget(ToolsAdd)
        self.ToolTabs.setObjectName(_fromUtf8("ToolTabs"))
        self.Columns = QtGui.QWidget()
        self.Columns.setMinimumSize(QtCore.QSize(565, 0))
        self.Columns.setMaximumSize(QtCore.QSize(565, 360))
        self.Columns.setObjectName(_fromUtf8("Columns"))
        self.formLayout = QtGui.QFormLayout(self.Columns)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.CloumnName = QtGui.QLabel(self.Columns)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CloumnName.setFont(font)
        self.CloumnName.setObjectName(_fromUtf8("CloumnName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.CloumnName)
        self.ColumnNumber = QtGui.QLabel(self.Columns)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ColumnNumber.setFont(font)
        self.ColumnNumber.setObjectName(_fromUtf8("ColumnNumber"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.ColumnNumber)
        self.CustomerName = QtGui.QLabel(self.Columns)
        self.CustomerName.setObjectName(_fromUtf8("CustomerName"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.CustomerName)
        self.CustomerNameEdit = QtGui.QLineEdit(self.Columns)
        self.CustomerNameEdit.setObjectName(_fromUtf8("CustomerNameEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.CustomerNameEdit)
        self.TransactionCmnt = QtGui.QLabel(self.Columns)
        self.TransactionCmnt.setObjectName(_fromUtf8("TransactionCmnt"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.TransactionCmnt)
        self.TransactionCmntEdit = QtGui.QLineEdit(self.Columns)
        self.TransactionCmntEdit.setObjectName(_fromUtf8("TransactionCmntEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.TransactionCmntEdit)
        self.AccNum = QtGui.QLabel(self.Columns)
        self.AccNum.setObjectName(_fromUtf8("AccNum"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.AccNum)
        self.AccNumEdit = QtGui.QLineEdit(self.Columns)
        self.AccNumEdit.setObjectName(_fromUtf8("AccNumEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.AccNumEdit)
        self.CreditAmount = QtGui.QLabel(self.Columns)
        self.CreditAmount.setObjectName(_fromUtf8("CreditAmount"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.CreditAmount)
        self.CreditAmountEdit = QtGui.QLineEdit(self.Columns)
        self.CreditAmountEdit.setObjectName(_fromUtf8("CreditAmountEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.CreditAmountEdit)
        self.DebitAmount = QtGui.QLabel(self.Columns)
        self.DebitAmount.setObjectName(_fromUtf8("DebitAmount"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.DebitAmount)
        self.DebitAmountEdit = QtGui.QLineEdit(self.Columns)
        self.DebitAmountEdit.setObjectName(_fromUtf8("DebitAmountEdit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.DebitAmountEdit)
        self.ToolTabs.addTab(self.Columns, _fromUtf8(""))
        self.SheetNames = QtGui.QWidget()
        self.SheetNames.setObjectName(_fromUtf8("SheetNames"))
        self.gridLayout_6 = QtGui.QGridLayout(self.SheetNames)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.sheetNamesLabel = QtGui.QLabel(self.SheetNames)
        self.sheetNamesLabel.setObjectName(_fromUtf8("sheetNamesLabel"))
        self.gridLayout_6.addWidget(self.sheetNamesLabel, 0, 0, 1, 1)
        self.sheetNamesDesc = QtGui.QLabel(self.SheetNames)
        self.sheetNamesDesc.setObjectName(_fromUtf8("sheetNamesDesc"))
        self.gridLayout_6.addWidget(self.sheetNamesDesc, 1, 0, 1, 1)
        self.sheets = QtGui.QPlainTextEdit(self.SheetNames)
        self.sheets.setObjectName(_fromUtf8("sheets"))
        self.gridLayout_6.addWidget(self.sheets, 2, 0, 1, 1)
        self.ToolTabs.addTab(self.SheetNames, _fromUtf8(""))
        self.Companies = QtGui.QWidget()
        self.Companies.setObjectName(_fromUtf8("Companies"))
        self.gridLayout_7 = QtGui.QGridLayout(self.Companies)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.companiesLabel = QtGui.QLabel(self.Companies)
        self.companiesLabel.setObjectName(_fromUtf8("companiesLabel"))
        self.gridLayout_7.addWidget(self.companiesLabel, 0, 0, 1, 1)
        self.companiesDesc = QtGui.QLabel(self.Companies)
        self.companiesDesc.setObjectName(_fromUtf8("companiesDesc"))
        self.gridLayout_7.addWidget(self.companiesDesc, 1, 0, 1, 1)
        self.companies_keywords = QtGui.QPlainTextEdit(self.Companies)
        self.companies_keywords.setObjectName(_fromUtf8("companies_keywords"))
        self.gridLayout_7.addWidget(self.companies_keywords, 2, 0, 1, 1)
        self.ToolTabs.addTab(self.Companies, _fromUtf8(""))
        self.Surnames = QtGui.QWidget()
        self.Surnames.setObjectName(_fromUtf8("Surnames"))
        self.gridLayout_8 = QtGui.QGridLayout(self.Surnames)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.surnamesLabel = QtGui.QLabel(self.Surnames)
        self.surnamesLabel.setObjectName(_fromUtf8("surnamesLabel"))
        self.gridLayout_8.addWidget(self.surnamesLabel, 0, 0, 1, 1)
        self.surnamesDesc = QtGui.QLabel(self.Surnames)
        self.surnamesDesc.setObjectName(_fromUtf8("surnamesDesc"))
        self.gridLayout_8.addWidget(self.surnamesDesc, 1, 0, 1, 1)
        self.surnames_new = QtGui.QPlainTextEdit(self.Surnames)
        self.surnames_new.setObjectName(_fromUtf8("surnames_new"))
        self.gridLayout_8.addWidget(self.surnames_new, 2, 0, 1, 1)
        self.ToolTabs.addTab(self.Surnames, _fromUtf8(""))
        self.Junk = QtGui.QWidget()
        self.Junk.setObjectName(_fromUtf8("Junk"))
        self.gridLayout_9 = QtGui.QGridLayout(self.Junk)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.junkLabel = QtGui.QLabel(self.Junk)
        self.junkLabel.setObjectName(_fromUtf8("junkLabel"))
        self.gridLayout_9.addWidget(self.junkLabel, 0, 0, 1, 1)
        self.junkDesc = QtGui.QLabel(self.Junk)
        self.junkDesc.setObjectName(_fromUtf8("junkDesc"))
        self.gridLayout_9.addWidget(self.junkDesc, 1, 0, 1, 1)
        self.junkDesc2 = QtGui.QLabel(self.Junk)
        self.junkDesc2.setObjectName(_fromUtf8("junkDesc2"))
        self.gridLayout_9.addWidget(self.junkDesc2, 2, 0, 1, 1)
        self.junkWords = QtGui.QPlainTextEdit(self.Junk)
        self.junkWords.setObjectName(_fromUtf8("junkWords"))
        self.gridLayout_9.addWidget(self.junkWords, 3, 0, 1, 1)
        self.ToolTabs.addTab(self.Junk, _fromUtf8(""))
        self.SpellCorrect = QtGui.QWidget()
        self.SpellCorrect.setObjectName(_fromUtf8("SpellCorrect"))
        self.gridLayout_10 = QtGui.QGridLayout(self.SpellCorrect)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.words = QtGui.QLabel(self.SpellCorrect)
        self.words.setObjectName(_fromUtf8("words"))
        self.gridLayout_10.addWidget(self.words, 0, 0, 1, 1)
        self.wordsDesc = QtGui.QLabel(self.SpellCorrect)
        self.wordsDesc.setObjectName(_fromUtf8("wordsDesc"))
        self.gridLayout_10.addWidget(self.wordsDesc, 1, 0, 1, 1)
        self.WordsNew = QtGui.QPlainTextEdit(self.SpellCorrect)
        self.WordsNew.setObjectName(_fromUtf8("WordsNew"))
        self.gridLayout_10.addWidget(self.WordsNew, 2, 0, 1, 1)
        self.ToolTabs.addTab(self.SpellCorrect, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.ToolTabs, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_4)

        self.retranslateUi(ToolsAdd)
        self.ToolTabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.ToolsCloseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ToolsAdd.close)
        QtCore.QMetaObject.connectSlotsByName(ToolsAdd)

    def retranslateUi(self, ToolsAdd):
        ToolsAdd.setWindowTitle(_translate("ToolsAdd", "Tools and Settings", None))
        self.ToolsCloseButton.setText(_translate("ToolsAdd", "Close", None))
        self.CloumnName.setText(_translate("ToolsAdd", "Column Name", None))
        self.ColumnNumber.setText(_translate("ToolsAdd", "Column Number", None))
        self.CustomerName.setText(_translate("ToolsAdd", "Customer Name :", None))
        self.CustomerNameEdit.setText(_translate("ToolsAdd", "1", None))
        self.TransactionCmnt.setText(_translate("ToolsAdd", "Transaction Comment :", None))
        self.TransactionCmntEdit.setText(_translate("ToolsAdd", "3", None))
        self.AccNum.setText(_translate("ToolsAdd", "Account Number :", None))
        self.AccNumEdit.setText(_translate("ToolsAdd", "5", None))
        self.CreditAmount.setText(_translate("ToolsAdd", "Credit Amount :", None))
        self.CreditAmountEdit.setText(_translate("ToolsAdd", "6", None))
        self.DebitAmount.setText(_translate("ToolsAdd", "Debit Amount :", None))
        self.DebitAmountEdit.setText(_translate("ToolsAdd", "7", None))
        self.ToolTabs.setTabText(self.ToolTabs.indexOf(self.Columns), _translate("ToolsAdd", "Columns", None))
        self.sheetNamesLabel.setText(_translate("ToolsAdd", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Sheet Names</span></p></body></html>", None))
        self.sheetNamesDesc.setText(_translate("ToolsAdd", "Enter coma ( \',\' ) separated sheetnames in order of your excel files.", None))
        self.ToolTabs.setTabText(self.ToolTabs.indexOf(self.SheetNames), _translate("ToolsAdd", "Sheet Names", None))
        self.companiesLabel.setText(_translate("ToolsAdd", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Company Related Terms</span></p></body></html>", None))
        self.companiesDesc.setText(_translate("ToolsAdd", "Enter coma ( \',\' ) separated keywords which are company related.", None))
        self.ToolTabs.setTabText(self.ToolTabs.indexOf(self.Companies), _translate("ToolsAdd", "Companies", None))
        self.surnamesLabel.setText(_translate("ToolsAdd", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Surnames</span></p></body></html>", None))
        self.surnamesDesc.setText(_translate("ToolsAdd", "Enter coma ( \',\' ) separated surnames.", None))
        self.ToolTabs.setTabText(self.ToolTabs.indexOf(self.Surnames), _translate("ToolsAdd", "Surnames", None))
        self.junkLabel.setText(_translate("ToolsAdd", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Junk Words</span></p></body></html>", None))
        self.junkDesc.setText(_translate("ToolsAdd", "Enter coma ( \',\' ) separated keywords you want to treat as junk, occuring", None))
        self.junkDesc2.setText(_translate("ToolsAdd", "before individual names and customer names in transaction comments.", None))
        self.ToolTabs.setTabText(self.ToolTabs.indexOf(self.Junk), _translate("ToolsAdd", "Junk", None))
        self.words.setText(_translate("ToolsAdd", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Words</span></p></body></html>", None))
        self.wordsDesc.setText(_translate("ToolsAdd", "Enter coma ( \',\' ) separated keywords you want to spell correct.", None))
        self.ToolTabs.setTabText(self.ToolTabs.indexOf(self.SpellCorrect), _translate("ToolsAdd", "Spell Correct", None))

