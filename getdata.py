import commons
import collections


def create(sheet, curr_row, mdata, cdata, cols):
    """
    It takes in the 'sheet' to read from and other lists and dictionaries and
    fills them from the values in the sheet at the 'curr_row'.
    It returns nothing.
    """

    temp = 0
    # Reads company name from the column 0th of 'curr_row' and appends it to
    # the list if it is distinct. Also, makes a list of words named
    # 'lavenstein_true_words' to be used to correct the spellings of these
    # companies.
    value1 = sheet.cell_value(curr_row, cols.company_col)
    value1 = value1.replace('.', ' ')
    value1 = value1.replace('  ', ' ')
    value1 = value1.strip()
    # todo: If some values have to be hard coded then make a functionality for that
    # if value1 == 'SARADHA':
    #     value1 = 'Saradha Realty India Ltd'
    if value1 not in mdata.companies:
        mdata.companies.append(value1)
        mdata.comp_acc_dict[value1] = []
        for i in commons.stripping(value1.lower(), cdata).split():
            if i not in mdata.lavenstein_true_words:
                mdata.lavenstein_true_words.append(i)

    # Reads account number from the 2nd column and appends it to the list
    # distinctly. Also appends it to the dictionary for orgs and their
    # corresponding account numbers. Makes a new dictionary key with reduced
    # digits (here 5 digits) with a value of full account number. Factor can
    # be changed by changing the value of 'reduced_digits'.
    reduced_digits = 100000
    value = sheet.cell_value(curr_row, cols.account_col)
    if value not in mdata.account_numbers and type(value) in [int, float]:
        mdata.account_numbers.append(value)
        mdata.comp_acc_dict[value1].append(value)
        temp = value % reduced_digits
        mdata.reduced_acc_nums[str(temp).strip('0').strip('.')] = value


def input(sheet, curr_row, sdata, cols):
    """
    It takes in the 'sheet' to read from and other lists and dictionaries and
    fills them from the values in the sheet at the 'curr_row'.
    It returns nothing.
    """

    # Reads transaction comments from the 4th column and appends it to the
    # list of comments.
    value = sheet.cell_value(curr_row, cols.transaction_col)
    sdata.trans_comments[curr_row] = value

    # reads credit and debit amount sums them for the current row and saves it
    # into another list.
    value = sheet.cell_value(curr_row, cols.credit_col)
    value1 = sheet.cell_value(curr_row, cols.debit_col)
    amount = 0
    if type(value) in [str, bytes] and type(value1) in [str, bytes]:
        sdata.credit[curr_row] = 0
        sdata.debit[curr_row] = 0
        amount = 0
    elif type(value) in [str, bytes]:
        amount += value1
        sdata.debit[curr_row] = value1
    elif type(value1) in [str, bytes]:
        amount += value
        sdata.credit[curr_row] = value
    else:
        amount += value + value1
    sdata.amt[curr_row] = amount


files = [
    'assets/company_related_terms.txt',
    'assets/surnames.txt',
    'assets/names.txt',
    'assets/junk.txt',
    'assets/spell_check_words.txt',
    'assets/replace.txt'
]


class common_data:

    company_related_terms = []
    surnames = []
    names = []
    junk_keywords = []
    spell_check_words = []
    ignore = []

    def __init__(self):
        with open(files[0], "r") as f:
            self.company_related_terms = [
                word.strip() for word in f.readlines()
            ]

        with open(files[1], "r") as f:
            self.surnames = [word.strip() for word in f.readlines()]

        with open(files[2], "r") as f:
            self.names = [word.strip() for word in f.readlines()]

        with open(files[3], "r") as f:
            self.junk_keywords = [word.strip() for word in f.readlines()]

        with open(files[4], "r") as f:
            self.spell_check_words = [word.strip() for word in f.readlines()]

        with open(files[5], "r") as f:
            self.ignore = [word.strip() for word in f.readlines()]


columns = collections.namedtuple(
    "columns",
    "company_col, account_col, transaction_col, credit_col, debit_col"
)

master_data = collections.namedtuple(
    "master_data",
    "companies, \
    comp_acc_dict, \
    account_numbers, \
    reduced_acc_nums, \
    lavenstein_true_words, \
    entities1, \
    entities2"
)


class per_sheet_data:

    trans_comments = ['']
    amt = [0]
    credit = [0]
    debit = [0]

    def __init__(self, rows):
        self.trans_comments = [''] * (rows)
        self.amt = [0] * (rows)
        self.credit = [0] * (rows)
        self.debit = [0] * (rows)
