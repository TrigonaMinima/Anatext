import difflib

lavensteinTrue = [u'bengal', u'media', u'bhasank', u'foods', u'debika', u'dasgupta', u'global', u'khushi', u'landmark', u'cement', u'saradha', 
u'construction', u'garden', u'resort', u'and', u'hotel', u'housing', u'madhumita', u'sen', u'sudipta', u'mr.tarkeshwar', u'gupta', u'piyali', 
u'subhojit', u'priyanka', u'rose', u'capital', u'limited', u'abasan', u'agro', u'automobile', u'india', u'exports', u'financial', u'management', 
u'services', u'meditech', u'printing', u'publication', u'realty', u'shopping', u'mall', u'tours', u'travels', u'trading', u'communication', u'broadcast',
u'institute']


chars=['#', '-', '!', '@', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '`', '~', ';', ':', '/', ',', '.', '   ', '  ']
def correct(words, comp):
        comp = comp.lower()
        for i in chars:
                comp = comp.replace(i, ' ')
        lis = comp.split()
        for i in lis:
                sugg = difflib.get_close_matches(i, words)
                print i, sugg
                if len(sugg):
                        comp =  comp.replace(i, sugg[0])
        return comp

i = 'INSFTUTE'

i=correct(lavensteinTrue, i.lower())

s =  difflib.SequenceMatcher(None, "institute", "insftute")
print s.ratio()

print i