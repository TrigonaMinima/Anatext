def misc_mappings(comment, account_numbers, comp_acc_dict, reduced_acc_nums):
    """Takes the transaction comment string and maps for miscellaneous mappings."""
    s = ''
    if any(word in comment for word in ['chq', 'cheque', 'chk', 'mc ', 'ch ', 'c no', 'cn ', 'mcc']):
        s = 'Cheque'
    if s == '' and any(word in comment for word in ['neft']):
        s = 'NEFT'
    if s == '' and any(word in comment for word in ['rtgs']):
        s = 'RTGS'
    if s == '' and any(word in comment for word in ['clg', 'clearing']):
        s = 'Clearing'
    if s == '' and any(word in comment for word in ['tax']):
        s = 'Tax'
    if s == '' and any(word in comment for word in ['loan']):
        s = 'Loan'
    if s == '' and any(word in comment for word in ['fd', 'rdp']):
        s = 'Investment'
    if s == '' and any(word in comment for word in ['charge', 'chg', 'chrg']):
        s = 'Charges'
    if s == '' and (any(word in comment for word in ['trf to', 'by', 'frm']) and len(comment.split()) > 1):
        # if 'by' in comment:
        #     temp = comment.split()[1]
        # else:
        #     temp = comment.split()[2]
        for num in comment.split():
            if num.isdigit():
                temp = num
                break
            else:
                temp = ''

        if temp != '':
            for num in reduced_acc_nums:
                if float(temp) == float(num):
                    for fullnum in comp_acc_dict:
                        if reduced_acc_nums[num] in comp_acc_dict[fullnum]:
                            s = fullnum
                            break
                    if s != '':
                        break
            if s == '':
                temp = float(temp)
                if temp in account_numbers:
                    for comp in comp_acc_dict:
                        if temp in comp_acc_dict[comp]:
                            s = comp
                            break
                else:
                    s = 'Unidentified account'

    if s == '' and (comment.replace(' ', '').isdigit() or comment.replace('to', '').replace('trf', '').replace('trfr', '').replace('ddr', '').replace(' ', '').isdigit()) and len(comment.replace(' ', '')) > 6:
        s = 'interconnected'
    if s == '' and any(word in comment for word in ['trf', 'tran', 'trn', 'credit', 'prcr', 'pos']):
        s = 'Transfer'
    if s == '' and any(word in comment for word in ['reject']):
        s = 'Reject'
    if s == '' and any(word in comment for word in ['tds']):
        s = 'TDS'
    if s == '' and any(word in comment for word in [' bc ']):
        s = 'BC'
    if s == '' and any(word in comment for word in ['po issued', 'pos issued', ' po ']):
        s = 'PO'
    if s == '' and any(word in comment for word in ['retd',  'return', 'reversal', 'reject', 'insufficient', 'error', 'reversed', 'cancelled', 'wrong', 'rev', 'wrng']):
        s = 'Reversal'
    return s
