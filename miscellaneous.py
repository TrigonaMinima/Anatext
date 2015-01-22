def replaces(comment):
    lis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    for i in lis:
        comment = comment.replace(i, '')
    comment = comment.strip()
    return comment


def misc_mappings(comment, account_numbers, comp_acc_dict, reduced_acc_nums):
    """
    Takes the transaction comment string and maps for miscellaneous
    mappings.
    """
    s = ''
    temp = ''
    keywords = ['trf', 'to', 'by', 'frm', 'ft ', 'td ', ' loa ', 'tr', 'from']
    if (any(word in comment for word in keywords) and len(comment.split()) > 1):
        new_comment = replaces(comment).split()
        for num in new_comment:
            if num.isdigit():
                temp = num
                break
            else:
                temp = ''

        if temp != '' and len(temp) > 16:
            s = 'Interconnected'
        elif len(temp) > 8:
            for num in reduced_acc_nums:
                if float(temp) == float(num):
                    for fullnum in comp_acc_dict:
                        if reduced_acc_nums[num] in comp_acc_dict[fullnum]:
                            s = fullnum
                            break
                    if s != '':
                        break
            if s == '':
                s = 'Unidentified account'
        elif len(temp) > 2:
            temp = float(temp)
            if temp in account_numbers:
                for comp in comp_acc_dict:
                    if temp in comp_acc_dict[comp]:
                        s = comp
                        break
            if s == '':
                count = 0
                for i in new_comment:
                    if len(i) > 3:
                        count += 1
                if count > 1:
                    s = 'Interconnected'
        else:
            s = ''
    if s == '' and (comment.replace('to', '').replace('trf', '').replace('trfr', '').replace('ddr', '').replace(' ', '').isdigit()) and len(comment.replace(' ', '')) > 6:
        s = 'Interconnected'
    if s == '' and any(word in comment for word in ['chq', 'cheque', 'chk', 'mc ', ' ch ', 'c no', 'cn ', 'mcc', ' chno ']):
        s = 'Cheque'
    if s == '' and any(word in comment for word in ['clg', 'clearing']):
        s = 'Clearing'
    if s == '' and any(word in comment for word in ['neft']):
        s = 'NEFT'
    if s == '' and any(word in comment for word in ['rtgs', 'rtg ']):
        s = 'RTGS'
    if s == '' and any(word in comment for word in ['reject']):
        s = 'Reject'
    reversal = [
        'retd',  'return', 'reversal', 'reject', 'insuf',
        'error', 'reversed', 'cancelled', 'wrong', 'rev', 'wrng']
    if s == '' and any(word in comment for word in reversal):
        s = 'Reversal'
    if s == '' and any(word in comment for word in ['tax']):
        s = 'Tax'
    if s == '' and any(word in comment for word in ['charge', 'chg', 'chrg']):
        s = 'Charges'
    if s == '' and any(word in comment for word in ['trf', 'tran', 'trn', 'credit', 'prcr', 'pos', 'transfer']):
        if 'credit' in comment:
            s = 'Transfer-credit'
        elif 'debit' in comment:
            s = 'Transfer-debit'
        elif 'deposit' in comment:
            s = 'Deposit'
        else:
            s = 'Transfer'
    if s == '' and any(word in comment for word in ['tds']):
        s = 'TDS'
    if s == '' and any(word in comment for word in ['loan']):
        s = 'Loan'
    if s == '' and any(word in comment for word in ['fd ', 'rdp']):
        s = 'Investment'
    if s == '' and any(word in comment for word in [' bc ']):
        s = 'BC'
    if s == '' and any(word in comment for word in ['po issued', 'pos issued', ' po ']):
        s = 'PO'
    if s == '' and any(word in comment for word in ['various']):
        s = 'Various'
    if s == '' and any(word in comment for word in [' lc']):
        s = 'LC'
    return s
