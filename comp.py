import sys
sys.dont_write_bytecode = True

import difflib
import commons
import accounts
import miscellaneous
import entities
import individual


def direct_mapping(
    sheet, companies, trans_comments, reduced_acc_nums, comp_acc_dict, mapping, lavenstein_true_words,
        entities1, entities2, account_numbers, credit):
    """Takes in the comments and tries to maps them to the corresponding values like - known company names,
    unknown company names, individual names, ATM, cheques, account numbers and other miscellaneous values.
    """
    count = 0
    for i in trans_comments:
        s = ''
        if i != '':
            if type(i) not in [int, float]:
                i = commons.laven(
                    lavenstein_true_words + commons.spell_check_words, i.lower())
                if any(word in i for word in ['salary']):
                    s = 'Salary'
                elif any(word in i for word in ['cash', 'self', 'csh', 'cwdr', 'ourselve']):
                    s = 'Cash'
                elif any(word in i for word in ['atm ', 'nfs ', 'atw ', 'eaw ', 'nwd ']):
                    if credit[count] != 0:
                        s = 'ATM Reversal'
                    else:
                        s = 'ATM'
                elif s == '':
                    # Extracting known company names

                    k = commons.refine(i)

                    for j in companies:
                        if j.lower() in k:
                            s = j
                            break
                        elif commons.stripping(j.lower()) in k:
                            s = j
                            break
                    # if s == '' and any(word in i for word in ['saradha']):
                    #     s = 'Saradha Realty India Ltd'
                    # Method for extracting the name of unknown companies.
                    if s == '':
                        s = entities.entity_recog_org(
                            k, count, entities1, trans_comments)
                    # Method for extracting the names of individuals.
                    if s == '':
                        s = individual.entity_recog_name(
                            i, count, entities2, trans_comments)
                    # Method for mapping account numbers
                    if s == '' and any(word in i for word in [' cc', ' cd']):
                        s = accounts.accnum(i, reduced_acc_nums, comp_acc_dict)
                    # Methofd for the mapping of miscellaneous values.
                    if s == '':
                        s = miscellaneous.misc_mappings(
                            i, account_numbers, comp_acc_dict, reduced_acc_nums)
            else:
                for k in reduced_acc_nums:
                    if float(i) == float(k):
                        for j in comp_acc_dict:
                            if reduced_acc_nums[k] in comp_acc_dict[j]:
                                s = j
                                break
                        if s != '':
                            break
                if s == '':
                    i = float(i)
                    if i in account_numbers:
                        for j in comp_acc_dict:
                            if i in comp_acc_dict[j]:
                                s = j
                                break

        if s != '':
            trans_comments[count] = ''
        # print s
        mapping[count] = s
        # print count, ' ',
        count += 1
        if s != '':
            sheet.write('A' + str(count), s)

    count = 0
    for i in trans_comments:
        s = ''
        if i != '' and type(i) not in [float, int]:
            k = commons.stripping(i)
            for j in entities1:
                if k in j:
                    s = j

        count += 1
        if s != '':
            mapping[count] = s
            sheet.write('A' + str(count), s)
    # print count
