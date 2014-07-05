import xlrd
import xlsxwriter
import getdata
import comp
import accounts
import commons
import printing


# Read the xlsx file
workbook = xlrd.open_workbook("saradha.xlsx")
worksheet = workbook.sheet_by_name('Sheet1')
rows = worksheet.nrows - 1

# Global variables
companies = []
account_numbers = []
# {row number having substring 'cd' : comment containing keyword 'cd'}
cd = {}
# {last six digits of the account number : whole account number}
reduced_acc_nums = {}
# list having all the transaction comments
trans_comments = [''] * (rows + 1)
# {company name : [list of account numbers associated with the company]}
comp_acc_dict = {}
mapping = [''] * (rows + 2)
# list of credit and debit amount
amt = [0] * (rows + 1)
credit = [0] * (rows + 1)
debit = [0] * (rows + 1)
# list of the correct words from the known company names given in the 1st
# column of the excel file.
lavenstein_true_words = []
# list of orgs
entities1 = []
# list of names
entities2 = []

# Loads the company related terms from the file
# 'assets/company_related_terms.txt'
f = open('assets/company_related_terms.txt', "r")
commons.company_related_terms = [word.strip() for word in f.readlines()]
f.close()

# Loads the surnames from the file 'assets/surnames.txt'
f = open('assets/surnames.txt', "r")
commons.surnames = [word.strip() for word in f.readlines()]
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


# Iterates through the xlsx file and calls input() function of getdata module.
curr_row = 0
while curr_row < rows:
    curr_row += 1
    row = worksheet.row(curr_row)
    getdata.input(
        worksheet, companies, cd, comp_acc_dict, account_numbers, reduced_acc_nums,
        trans_comments, amt, lavenstein_true_words, credit, debit, curr_row)

# Opens a new xlsx file named 'alpha.xlsx' to write the mappings into it.
workbook = xlsxwriter.Workbook('alpha.xlsx')
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

mapping[0] = 'Level 1, 2 & 3'
worksheet.write('A1', "Level 1, 2 & 3")

# Closed the 'alpha.xlsx' after writing the mappings.
workbook.close()
