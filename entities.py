import sys
sys.dont_write_bytecode = True

import commons


def entity_recog_org(comment, count, entities, trans_comments):
    """Checks for the potential company name in a string and returns the value.

    It checks according to the saved terms in the 'assets/company_related_terms.txt' and stops just
    before the junk value before the name.
    """
    s = ''

    temp = comment

    # temp = commons.refine(comment)

    # Extraction starts here
    lis = temp.split()
    name = ''
    for j in commons.company_related_terms:
        if j in lis:
            k = lis.index(j) - 1
            if k < 1:
                break
            name = j
            while k >= 0:
                if not commons.junk(lis[k]):
                    name = lis[k] + ' ' + name
                else:
                    break
                k -= 1
            name = ' ' + name
            if len(name.split()) < 2:
                name = ''
                continue
            trans_comments[count] = ''
            name = name.strip()
            for k in entities:
                if commons.stripping(name) in k:
                    s = k
                    break
                elif commons.stripping(k) in name:
                    entities.pop(entities.index(k))
                    # entities.append(name)
                    # s = name
            if s == '':
                entities.append(name)
                s = name
            break
    return s
