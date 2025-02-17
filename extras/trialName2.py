# determines the name of individuals in a list of names with junk

106

import difflib

keywords = ['bhadra', 'dugar', 'sardar', 'gupta', 'rana', 'zafar', 'batori', 'singh', 'modi', 'wadhwa', 'chauhan', 'chaudhary', 'roy', 'khan', 'mittal', 'kumar',
             'sharma', 'jalil', 'sen', 'ghosh', 'paul', 'chakraborti', 'sarkar', 'shome', 'das', 'basu', 'deb', 'malik', 'saha', 'mukherjee', 'chitrakar', 'dey', 'bose', 'garg',
             'ghoshal', 'ali', 'majumdar', 'chattrejee', 'bhatiya', 'bhattacharya', 'pal', 'burman', 'banerjee', 'dutta', 'nath', 'bajaj', 'biswas', 'basak', 'sanyal',
             'bandyopadhyay', 'sinha', 'bhowmik', 'rakshit', 'shaw', 'mitra', 'bakshi', 'nandi', 'giri', 'mukhapadhay', 'upadhyay', 'samantha', 'kishore', 'mishra',
             'sadhu', 'ganguly', 'mahapatra', 'nag', 'dhar', 'kazi', 'hazra', 'ranjan', 'pramanik', 'abdullah', 'kapoor', 'prasad', 'lahri', 'tiwari', 'bhaskar', 'mandal',
             'katyal', 'adhikari', 'sahana', 'reza', 'patnaik', 'sengupta', 'kundal', 'mal', 'bhatt', 'bagan', 'lal', 'chourasia', 'prajapati', 'talukdar', 'thapa', 'chandra', 
             'ansari', 'karar', 'debnath', 'jafar', 'mani', 'pandey', 'joshi', 'fernandeS', 'ram', 'mathew', 'gomes', 'jaiswal', 'bagchi', 'bharadwaj', 'pandit', 'nayak', 
             'shaikh', 'kakkar', 'podder', 'patra', 'kundu', 'rodrigues', 'ray', 'deria', 'souza', 'dsouza', 'pancholi', 'tyagi', 'rastogi', 'pradhan', 'masud', 'trivedi', 
             'azad', 'alam', 'alangir', 'nanda', 'shukla', 'begum', 'hussain', 'rudra', 'paswan', 'rajput', 'yadav', 'thakur', 'bharti', 'rahman', 'sahu', 'islam', 'maheshwari', 
             'ahmed', 'haque', 'chettri', 'jain', 'halder', '']


chars = ['/ioba', 'to ', 'a/c', '#', '-', '!', '@', '$', '%', '^', '&', '*',
         '(', ')', '_', '+', '=', '`', '~', ';', ':', '/', ',', '.', '   ', '  ', '|']


def correct(words, comp):
    comp = comp.replace(' & ', ' and ')
    for i in chars:
        comp = comp.replace(i, ' ')
    lis = comp.split()
    for i in lis:
        sugg = difflib.get_close_matches(i, words)
        if len(sugg):
            if difflib.SequenceMatcher(None, i, sugg[0]).ratio() > 0.800:
                comp = comp.replace(i, sugg[0])
    return comp

a = ['DD-BHARTI DEVI DUGAR', 'RAJA  BHADRA', 'K N GUPTA', 'AJIR DAINIK BATORI', 'MANJU MODI', 'DD FAV SK. JALIL', 'DIPAK KR SEN', 'MILAN GHOSH',
     'DD FAV ELIZABETH MARY PAUL', 'MD ABDUL MUNIT TALUKDAR', 'TRF TO JAYANTA GHOSH/HDCCBL']

junkKeywords = ['trans', 'to', 'of', 'cbin', 'ltd', 'tgs', 'from', 'baroda',
                'rtgs', 'essel', 'trf', 'fav', 'dd']

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
