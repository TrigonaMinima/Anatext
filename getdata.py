import commons


def master_data_create(sheet, companies, comp_acc_dict, account_numbers, reduced_acc_nums, lavenstein_true_words, curr_row, company_col, account_col):
    """It takes in the 'sheet' to read from and other lists and dictionaries and fills them from the values in the sheet at the 'curr_row'. It returns nothing."""

    temp = 0
    # Reads company name from the column 0th of 'curr_row' and appends it to
    # the list if it is distinct. Also, makes a list of words named
    # 'lavenstein_true_words' to be used to correct the spellings of these
    # companies.
    value1 = sheet.cell_value(curr_row, company_col)
    value1 = value1.replace('.', ' ')
    value1 = value1.replace('  ', ' ')
    value1 = value1.strip()
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
    value = sheet.cell_value(curr_row, account_col)
    if value not in account_numbers and type(value) in [int, float]:
        account_numbers.append(value)
        comp_acc_dict[value1].append(value)
        temp = value % reduced_digits
        reduced_acc_nums[str(temp).strip('0').strip('.')] = value


def input(sheet, trans_comments, amt, credit, debit, curr_row, transaction_col, credit_col, debit_col):
    """It takes in the 'sheet' to read from and other lists and dictionaries and fills them from the values in the sheet at the 'curr_row'. It returns nothing."""

    # Reads transaction comments from the 4th column and appends it to the
    # list of comments.
    value = sheet.cell_value(curr_row, transaction_col)
    trans_comments[curr_row] = value

    # reads credit and debit amount sums them for the current row and saves it
    # into another list.
    value = sheet.cell_value(curr_row, credit_col)
    value1 = sheet.cell_value(curr_row, debit_col)
    amount = 0
    if type(value) == str and type(value1) == str:
        credit[curr_row] = 0
        debit[curr_row] = 0
        amount = 0
    elif type(value) == str:
        amount += value1
        debit[curr_row] = value1
    elif type(value1) == str:
        amount += value
        credit[curr_row] = value
    else:
        amount += value + value1
    amt[curr_row] = amount
