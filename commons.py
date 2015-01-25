import sys
sys.dont_write_bytecode = True

import difflib
import replace_words

chars = [
    '/ioba', 'to:', 'a/c', '#', '-', '!', '@', '$', '%', '^', '&', '*', '?', '<', '>', '\'', '\"',
    '(', ')', '_', '+', '=', '`', '~', ';', ':', '/', ',', '.', '|', '\\', '   ', '  ']


def correct(words, comment):
    for i in chars:
        comment = comment.replace(i, ' ')

    lis = comment.split()
    for word in lis:
        suggestions = difflib.get_close_matches(i, words)
        if len(suggestions):
            if difflib.SequenceMatcher(
                None,
                word,
                suggestions[0]
            ).ratio() > 0.800:
                comment = comment.replace(word, ' ' + suggestions[0] + ' ')
    comment = comment.replace('  ', ' ')
    return comment


def laven(words, comment):
    """
    Corrects the comment
    """
    comment = ' ' + comment + ' '

    for i in replace_words.replacing_misc:
        comment = comment.replace(i, replace_words.replacing_misc[i])

    return correct(words, comment)


def stripping(company_name, cdata):
    """
    Strips the company names of the names whichever is found first in
    ignoring list.
    """
    # company_name = company_name.replace('.', '')
    company_name = company_name.replace('limited', 'ltd')
    company_name = company_name.replace('private', 'pvt')
    for i in cdata.ignore:
        if i in company_name:
            return company_name[:-len(i) - 1]
    return company_name


def junk(string, cdata):
    """
    Determines if the string contains any digit or a part of junk keywords as
    given in 'assets/junk_keywords.txt'.
    """
    for char in string:
        if char.isdigit():
            return True
    if string in cdata.junk_keywords:
        return True
    return False


def refine(comment, cdata):
    """
    Correction of the comment.
    """
    comment = ' ' + comment + ' '
    if not any(word in comment for word in ['pvt', 'private']):
        comment = comment.replace(' p ', ' pvt ')
    else:
        comment = comment.replace(' l ', ' ltd ')
    for i in replace_words.replacing_entities:
        comment = comment.replace(i, replace_words.replacing_entities[i])
    if not any(word in comment for word in ['hi tech ', 'info tech', 'auto tech', 'fast tech', 'micro tech']):
        comment = comment.replace(' tech ', ' technologies ')

    comment = correct(cdata.company_related_terms, comment)

    return comment
