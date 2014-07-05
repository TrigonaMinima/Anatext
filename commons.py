import difflib

company_related_terms = []
surnames = []
junk_keywords = []
spell_check_words = []

ignore = [
    'development limited', 'private limited', 'automobiles limited', 'company pvt. ltd.', 'india ltd',
    'and travels ltd.', 'pvt. ltd.', 'pvt ltd', 'pvt.ltd.', 'ltd.', 'ltd', 'communication']  # 'cement private limited',

chars = ['/ioba', 'to:', 'a/c', '#', '-', '!', '@', '$', '%', '^', '&', '*',
         '(', ')', '_', '+', '=', '`', '~', ';', ':', '/', ',', '.', '   ', '  ', '|']

replace = {'&': ' and ',
           'ltd': ' ltd ',
           'pvt': ' pvt ',
           ' pv ': ' pvt ',
           'properties': ' properties ',
           ' prop ': ' properties ',
           'limited': ' ltd ',
           'entp': ' enterprise ',
           'engg': ' engineering ',
           'trdg': ' trading ',
           'commn': ' communication ',
           'mkt ': ' market ',
           'hitech': ' hi tech ',
           'tele media': ' telemedia ',
           ' pub ': ' publications ',
           'india': ' india ',
           'private': ' pvt ',
           'pratidin': ' pratidin ',
           ' .com ': '.com ',
           ' pro ': ' productions ',
           'comm ': ' communication ',
           'commn ': ' communication ',
           ' i ': ' india '}


def correct(words, comment):
    """Corrects the comment
    """
    comment = ' ' + comment
    if 'pvt' not in comment or 'private' not in comment:
        comment = comment.replace(' p ', ' pvt ')
    if 'hi tech ' not in comment:
        comment = comment.replace(' tech ', ' technologies ')
    for i in replace:
        comment = comment.replace(i, replace[i])
    for i in chars:
        comment = comment.replace(i, ' ')

    lis = comment.split()
    for i in lis:
        suggestions = difflib.get_close_matches(i, words)
        if len(suggestions):
            if difflib.SequenceMatcher(None, i, suggestions[0]).ratio() > 0.800:
                comment = comment.replace(i, suggestions[0])
    return comment


def stripping(company_name):
    """Strips the company names of the names whichever is found first in ignoring list."""
    for i in ignore:
        if i in company_name:
            return company_name[:-len(i) - 1]
    return company_name
