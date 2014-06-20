import xlrd
import xlsxwriter
import getData
import comp 
import  accounts
import printing

# read the xlsx file
workbook = xlrd.open_workbook("saradha.xlsx")
worksheet = workbook.sheet_by_name('Sheet1')
rows = worksheet.nrows - 1

org = []        # list of distinct companies
acc = []        # list of distinct account numbers
cd = {}         # {row number having substring 'cd' : comment containing keyword 'cd'}
chq = {}        # {row number having cheques : check numbers}
reducedAcc = {} # {last six digits of the account number : whole account number}
comments = [''] * (rows+1)   # list having all the transaction comments
transaction = [''] * (rows+1)           # list having all the transaction details
orgAcc = {}     # {company name : [list of account numbers associated with the company]}
mapping = [''] * (rows+2)    # mapped fields
amt = [0] * (rows+1)        # list of credit and debit amount
trf = {}        # {row number having substring 'trf' or 'transfer' : comment containing keyword 'trf'}
lavensteinTrue = []     # list of the true words from the company

mapping[0] = 'Level 1, 2 & 3'

curr_row = 0
while curr_row < rows:
        curr_row += 1
        row = worksheet.row(curr_row)
        getData.input(worksheet, curr_row, cd, org, orgAcc, acc, reducedAcc, comments, transaction, chq, trf, amt, lavensteinTrue)


workbook = xlsxwriter.Workbook('alpha.xlsx')
worksheet = workbook.add_worksheet()

comp.direct_mapping(worksheet, comments, org, reducedAcc, orgAcc, mapping, lavensteinTrue)
print "direct_mapping over"

accounts.accnum(worksheet, cd, reducedAcc, orgAcc, mapping)
print "accnum over"

printing.p(org, acc, reducedAcc, cd, chq, orgAcc, comments, trf, lavensteinTrue)

count=0
index=0
amount=0
for i in mapping:
        if i!='':
                count+=1
                amount+=amt[index]
        index+=1
print count
print amount

mapping[0] = 'Level 1, 2 & 3'
worksheet.write('A1', "Level 1, 2 & 3")

workbook.close()