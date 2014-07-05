
def check_acc(string, reduced_acc_nums, comp_acc_dict):
    """Checks the string for company names if else either returns 'cd/cc' or 'Interconnected'."""
    if len(string) < 3:
        return 'cd/cc'
    elif len(string) in range(3, 6):
        for i in reduced_acc_nums:
            if string in i:
                for j in comp_acc_dict:
                    if reduced_acc_nums[i] in comp_acc_dict[j]:
                        return j
    else:
        return "Interconnected"


def accnum(cdcc, reduced_acc_nums, comp_acc_dict):
    """Gets the string in 'cdcc' and return any one of the 4 strings - 'Various', 'Interconnected', 'cd/cc' 
    or name of the mapped company, depending on the conditions.
    """
    count = 0
    s = ''
    if 'various' not in cdcc:
        temp = ''
        temp = ''.join(x for x in cdcc if x.isdigit())
        count += 1
        s = check_acc(temp, reduced_acc_nums, comp_acc_dict)
    else:
        s = "Various"
        count += 1
    # print count
    return s
