import sys
sys.dont_write_bytecode = True

import difflib
import accounts
import miscellaneous
import entities
import individual
import commons


def direct_mapping(sheet, mdata, sdata, cdata, mapping):
    """
    Takes in the comments and tries to maps them to the corresponding values
    like - known company names, unknown company names, individual names,
    ATM, cheques, account numbers and other miscellaneous values.
    """

    for count, i in enumerate(sdata.trans_comments):
        s = ''
        if i != '':
            if type(i) not in [int, float]:
                words = mdata.lavenstein_true_words + cdata.spell_check_words
                i = commons.laven(words, i.lower())

                if any(word in i for word in ['salary']):
                    s = 'Salary'
                elif any(word in i for word in ['cash', 'self', 'csh', 'cwdr', 'ourselve']):
                    s = 'Cash'
                elif any(word in i for word in ['atm ', 'nfs ', 'atw ', 'eaw ', 'nwd ']):
                    if sdata.credit[count] != 0:
                        s = 'ATM Reversal'
                    else:
                        s = 'ATM'
                elif s == '':
                    # Extracting known company names

                    k = commons.refine(i, cdata)

                    for j in mdata.companies:
                        if j.lower() in k:
                            s = j
                            break
                        elif commons.stripping(j.lower(), cdata) in k:
                            s = j
                            break
                    # if s == '' and any(word in i for word in ['saradha']):
                    #     s = 'Saradha Realty India Ltd'
                    # Method for extracting the name of unknown companies.
                    if s == '':
                        s = entities.entity_recog_org(
                            k, count, mdata.entities1, sdata.trans_comments, cdata)
                    # Method for extracting the names of individuals.
                    if s == '':
                        s = individual.entity_recog_name(
                            i, count, mdata.entities2, sdata.trans_comments, cdata)
                    # Method for mapping account numbers
                    if s == '' and any(word in i for word in [' cc', ' cd']):
                        s = accounts.accnum(i, mdata)
                    # Methofd for the mapping of miscellaneous values.
                    if s == '':
                        s = miscellaneous.misc_mappings(i, mdata)
            else:
                for k in mdata.reduced_acc_nums:
                    if float(i) == float(k):
                        for j in mdata.comp_acc_dict:
                            if mdata.reduced_acc_nums[k] in mdata.comp_acc_dict[j]:
                                s = j
                                break
                        if s != '':
                            break
                if s == '':
                    i = float(i)
                    if i in mdata.account_numbers:
                        for j in mdata.comp_acc_dict:
                            if i in mdata.comp_acc_dict[j]:
                                s = j
                                break

        if s != '':
            sdata.trans_comments[count] = ''
        # print s
        mapping[count] = s
        # print count, ' ',
        if s != '':
            sheet.write('A' + str(count), s)

    count = 0
    for count, i in enumerate(sdata.trans_comments):
        s = ''
        if i != '' and type(i) not in [float, int]:
            k = commons.stripping(i, cdata)
            for j in mdata.entities1:
                if k in j:
                    s = j

        if s != '':
            mapping[count] = s
            sheet.write('A' + str(count), s)
    # print count
