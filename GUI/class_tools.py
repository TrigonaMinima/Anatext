from PyQt4 import QtCore, QtGui

from tools import Ui_ToolsAdd


class StartTools(QtGui.QDialog):

    def __init__(self, parent=None):
        super(StartTools, self).__init__(parent)

        self.ui_tools = Ui_ToolsAdd()
        self.ui_tools.setupUi(self)

        self.connect_slots()

    def connect_slots(self):
        self.ui_tools.ToolsCloseButton.clicked.connect(
            self.get_data)

    def get_data(self):
        self.columns()
        self.sheets()
        self.companies()
        self.surnames()
        self.junk()
        self.corrections()

    def columns(self):
        cus_name = eval(unicode(self.ui_tools.CustomerNameEdit.text()))
        comment = eval(unicode(self.ui_tools.TransactionCmntEdit.text()))
        account = eval(unicode(self.ui_tools.AccNumEdit.text()))
        credit = eval(unicode(self.ui_tools.CreditAmountEdit.text()))
        debit = eval(unicode(self.ui_tools.DebitAmountEdit.text()))
        print cus_name, comment, account, credit, debit
        # print type(comment)

    def sheets(self):
        names = self.ui_tools.sheets.toPlainText()
        names = [str(name).strip() for name in names.split(',')]
        # names.clear()
        print names

    def companies(self):
        comps = unicode(self.ui_tools.companies_keywords.toPlainText())
        comps = [str(comp).strip() for comp in comps.split(',')]
        print comps

    def surnames(self):
        snames = unicode(self.ui_tools.surnames_new.toPlainText())
        snames = [str(sname).strip() for sname in snames.split(',')]
        print snames

    def junk(self):
        junkings = unicode(self.ui_tools.junkWords.toPlainText())
        junkings = [str(junking).strip() for junking in junkings.split(',')]
        print junkings

    def corrections(self):
        corrs = unicode(self.ui_tools.WordsNew.toPlainText())
        corrs = [str(corr).strip() for corr in corrs.split(',')]
        print corrs
