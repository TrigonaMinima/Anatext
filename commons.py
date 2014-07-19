import difflib
import replace_words

company_related_terms = []
surnames = []
names = []
junk_keywords = []
spell_check_words = []
replacing = replace_words.replacing

ignore = replace_words.ignore

chars = ['/ioba', 'to:', 'a/c', '#', '-', '!', '@', '$', '%', '^', '&', '*',
         '(', ')', '_', '+', '=', '`', '~', ';', ':', '/', ',', '.', '   ', '  ', '|', '\\']


def correct(words, comment)
    lis = comment.split()
    for i in lis:
        suggestions = difflib.get_close_matches(i, words)
        if len(suggestions):
            if difflib.SequenceMatcher(None, i, suggestions[0]).ratio() > 0.800:
                comment = comment.replace(i, ' '+suggestions[0]+' ')
    comment = comment.replace(' ', '')
    return comment

def laven(words, comment):
    """Corrects the comment
    """
    comment = ' ' + comment + ' '
    if ('pvt' not in comment or 'private' not in comment) and len(comment[:comment.index(' p ')]) > 5:
        comment = comment.replace(' p ', ' pvt ')
    if 'hi tech ' not in comment:
        comment = comment.replace(' tech ', ' technologies ')

    for i in chars:
        comment = comment.replace(i, ' ')
    for i in replacing:
        comment = comment.replace(i, replace[i])

    comment = correct(words, comment)
    return comment



def stripping(company_name):
    """Strips the company names of the names whichever is found first in ignoring list."""
    # company_name = company_name.replace('.', '')
    company_name = company_name.replace('limited', 'ltd')
    company_name = company_name.replace('private', 'pvt')
    for i in ignore:
        if i in company_name:
            return company_name[:-len(i) - 1]
    return company_name
