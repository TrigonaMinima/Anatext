# determines the name of companies in a list of companies having
# individual companies in one list item


import difflib

keywords = ['ltd', 'limited', 'films', 'broadcast', 'publications', 'pratidin', 'communication', 'online', 'realcon', 'realtors', 'trading', 'infra', 'aircon', 'airtel', 'pvt', 'systems', 'private',
            'infotech', 'radio', 'forms', 'electronics', 'electrical', 'services', 'solutions', 'technologies', 'corporation', 'merchandise', 'informatics', 'center',
            'multivision', 'cable', 'travels', 'telecommunications', 'security', 'international', 'studios', 'media', '.com', 'institute', 'associations', 'enterprise',
            'development', 'network', 'entertainment', 'research', 'properties', 'associates', 'public', 'company', 'project', 'hotels', 'builders', 'printers', 'industries',
            'motors', 'technologies', 'computers', 'advertising', 'developers', 'productions', 'residency', 'constructions', 'samachar', 'movers' 'works', 
            'hosiery', 'sons', 'boutique', 'textiles', 'tourism', 'engineering', 'club', 'p']


chars = ['/ioba', 'to ', 'a/c', '#', '-', '!', '@', '$', '%', '^', '&', '*',
         '(', ')', '_', '+', '=', '`', '~', ';', ':', '/', ',', '.', '   ', '  ', '|', '\\']


def correct(words, comp):
    comp = comp.replace('&', ' and ')
    comp = comp.replace('ltd', ' ltd ')
    comp = comp.replace('pvt', ' pvt ')
    comp = comp.replace('limited', ' limited ')
    comp = comp.replace('entp', ' enterprise ')
    comp = comp.replace('engg', ' engineering ')
    comp = comp.replace('trdg', ' trading ')
    for i in chars:
        comp = comp.replace(i, ' ')
    lis = comp.split()
    for i in lis:
        sugg = difflib.get_close_matches(i, words)
        if len(sugg):
            if difflib.SequenceMatcher(None, i, sugg[0]).ratio() > 0.800:
                comp = comp.replace(i, sugg[0])
    return comp

