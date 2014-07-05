def misc_mappings(comment, account_numbers, comp_acc_dict):
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
    if s == '' and (('trf to' in comment and len(comment.split()) > 2) or ('by' in comment and len(comment.split()) > 1)):
        if 'by' in comment:
            temp = comment.split()[1]
        else:
            temp = comment.split()[2]
        if temp != '' and temp.isdigit():
            temp = float(temp)
            if temp in account_numbers:
                for j in comp_acc_dict:
                    if temp in comp_acc_dict[j]:
                        s = j
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
    if s == '' and any(word in comment for word in ['po issued', 'pos issued']):
        s = 'PO'
    if s == '' and any(word in comment for word in ['retd',  'return', 'reversal', 'reject', 'insufficient', 'error', 'reversed', 'cancelled']):
        s = 'Reversal'
    return s
