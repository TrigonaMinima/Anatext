import xlrd
import xlsxwriter
import getdata
import comp
import accounts
import commons
import printing

# Loads the company related terms from the file
# 'assets/company_related_terms.txt'
f = open('assets/company_related_terms.txt', "r")
commons.company_related_terms = [word.strip() for word in f.readlines()]
f.close()

# Loads the surnames from the file 'assets/surnames.txt'
f = open('assets/surnames.txt', "r")
commons.surnames = [word.strip() for word in f.readlines()]
f.close()

# Loads the names from the file 'assets/names.txt'
f = open('assets/names.txt', "r")
commons.names = [word.strip() for word in f.readlines()]
f.close()

# Loads the junk words which might come before a name from the file
# 'assets/junk.txt'
f = open('assets/junk.txt', "r")
commons.junk_keywords = [word.strip() for word in f.readlines()]
f.close()

# Loads the normal words which might be spelled incorectly from the file
# 'assets/spell_check_words.txt'
f = open('assets/spell_check_words.txt', "r")
commons.spell_check_words = [word.strip() for word in f.readlines()]
f.close()


excel_files = {'RoseVally1.xlsx': ['RoseVallyAllDataPart1', 'alpha1.xlsx'],
               'RoseVally2.xlsx': ['RoseVallyAllDataPart2', 'alpha2.xlsx'],
               'RoseVally3.xlsx': ['RoseVallyAllDataPart3', 'alpha3.xlsx'],
               'RoseVally4.xlsx': ['RoseVallyAllDataPart4', 'alpha4.xlsx']}


# Global variables
company_col = 0
account_col = 3
transaction_col = 6
credit_col = 8
debit_col = 9

companies = []
account_numbers = []
# {last six digits of the account number : whole account number}
reduced_acc_nums = {}
# {company name : [list of account numbers associated with the company]}
comp_acc_dict = {}
# list of the correct words from the known company names given in the 1st
# column of the excel file.
lavenstein_true_words = []
# list of unknown companies
entities1 = []
# list of names
entities2 = []


# Iterates through the xlsx file and creates a master data set.
for sheet in excel_files:

    rows = 0
    workbook = xlrd.open_workbook(sheet)
    worksheet = workbook.sheet_by_name(excel_files[sheet][0])
    rows = worksheet.nrows
    # print rows
    curr_row = 0
    while curr_row < rows-1:
        curr_row += 1
        # print curr_row, '  ',
        row = worksheet.row(curr_row)
        getdata.master_data_create(worksheet, companies, comp_acc_dict,
                                   account_numbers, reduced_acc_nums, lavenstein_true_words, curr_row)


# Iterates through the xlsx file and calls input() function of getdata module.
for sheet in excel_files:

    rows = 0
    workbook = xlrd.open_workbook(sheet)
    worksheet = workbook.sheet_by_name(excel_files[sheet][0])
    rows = worksheet.nrows

    # list having all the transaction comments
    trans_comments = [''] * (rows + 1)
    # list of credit and debit amount
    amt = [0] * (rows + 1)
    credit = [0] * (rows + 1)
    debit = [0] * (rows + 1)
    mapping = [''] * (rows + 2)

    curr_row = 0
    while curr_row < rows-1:
        curr_row += 1
        row = worksheet.row(curr_row)
        getdata.input(worksheet, trans_comments, amt, credit, debit, curr_row)

    # Opens a new xlsx file named 'alpha.xlsx' to write the mappings into it.
    workbook = xlsxwriter.Workbook(excel_files[sheet][1])
    worksheet = workbook.add_worksheet()

    # First, the direct mapping is done. The names and common words occuring
    # in transaction comments are checked and separated.
    comp.direct_mapping(
        worksheet, companies, trans_comments, reduced_acc_nums, comp_acc_dict, mapping,
        lavenstein_true_words, entities1, entities2, account_numbers, credit)
    print "direct_mapping over"

    # printing.p(companies, account_numbers, reduced_acc_nums, cd, comp_acc_dict, trans_comments,
    #            lavenstein_true_words, entities1)
    # Total amount mapped is calculated.
    count = 0
    index = 0
    amount = 0
    for i in mapping:
        if i != '':
            count += 1
            amount += amt[index]
        index += 1
    print count
    print amount

    mapping[0] = 'Mappings'
    worksheet.write('A1', "Mappings")

    # Closed the 'alpha.xlsx' after writing the mappings.
    workbook.close()
