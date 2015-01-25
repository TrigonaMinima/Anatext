
def check_acc(string, mdata):
    """
    Checks the string for company names if else either
    returns 'cd/cc' or 'Interconnected'.
    """
    if any(word in string for word in ['trf', 'tran', 'trn', 'credit', 'prcr', 'pos', 'transfer']):
        return 'Transfer'
    if len(string) < 3:
        return 'cd/cc'
    elif len(string) in range(3, 6):
        for i in mdata.reduced_acc_nums:
            if float(string) == float(i):
                for j in mdata.comp_acc_dict:
                    if mdata.reduced_acc_nums[i] in mdata.comp_acc_dict[j]:
                        return j
    else:
        return "Interconnected"


def accnum(cdcc, mdata):
    """
    Gets the string in 'cdcc' and return any one of the
    4 strings - 'Various', 'Interconnected', 'cd/cc' or name of the mapped
    company, depending on the conditions.
    """
    count = 0
    s = ''
    if 'various' not in cdcc:
        temp = ''
        temp = ''.join(x for x in cdcc if x.isdigit())
        count += 1
        s = check_acc(temp, mdata)
    else:
        s = "Various"
        count += 1
    # print count
    return s
