import xlrd
import xlsxwriter

# read the xlsx file
workbook = xlrd.open_workbook("saradha.xlsx")
worksheet = workbook.sheet_by_name('Sheet1')
rows = worksheet.nrows - 1

strings = []    # list of strings other than companies in org
org = []        # list of distinct companies
acc = []        # list of distinct account numbers
cd = {}         # {row number having substring 'cd' : comment containing keyword 'cd'}
chq = {}        # {row number having cheques : check numbers}
reducedAcc = {} # {last six digits of the account number : whole account number}
comments = [''] * (rows+1)   # list having all the transaction comments
orgAcc = {}     # {company name : [list of account numbers associated with the company]}
mapping = [''] * (rows+1)    # mapped fields
amt = [0] * (rows+1)        # list of credit and debit amount
trf = {}        # {row number having substring 'trf' or 'transfer' : }

def input(curr_row):
        temp = 0
        # reads company name
        value1 = worksheet.cell_value(curr_row, 0)
        if value1 not in org:
                org.append(value1)
                orgAcc[value1] = []

        # reads account number
        value = worksheet.cell_value(curr_row, 2)
        if value not in acc:
                acc.append(value)
                orgAcc[value1].append(value)
                temp = value%100000
                reducedAcc[str(temp).strip('0').strip('.')]=value

        # reads transaction comments
        value = worksheet.cell_value(curr_row, 4)
        comments[curr_row] = value
        if type(value) in [float, int]:
                chq[curr_row] = value
        elif 'cd' in value.lower() or 'cc' in value.lower():
                cd[curr_row] = value
                comments[curr_row] = ''
        elif ''.join(x for x in value if x.isdigit()) in [float, int]:
                chq[curr_row] = value
        elif 'trf' or 'transfer' in value.lower():
                trf[curr_row] = value
                # comments[curr_row] = ''
        else:
                strings.append(value)

        # reads credit and debit amount
        value = worksheet.cell_value(curr_row, 6)
        value1 =  worksheet.cell_value(curr_row, 7)
        amount=0
        if value == '':
                amount+=value1
        elif value1 == '':
                amount+=value
        else:
                amount+=value+value1
        amt[curr_row] = amount

mapping[0] = 'Level 1, 2 & 3'
# curr_row = 0
# while curr_row <= rows:
#         mapping.append('')
#         amt.append(0)
#         comments.append('')
#         curr_row+=1

curr_row = 0
while curr_row < rows:
        curr_row += 1
        row = worksheet.row(curr_row)
        input(curr_row)

ignore = ['development limited', 'private limited', 'cement private limited', 'automobiles limited', 'company pvt. ltd.', 'india ltd', 
'pvt. ltd.', 'pvt ltd', 'pvt.ltd.', 'ltd.', 'ltd', 'communication']

cdcc = ['a/cs', '+', ';', '/']

def checkin1(comp):
        for i in ignore:
                if i in comp:
                        return comp[:-len(i)-1]
        return comp

def checkin2(comp):
        for i in cdcc:
                if i in comp:
                        return True
        return False


def direct_mapping():
        count=0
        for i in comments:
                s=''
                if i != '':
                        if type(i) not in [int, float]:
                                for j in org:
                                        if  j.lower() != 'saradha' and j.lower() in i.lower():
                                                s=j
                                                # print j
                                                comments[count] = ''
                                                break
                                        elif j.lower() != 'saradha' and checkin1(j.lower()) in i.lower():
                                                s=j
                                                # print j
                                                comments[count] = ''
                                                break
                                if s!='':
                                        if 'salary' in i.lower():
                                                s='Salary'
                                                comments[count] = ''
                                                break
                                        elif checkin2(i.lower()):
                                                print 'asdasdasm'
                                                s='Interconnected'
                                                comments[count] = ''
                                                break
                                        elif 'transfer' in i.lower() or 'trf' in i.lower() or 'trfr' in i.lower():
                                                s='Transfer'
                                                comments[count] = ''
                                                break
                                        elif 'various' in i.lower():
                                                s='various'
                                                comments[count] = ''
                                                break
                        else:
                                for k in reducedAcc:
                                        if i == reducedAcc[k]:
                                                for j in orgAcc:
                                                        if reducedAcc[k] in orgAcc[j]:
                                                                s = j
                                                                # print j
                                                                comments[count] = ''
                                                                break
                # print s
                mapping[count] = s
                count+=1
        print count


def check_acc(string, row):
        if len(string) < 3 :
                mapping[row] = ''
        elif len(string) in range(3,6):
                for i in reducedAcc:
                        if string in i:
                                for j in orgAcc:
                                        if reducedAcc[i] in orgAcc[j]:
                                                mapping[row] = j
        else:
                mapping[row] = "Interconnected"
        return 1


def accnum():
        count=0;
        for i in cd:
                # print s
                if 'various' not in cd[i].lower():
                        s=''
                        s=''.join(x for x in cd[i] if x.isdigit())
                        count += check_acc(s, i)
                else:
                        mapping[i] = "Interconnected"
                        count += 1
        print count

direct_mapping()
print "direct_mapping over"

accnum()
print "accnum over"


def p():
        print len(org)
        print org
        print len(acc)
        print acc
        print len(reducedAcc)
        print reducedAcc
        print len(cd)
        print cd
        print len(chq)
        print chq
        print len(orgAcc)
        print orgAcc
        # print comments

# p()

count=0
index=0
amount=0
for i in mapping:
        if i!='':
                count+=1
                # print index, '-', amt[index], '  ',
                amount+=amt[index]
        index+=1
print count
print amount

mapping[0] = 'Level 1, 2 & 3'

workbook = xlsxwriter.Workbook('alpha.xlsx')
worksheet = workbook.add_worksheet()

count=1
for i in mapping:
        if i!='':
                worksheet.write('A'+str(count), i)
        else:
                worksheet.write('A'+str(count), "")
        count+=1

workbook.close()