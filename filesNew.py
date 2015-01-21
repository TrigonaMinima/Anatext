import sys
sys.dont_write_bytecode = True

import xlrd
import xlsxwriter
import getdata
import comp
import accounts
import commons
import printing

# Loads the company related terms from the file
# 'assets/company_related_terms.txt'
with open('assets/company_related_terms.txt', "r") as f:
    commons.company_related_terms = [word.strip() for word in f.readlines()]

# Loads the surnames from the file 'assets/surnames.txt'
with open('assets/surnames.txt', "r") as f:
    commons.surnames = [word.strip() for word in f.readlines()]

# Loads the names from the file 'assets/names.txt'
with open('assets/names.txt', "r") as f:
    commons.names = [word.strip() for word in f.readlines()]

# Loads the junk words which might come before a name from the file
# 'assets/junk.txt'
with open('assets/junk.txt', "r") as f:
    commons.junk_keywords = [word.strip() for word in f.readlines()]

# Loads the normal words which might be spelled incorectly from the file
# 'assets/spell_check_words.txt'
with open('assets/spell_check_words.txt', "r") as f:
    commons.spell_check_words = [word.strip() for word in f.readlines()]

# Loads the ignore words which might be come in company name from
# the file 'assets/replace.txt'
with open('assets/replace.txt', "r") as f:
    commons.ignore = [word.strip() for word in f.readlines()]

excel_files = {
    'Data/icore_banking_data.xlsx': ['Report', 'Data/icore.xlsx']
}

# excel_files = {
#     'Data/RoseVally1.xlsx': ['RoseVallyAllDataPart1', 'Data/alpha1.xlsx'],
#     'Data/RoseVally2.xlsx': ['RoseVallyAllDataPart2', 'Data/alpha2.xlsx'],
#     'Data/RoseVally3.xlsx': ['RoseVallyAllDataPart3', 'Data/alpha3.xlsx'],
#     'Data/RoseVally4.xlsx': ['RoseVallyAllDataPart4', 'Data/alpha4.xlsx']}


# Global variables
company_col = 0
account_col = 7
transaction_col = 2
credit_col = 5
debit_col = 4

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
    for curr_row in range(1, worksheet.nrows):
        row = worksheet.row(curr_row)
        getdata.master_data_create(
            worksheet, companies, comp_acc_dict,
            account_numbers, reduced_acc_nums, lavenstein_true_words,
            curr_row, company_col, account_col)

# Create a summary file
with open('Data/summary.txt', 'w') as f:

    # Iterates through the xlsx file and calls input() function of getdata module.
    for sheet in excel_files:

        workbook = xlrd.open_workbook(sheet)
        worksheet = workbook.sheet_by_name(excel_files[sheet][0])
        rows = worksheet.nrows

        # list having all the transaction comments
        trans_comments = [''] * (rows)
        # list of credit and debit amount
        amt = [0] * (rows)
        credit = [0] * (rows)
        debit = [0] * (rows)
        mapping = [''] * (rows)

        for curr_row in range(1, rows):
            row = worksheet.row(curr_row)
            getdata.input(
                worksheet, trans_comments, amt,
                credit, debit, curr_row,
                transaction_col, credit_col, debit_col)

        # Opens a new xlsx file named 'alpha.xlsx' to write the mappings into it.
        workbook = xlsxwriter.Workbook(excel_files[sheet][1])
        worksheet = workbook.add_worksheet()

        # First, the direct mapping is done. The names and common words occuring
        # in transaction comments are checked and separated.
        comp.direct_mapping(
            worksheet, companies, trans_comments, reduced_acc_nums,
            comp_acc_dict, mapping, lavenstein_true_words, entities1,
            entities2, account_numbers, credit)
        print "direct_mapping over"

        # printing.p(companies, account_numbers, reduced_acc_nums,
        #            cd, comp_acc_dict, trans_comments,
        #            lavenstein_true_words, entities1)
        # Total amount mapped is calculated.
        count = 0
        index = 0

        amount = 0
        total_cr_amount = 0
        cr_amount = 0
        total_de_amount = 0
        de_amount = 0
        for i in mapping:
            total_cr_amount += credit[index]
            total_de_amount += debit[index]
            # print index, ' ',
            if i != '':
                count += 1
                amount += amt[index]
                cr_amount += credit[index]
                de_amount += debit[index]
            index += 1
        # print
        print count
        print amount

        mapping[0] = 'Mappings'
        worksheet.write('A1', "Mappings")

        # Closed the 'alpha.xlsx' after writing the mappings.
        workbook.close()

        f.write("-----\nFile - " + sheet + "\n-----\n\nLines     : " +
                '{:07d}'.format(rows) + "            ")
        f.write("Mapped Lines  : " + '{:07d}\n'.format(count))
        f.write("Credit    : " + '{:03f}'.format(total_cr_amount) + "            ")
        f.write("Mapped Credit : " + '{:03f}\n'.format(cr_amount))
        f.write("Debit    : " + '{:03f}'.format(total_de_amount) + "            ")
        f.write("Mapped Debit  : " + '{:03f}\n\n'.format(de_amount))
        f.write("Mapped amount : " + '{:03f}\n\n'.format(amount))

        f.write("      Credit Info: Later\n")
        f.write("      Debit Info: Later\n\n\n")
