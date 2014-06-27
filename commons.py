import difflib

keywords1 = ['ltd', 'limited', 'films', 'broadcast', 'publications', 'pratidin', 'communication', 'online', 'realcon', 'realtors', 'trading', 'infra', 'aircon', 'airtel', 'pvt', 
            'systems', 'private', 'engineering', 'infotech', 'radio', 'forms', 'electronics', 'electrical', 'solutions', 'technologies', 'corporation', 'merchandise', 
            'informatics', 'center', 'canvas', 'multivision', 'cable', 'travels', 'telecommunications', 'security', 'international', 'studios', 'media', '.com', 'institute', 
            'associations', 'enterprise', 'development', 'network', 'entertainment', 'research', 'properties', 'associates', 'public', 'company', 'project', 'hotels', 
            'builders', 'printers', 'industries', 'motors', 'technologies', 'computers', 'advertising', 'developers', 'productions', 'residency', 'constructions', 
            'samachar', 'movers' 'works', 'hosiery', 'sons', 'boutique', 'textiles', 'tourism', 'club', 'udyog', 'automotive', 'wireless', 'interiors', 'p', 'trust', 'commercial',
            'federation', 'chemical', 'publishers', 'co', 'market', 'vyapaar', 'engineers'] #'services'

keywords2 = ['bhadra', 'dugar', 'sardar', 'gupta', 'rana', 'zafar', 'batori', 'singh', 'modi', 'wadhwa', 'chauhan', 'chaudhary', 'khan', 'mittal', 'kumar', 'garg',
            'sharma', 'jalil', 'sen', 'ghosh', 'paul', 'chakraborti', 'sarkar', 'shome', 'das', 'basu', 'deb', 'malik', 'saha', 'mukherjee', 'chitrakar', 'dey', 'bose',
            'ghoshal', 'ali', 'majumdar', 'chattrejee', 'bhatiya', 'bhattacharya', 'pal', 'roy', 'burman', 'banerjee', 'dutta', 'nath', 'bajaj', 'biswas', 'basak', 'sanyal',
            'bandyopadhyay', 'sinha', 'bhowmik', 'rakshit', 'shaw', 'mitra', 'bakshi', 'nandi', 'giri', 'mukhapadhay', 'upadhyay', 'samantha', 'kishore', 'mishra',
            'sadhu', 'ganguly', 'mahapatra', 'nag', 'lal', 'dhar', 'kazi', 'hazra', 'ranjan', 'pramanik', 'abdullah', 'kapoor', 'prasad', 'lahri', 'tiwari', 'bhaskar', 'mandal',
            'katyal', 'adhikari', 'sahana', 'reza', 'patnaik', 'sengupta', 'kundal', 'mal', 'bhatt']

normalWords = ['salary']

ignore = ['development limited', 'private limited', 'automobiles limited', 'company pvt. ltd.', 'india ltd',
          'and travels ltd.', 'pvt. ltd.', 'pvt ltd', 'pvt.ltd.', 'ltd.', 'ltd', 'communication', '']   #'cement private limited', 

junkKeywords = ['trans', 'to', 'of', 'cbin', 'ltd', 'tgs', 'from', 'baroda', 'micr', 'rfr', 'no',
                'rtgs', 'trf', 'fav', 'frm', 'by', 'apl', 'favouring', 'trfr', 'gs', 'cl', 'wd']

chars = ['/ioba', 'to:', 'a/c', '#', '-', '!', '@', '$', '%', '^', '&', '*',
         '(', ')', '_', '+', '=', '`', '~', ';', ':', '/', ',', '.', '   ', '  ', '|']


def correct(words, comp):
    comp = comp.replace('&', ' and ')
    comp = comp.replace('ltd', ' ltd ')
    comp = comp.replace('pvt', ' pvt ')
    comp = comp.replace('prop', ' properties ')
    comp = comp.replace('limited', ' limited ')
    comp = comp.replace('entp', ' enterprise ')
    comp = comp.replace('engg', ' engineering ')
    comp = comp.replace('trdg', ' trading ')
    comp = comp.replace('commn', ' communication ')
    comp = comp.replace('mkt ', ' market ')
    comp = comp.replace('pub', ' publications ')
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
    for i in keywords1+keywords2:
        if i in comp:
            return comp[:-len(i) - 1]
    return comp