a = ['FT-02062320000563-SIVA COMPULINK LIMITED', 'I/W CHQ RETURN-TRANS-HI TECH TRADERS PVT',
     'UTR#CITIH10090501185-XENITIS INFOTECH LTD.-CA-19670503555841-UCO BANK-KOLKATA-KOLKATA',
     'MCU-|UCBA00019 RTGS :SIVA COMPULINK   LIMITED/HDFC ', 'FT-02062320000553-HI TECH HOUSING PROJEC',
     'Trfd from A/c of BENGAL MEDIA PVT LTD to A/c of AAMAR PC COMPUTERS P 09-APR-2010',
     'UTR#CITIH10083500313- NET WORK CREDIT CORPORATION-CA-253010200012014-AXIS BANK-KOLKATA-RASH BEHARI AV',
     'UTR#CITIH09168500626-XENITIS INFOTECH LTD-CA-62001203656-STATE BANK OF HYDERABAD-KOLKATA-BRABOURNE',
     'R SHERWOOD HOTELS ', 'SIVA COMPULINK   LTD', 'ESSEL SHYAM TECHNOLOGIES', 'ESSEL SHYAM TECH LTD',
     'UTR#CITIH10125501060-GLOBAL AUTOMOBILES LTD.-CA-2924-INDIAN OVERSEAS BANK-KOLKATA-BALLYGUNGE',
     'RTGS :UNIQUE BUILDERS/UTIB SURYAMUKHI   GIC  LTD', 'UTR#CITIH10069500734-BIGBOSS EXIM LTD.-CA-33105136842-STANDARD CHARTERED',
     'BANK-KOLKATA-19 N.S ROAD-|S UTIBH09087009101-RTGS-ESSEL SHYAM TECHNOLOGIES LTD', 'RTGS :SIVA COMPULINK   LTD',
     'ANUBHUTI PRINTERS AT RAIPUR-CIVIL LINES MAA MAHAMAYA', '/HDFC TRF TO SHERWOOD HOTELS & RESORTS PVT LTD',
     'FT-02062050000087-SIVA INDUSTRIES AND HO', 'TRFR TO:SARADHA  REALTY  INDIA LTD', 'SARADHA AGRO DEVELOPMENT LTD UTR',
     'UTR#CITIH10040500820-BHOMIYA VYAPAAR PVT LTD-CA-060102', 'UTIBH11257044509-IMPULSE PRODUCTION PVT.LTD',
     'IMPULSE PRODUCTION P LTD', 'RTGS :SIVA COMPULINK   LTD/HDFC RTGS', ':GNN INDIA PVT LTD/CBIN', 'MANTAHAN BROADBAND SERVICES P RTGS',
     ':AMBICA PAPER  PVT LTD/VYSA', ':AMBICA PAPER  PVT LTD/VYSAPO', 'FAV INTELLIGENT INFRASTRUCTURE LIMITED AT KOLKATTA-KANKURGACHIRTGS',
     'IBKLH10132008325/SARADHA  REALTY INDIA LTD', 'TO BASEVA DISTRIBUTORS PVT LTD', 'SURYAMUKHI   GIC  LTD', 
     'IDBI BANK TO DHARA VINIMAY PVT LTD', 'IDBI BANK TO THIRD EYE COMMERCIAL P LTD,BANK OF BARODA', 'broadcast worldwide ltd',
     'EKDIN MEDIA PVT LTD', 'broadcast worldwide', 'LEXUS MOTORS', 'UTIBH11258069093-IMPULSE PRODUCTION PVT.LTD',
     'I/W CHQ RETURN-TRANS-HI TECH TRADERS PVT', 'FT-02062320000553-HI TECH HOUSING PROJEC', 'SHERWOOD HOTELS', 'ANUBHUTI PRINTRES', 
     'UTR#CITIH10090501185-XENITIS INFOTECH LTD.-CA-19670503555841-UCO BANK-KOLKATA-KOLKATA MCU-|UCBA00019',
     'UTR#CITIH10089501023-GLOBAL AUTOMOBILES LTD-CA-2924-INDIAN OVERSEAS BANK-KOLKATA-BALLYGUNGE - KOLKAT', 'TIJ TRDING', 
     'TO G A P LTD', 'TO V ENTERPRISES', 'UTIBH09010004858-RTGS-ESSEL SHYAM COMMUNICATION LI', 'RTGS :GNN INDIA PVT LTD/CBIN',
     'TO BEEVAS ADVERTISING', 'BROADCAST WORLD', 'RTGS :AMBICA PAPER  PVT LTD/VYSA', 'TO GITA TRADING CO', 'TO L.C.MARGIN/COMM',
     'UTR#CITIH10084501458-BAHAR SUPPLIERS PVT.LTD.-CA-00080340025090-HDFC BANK-KOLKATA-KOLKATA - STEPHEN',
     'SANGBAD PRATIDIN', 'armen properties', 'S.K.DEVELOPERS', 'TRF TO UNIQUE BUILDERS', 'IMPULSE PRODUCTION PVT LTD', 
     'TRF TO SHERWOOD HOTELS & RESORTS PVT LTD', 'jaita estate pvtltd', 'AXISF12279037022-ANUBHUTI PRINTERS AND PUBLICATION',
     '151466 SOUTH INDIAN BANK LTD.', 'AXISF13035086177-INDIAN HOTEL COMPANY LIMITED', 
     'TRF TO SHERWOOD HOTELS & RESORTS PVT LTD', 'IMPLULSE PRODCDTION P LTD', 'P U ENTP', 'WIR & WIRELESS', 'TO BROADCAST WW', 
     'TO BROADCAST WORLDWIDE LTD', '\TO RVRE&C LTD', 'WDL TFR   WEALTHMAX FINANC IDIBH10005127264']

junkKeywords = ['trans', 'to', 'of', 'cbin', 'ltd', 'tgs', 'from', 'baroda',
                'rtgs', 'essel', 'trf', 'fav']

print len(a)


def junk(string):
    for i in string:
        if i.isdigit():
            return True
    if string in junkKeywords:
        return True
    return False

count = 0
for i in a:
    i = correct(keywords, i.lower())
    # print i
    lis = i.split()
    name = ''
    for j in keywords:
        if j in lis:
            k = lis.index(j) - 1
            name = j
            while k >= 0:
                if not junk(lis[k]):
                    name = lis[k] + ' ' + name
                else:
                    # i = i.replace(lis[k], '')
                    break
                k -= 1
            print name
            count += 1
            break
print count
