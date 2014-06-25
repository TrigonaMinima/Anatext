import difflib

keywords = ['ltd', 'limited', 'films', 'p', 'broadcast', 'publications', 'pratidin', 'communication', 'online', 'realcon', 'realtors', 'trading', 'infra', 'aircon', 'airtel', 'pvt', 'systems', 'private',
            'infotech', 'radio', 'forms', 'electronics', 'electrical', 'services', 'solutions', 'technologies', 'corporation', 'merchandise', 'informatics', 'center',
            'multivision', 'cable', 'travels', 'telecommunications', 'security', 'international', 'studios', 'media', '.com', 'institute', 'associations', 'enterprise',
            'development', 'network', 'entertainment', 'research', 'properties', 'associates', 'public', 'company', 'project', 'hotels', 'builders', 'printers', 'industries',
            'motors', 'technologies', 'computers', 'advertising', 'developers', 'productions', 'residency', 'constructions', 'samachar', 'movers' 'works', 
            'hosiery', 'sons', 'boutique', 'textiles', 'tourism', 'engineering', 'club']

ignore = ['development limited', 'cement private limited', 'private limited', 'automobiles limited', 'company pvt. ltd.', 'india ltd',
          'and travels ltd.', 'pvt. ltd.', 'pvt ltd', 'pvt.ltd.', 'ltd.', 'ltd', 'communication', '']

junkKeywords = ['trans', 'to', 'of', 'cbin', 'ltd', 'tgs', 'from', 'baroda',
                'rtgs', 'trf', 'fav', 'frm', 'by', 'apl']

chars = ['/ioba', 'to:', 'a/c', '#', '-', '!', '@', '$', '%', '^', '&', '*', '0',
         '(', ')', '_', '+', '=', '`', '~', ';', ':', '/', ',', '.', '   ', '  ', '|']


def correct(words, comp):
    comp = comp.replace('&', ' and ')
    comp = comp.replace('ltd', ' ltd ')
    comp = comp.replace('pvt', ' pvt ')
    comp = comp.replace('limited', ' limited ')
    comp = comp.replace('entp', ' enterprise ')
    comp = comp.replace('engg', ' engineering ')
    for i in chars:
        comp = comp.replace(i, ' ')
    lis = comp.split()
    for i in lis:
        sugg = difflib.get_close_matches(i, words)
        if len(sugg):
            if difflib.SequenceMatcher(None, i, sugg[0]).ratio() > 0.800:
                comp = comp.replace(i, sugg[0])
    return comp


def checkin1(comp):
    for i in ignore:
        if i in comp:
            return comp[:-len(i) - 1]
    return comp

def checkin2(comp):
    for i in keywords:
        if i in comp:
            return comp[:-len(i) - 1]
    return comp
