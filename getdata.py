import commons


def input(sheet, companies, cd, comp_acc_dict, account_numbers, reduced_acc_nums, trans_comments, amt, lavenstein_true_words, credit, debit, curr_row):
    """It takes in the 'sheet' to read from and other lists and dictionaries and fills them from the values in the sheet at the 'curr_row'. It returns nothing."""

    temp = 0
    # Reads company name from the column 0th of 'curr_row' and appends it to
    # the list if it is distinct. Also, makes a list of words named
    # 'lavenstein_true_words' to be used to correct the spellings of these
    # companies.
    value1 = sheet.cell_value(curr_row, 0)
    if value1 == 'SARADHA':
        value1 = 'Saradha Realty India Ltd'
    if value1 not in companies:
        companies.append(value1)
        comp_acc_dict[value1] = []
        for i in commons.stripping(value1.lower()).split():
            if i not in lavenstein_true_words:
                lavenstein_true_words.append(i)

    # Reads account number from the 2nd column and appends it to the list
    # distinctly. Also appends it to the dictionary for orgs and their
    # corresponding account numbers. Makes a new dictionary key with reduced
    # digits (here 5 digits) with a value of full account number. Factor can
    # be changed by changing the value of 'reduced_digits'.
    reduced_digits = 100000
    value = sheet.cell_value(curr_row, 3)
    if value not in account_numbers:
        account_numbers.append(value)
        comp_acc_dict[value1].append(value)
        temp = value % reduced_digits
        reduced_acc_nums[str(temp).strip('0').strip('.')] = value

    # Reads transaction comments from the 4th column and appends it to the
    # list of comments.
    value = sheet.cell_value(curr_row, 6)
    trans_comments[curr_row] = value

    # reads credit and debit amount sums them for the current row and saves it
    # into another list.
    value = sheet.cell_value(curr_row, 8)
    value1 = sheet.cell_value(curr_row, 9)
    amount = 0
    if value == '':
        amount += value1
        debit[curr_row] = value1
    elif value1 == '':
        amount += value
        credit[curr_row] = value
    else:
        amount += value + value1
    amt[curr_row] = amount
