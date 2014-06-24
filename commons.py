keywords = ['limited', 'ltd', 'films', 'broadcast', 'pratidin', 'communication', 'realcon', 'realtors', 'trading', 'infra', 'aircon', 'airtel', 'pvt', 'systems', 'private',
'infotech', 'radio', 'forms', 'electronics', 'electrical', 'services', 'solutions', 'technologies', 'corporation', 'merchandise', 'informatics', 'center',
'multivision', 'cable', 'travels', 'telecommunications', 'security', 'international', 'studios', 'media', '.com', 'institute', 'associations', 'enterprise',
'development', 'network', 'entertainment', 'research', 'properties', 'associates', 'public', 'company']

ignore = ['development limited', 'private limited', 'cement private limited', 'automobiles limited', 'company pvt. ltd.', 'india ltd', 
'and travels ltd.', 'pvt. ltd.', 'pvt ltd', 'pvt.ltd.', 'ltd.', 'ltd', 'communication']

chars=['/ioba', 'to ', '#', '-', '!', '@', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '`', '~', ';', ':', '/', ',', '.', '   ', '  ', '|']

def correct(words, comp):
        for i in chars:
                comp = comp.replace(i, ' ')
        lis = comp.split()
        for i in lis:
                sugg = difflib.get_close_matches(i, words)
                if len(sugg):
                        # if difflib.SequenceMatcher(None, i, sugg[0]).ratio() > 0.800 :
                        comp =  comp.replace(i, sugg[0])
        return comp

def checkin1(comp):
        for i in ignore:
                if i in comp:
                        return comp[:-len(i)-1]
        return comp