import difflib

keywords1 = ['ltd', 'limited', 'films', 'broadcast', 'publications', 'pratidin', 'communication', 'online', 'realcon', 'realtors', 'trading', 'infra', 'aircon', 'airtel', 'pvt', 
            'systems', 'private', 'engineering', 'infotech', 'radio', 'forms', 'electronics', 'electrical', 'solutions', 'technologies', 'corporation', 'merchandise', 
            'informatics', 'center', 'canvas', 'multivision', 'cable', 'travels', 'telecommunications', 'security', 'international', 'studios', 'media', '.com', 'institute', 
            'associations', 'enterprise', 'development', 'network', 'entertainment', 'research', 'properties', 'associates', 'public', 'company', 'project', 'hotels', 
            'builders', 'printers', 'industries', 'motors', 'technologies', 'computers', 'advertising', 'developers', 'productions', 'residency', 'constructions', 
            'samachar', 'movers' 'works', 'hosiery', 'sons', 'boutique', 'textiles', 'tourism', 'club', 'udyog', 'automotive', 'wireless', 'interiors', 'p', 'trust', 
            'federation', 'chemical'] #'services'

keywords2 = ['bhadra', 'dugar', 'sardar', 'gupta', 'rana', 'zafar', 'batori', 'singh', 'modi', 'wadhwa', 'chauhan', 'chaudhary', 'khan', 'mittal', 'kumar', 'garg',
            'sharma', 'jalil', 'sen', 'ghosh', 'paul', 'chakraborti', 'sarkar', 'shome', 'das', 'basu', 'deb', 'malik', 'saha', 'mukherjee', 'chitrakar', 'dey', 'bose',
            'ghoshal', 'ali', 'majumdar', 'chattrejee', 'bhatiya', 'bhattacharya', 'pal', 'roy', 'burman', 'banerjee', 'dutta', 'nath', 'bajaj', 'biswas', 'basak', 'sanyal',
            'bandyopadhyay', 'sinha', 'bhowmik', 'rakshit', 'shaw', 'mitra', 'bakshi', 'nandi', 'giri', 'mukhapadhay', 'upadhyay', 'samantha', 'kishore', 'mishra',
            'sadhu', 'ganguly', 'mahapatra', 'nag', 'lal', 'dhar', 'kazi', 'hazra', 'ranjan', 'pramanik', 'abdullah', 'kapoor', 'prasad', 'lahri', 'tiwari', 'bhaskar', 'mandal',
            'katyal', 'adhikari', 'sahana', 'reza', 'patnaik', 'sengupta', 'kundal']

a = ['TRF TO 912020004682824', 'TRF TO 910020000716073', 'TRF TO 910020015150475', 'TRF TO 910020000716073', 'TRF TO NEW FD', 
        'TRF TO 775010200000435', '10474/7341/10480/10452', '581/10474/7341/10452', 'to trf dmt sb 21908', 'PITAM T', 'ARINDAM']

b = [ 4205005730.0, 50901000019005.0, 910020016246803.0, 912020004682824.0, 775010200001243.0, 25010200019521.0, 
        912020004844488.0, 912020032727935.0, 228140000118.0, 912020050442610.0, 25010200019530.0, 910020031445470.0, 
        910020000716073.0, 775010200000435.0, 912020042210249.0, 912020042335636.0]

chars = ['/ioba', 'to:', 'a/c', '#', '-', '!', '@', '$', '%', '^', '&', '*',
         '(', ')', '_', '+', '=', '`', '~', ';', ':', '/', ',', '.', '   ', '  ', '|']


def correct(words, comp):
    comp = comp.replace('&', ' and ')
    comp = comp.replace('ltd', ' ltd ')
    comp = comp.replace('pvt', ' pvt ')
    comp = comp.replace('limited', ' limited ')
    comp = comp.replace('entp', ' enterprise ')
    comp = comp.replace('engg', ' engineering ')
    comp = comp.replace('trdg', ' trading ')
    comp = comp.replace('tech', ' technologies ')
    comp = comp.replace('commn', ' communication ')
    for i in chars:
        comp = comp.replace(i, ' ')
    lis = comp.split()
    for i in lis:
        sugg = difflib.get_close_matches(i, words)
        if len(sugg):
            if difflib.SequenceMatcher(None, i, sugg[0]).ratio() > 0.800:
                comp = comp.replace(i, sugg[0])
    return comp

for i in a:
    i = correct(keywords2+keywords1, i.lower())
    # print i
    s=''
    if 'trf to' in i and len(i.split()) > 2:
        temp = i.split()[2]
        if temp != '' and temp.isdigit():
            temp = float(temp)
            if temp in b:
                s = 'found'
            else:
                s='Unidentified account'
        else:
            s = '34534'
    if s=='' and i.replace(' ','').isdigit() and len(i.replace(' ', ''))>6 :
        # print i.replace(' ', '')
        # print 
        s = 'interconnected'

    print s, i