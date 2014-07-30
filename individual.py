import sys
sys.dont_write_bytecode = True

import commons
import replace_words

def refine(comment):

    for i in replace_words.replacing_indi:
        comment = comment.replace(i, replace_words.replacing_indi[i])

    comment = commons.correct(commons.surnames+commons.names, comment)
    # comment = comment.replace(' pvt ', ' p ')
    # comment = comment.replace(' india ', ' i ')

    return comment

def entity_recog_name(comment, count, entities, trans_comments):
    """Checks for the potential individual name in a string and returns the value. 

    It checks according to the saved surnames in the 'assets/surnames.txt' and stops just 
    before the junk value before the name.
    """

    temp = refine(comment)

    lis = temp.split()
    name = ''
    for j in commons.surnames:
        if j in lis:
            trans_comments[count] = ''
            k = lis.index(j) - 1
            name = j
            while k >= 0:
                if not commons.junk(lis[k]):
                    name = lis[k] + ' ' + name
                else:
                    break
                k -= 1
            name = name.strip()
            if len(name.split()) < 2:
                s=''
                name = ''
                continue
            entities.append(name)
            break
    return name