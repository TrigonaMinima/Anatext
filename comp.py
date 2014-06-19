import difflib

lavenstein = []
chars=['#', '-', '!', '@', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '`', '~', ';', ':', '/', ',', '.']
def correct(words, comp):
        temp = comp.lower()
        for i in chars:
                comp = comp.replace(i, ' ')
        lis = comp.split()
        for i in lis:
                sugg = difflib.get_close_matches(i, words)
                if len(sugg):
                        comp.replace(i, sugg[0])
        return comp

ignore = ['development limited', 'private limited', 'cement private limited', 'automobiles limited', 'company pvt. ltd.', 'india ltd', 
'pvt. ltd.', 'pvt ltd', 'pvt.ltd.', 'ltd.', 'ltd', 'communication']
def checkin1(comp):
        for i in ignore:
                if i in comp:
                        return comp[:-len(i)-1]
        return comp

cdcc = ['+', ';', '/']
def checkin2(comp):
        for i in cdcc:
                if i in comp:
                        return True
        return False

def direct_mapping(sheet, comments, org, reducedAcc, orgAcc, mapping, lavensteinTrue):
        count=0
        for i in comments:
                s=''
                if i != '':
                        if type(i) not in [int, float]:
                                i=correct(lavensteinTrue, i)
                                if 'salary' in i.lower():
                                        s='Salary'
                                        comments[count] = ''
                                # elif checkin2(i.lower()):
                                        # s='Interconnected'
                                        # comments[count] = ''
                                elif 'transfer' in i.lower():# or 'trfr' in i.lower(): #or 'trf' in i.lower() 
                                        s='Transfer'
                                        comments[count] = ''
                                elif 'various' in i.lower():
                                        s='Various'
                                        comments[count] = ''
                                elif s=='':
                                        for j in org:
                                                if  j.lower() in i.lower():
                                                        s=j
                                                        if j.lower() == 'saradha':
                                                                s='Saradha Realty India Ltd'
                                                        comments[count] = ''
                                                        break
                                                elif j.lower() != 'saradha' and checkin1(j.lower()) in i.lower():
                                                        s=j
                                                        # print j
                                                        comments[count] = ''
                                                        break
                        else:
                                for k in reducedAcc:
                                        if i == reducedAcc[k]:
                                                for j in orgAcc:
                                                        if reducedAcc[k] in orgAcc[j]:
                                                                s = j
                                                                comments[count] = ''
                                                                break
                # print s
                mapping[count] = s
                count+=1
                sheet.write('A'+str(count), s)
        print count