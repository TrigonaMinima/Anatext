import commons

def junk(string):
    """Determines if the string contains any digit or a part of junk keywords as given in 'assets/junk_keywords.txt'."""
    for char in string:
        if char.isdigit():
            return True
    if string in commons.junk_keywords:
        return True
    return False


def entity_recog_org(comment, count, entities, trans_comments):
    """Checks for the potential company name in a string and returns the value.

    It checks according to the saved terms in the 'assets/company_related_terms.txt' and stops just 
    before the junk value before the name.
    """
    s = ''
    temp = commons.correct(commons.company_related_terms, comment)
    lis = temp.split()
    name = ''
    for j in commons.company_related_terms:
        if j in lis:
            trans_comments[count] = ''
            k = lis.index(j) - 1
            if k < 1:
                break
            name = j
            while k >= 0:
                if not junk(lis[k]):
                    name = lis[k] + ' ' + name
                else:
                    break
                k -= 1
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


def entity_recog_name(comment, count, entities, trans_comments):
    """Checks for the potential individual name in a string and returns the value. 

    It checks according to the saved surnames in the 'assets/surnames.txt' and stops just 
    before the junk value before the name.
    """
    temp = commons.correct(commons.surnames, comment)
    lis = temp.split()
    name = ''
    for j in commons.surnames:
        if j in lis:
            trans_comments[count] = ''
            k = lis.index(j) - 1
            name = j
            while k >= 0:
                if not junk(lis[k]):
                    name = lis[k] + ' ' + name
                else:
                    break
                k -= 1
            entities.append(name)
            break
    return name
