import sys
sys.dont_write_bytecode = True

import replace_words
import commons


def refine(comment, cdata):

    for i in replace_words.replacing_indi:
        comment = comment.replace(i, replace_words.replacing_indi[i])

    words = cdata.surnames + cdata.names
    comment = commons.correct(words, comment)

    return comment


def entity_recog_name(comment, count, entities, trans_comments, cdata):
    """
    Checks for the potential individual name in a string and returns the value.

    It checks according to the saved surnames in the 'assets/surnames.txt'
    and stops just before the junk value before the name.
    """

    temp = refine(comment, cdata)

    lis = temp.split()
    name = ''
    for j in cdata.surnames:
        if j in lis:
            trans_comments[count] = ''
            k = lis.index(j) - 1
            name = j
            while k >= 0:
                if not commons.junk(lis[k], cdata):
                    name = lis[k] + ' ' + name
                else:
                    break
                k -= 1
            name = name.strip()
            if len(name.split()) < 2:
                s = ''
                name = ''
                continue
            entities.append(name)
            break
    return name
