import sys
sys.dont_write_bytecode = True

import collections

import xlrd
import xlsxwriter
import comp
import accounts
import printing
import getdata

excel_files = {
    'Data/icore_banking_data.xlsx': ['Report', 'Data/icore.xlsx']
}

# excel_files = {
#     'Data/RoseVally1.xlsx': ['RoseVallyAllDataPart1', 'Data/alpha1.xlsx'],
#     'Data/RoseVally2.xlsx': ['RoseVallyAllDataPart2', 'Data/alpha2.xlsx'],
#     'Data/RoseVally3.xlsx': ['RoseVallyAllDataPart3', 'Data/alpha3.xlsx'],
#     'Data/RoseVally4.xlsx': ['RoseVallyAllDataPart4', 'Data/alpha4.xlsx']}


cols = getdata.columns(0, 7, 2, 5, 4)

mdata = getdata.master_data([], {}, [], {}, [], [], [])

cdata = getdata.common_data()


# Iterates through the xlsx file and creates a master data set.
for sheet in excel_files:
    rows = 0
    workbook = xlrd.open_workbook(sheet)
    worksheet = workbook.sheet_by_name(excel_files[sheet][0])
    for curr_row in range(1, worksheet.nrows):
        row = worksheet.row(curr_row)
        getdata.create(worksheet, curr_row, mdata, cdata, cols)


# Create a summary file
with open('Data/summary.txt', 'w') as f:

    # Iterates through the xlsx file and calls input() function of getdata
    # module.
    for sheet in excel_files:

        workbook = xlrd.open_workbook(sheet)
        worksheet = workbook.sheet_by_name(excel_files[sheet][0])
        rows = worksheet.nrows

        mapping = [''] * (rows)

        sdata = getdata.per_sheet_data(rows)

        for curr_row in range(1, rows):
            row = worksheet.row(curr_row)
            getdata.input(worksheet, curr_row, sdata, cols)

        # Opens a new xlsx file named 'alpha.xlsx' to write the mappings into
        # it.
        workbook = xlsxwriter.Workbook(excel_files[sheet][1])
        worksheet = workbook.add_worksheet()

        # First, the direct mapping is done. The names and common words occuring
        # in transaction comments are checked and separated.
        comp.direct_mapping(worksheet, mdata, sdata, cdata, mapping)

        print("direct_mapping over")

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
            total_cr_amount += sdata.credit[index]
            total_de_amount += sdata.debit[index]
            # print(index, ' ',)

            if i != '':
                count += 1
                amount += sdata.amt[index]
                cr_amount += sdata.credit[index]
                de_amount += sdata.debit[index]
            index += 1
        # print()
        print(count)
        print(amount)

        mapping[0] = 'Mappings'
        worksheet.write('A1', "Mappings")

        # Closed the 'alpha.xlsx' after writing the mappings.
        workbook.close()

        f.write("-----\nFile - " + sheet + "\n-----\n\nLines     : " +
                '{:07d}'.format(rows) + "            ")
        f.write("Mapped Lines  : " + '{:07d}\n'.format(count))

        f.write(
            "Credit    : " + '{:03f}'.format(total_cr_amount) + "            ")
        f.write("Mapped Credit : " + '{:03f}\n'.format(cr_amount))
        f.write(
            "Debit    : " + '{:03f}'.format(total_de_amount) + "            ")

        f.write("Mapped Debit  : " + '{:03f}\n\n'.format(de_amount))
        f.write("Mapped amount : " + '{:03f}\n\n'.format(amount))

        f.write("      Credit Info: Later\n")
        f.write("      Debit Info: Later\n\n\n")
