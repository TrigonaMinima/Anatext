import difflib

chars=['/ioba', '#', '-', '!', '@', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '`', '~', ';', ':', '/', ',', '.', '   ', '  ']
def correct(words, comp):
        for i in chars:
                comp = comp.replace(i, ' ')
        lis = comp.split()
        for i in lis:
                sugg = difflib.get_close_matches(i, words)
                if len(sugg):
                        comp =  comp.replace(i, sugg[0])
        # if 'saradha' in comp:
        #         if 'tours' not in comp or 'cons' not in comp or 'pri' not in comp or 'gar' not in comp:
        #                 comp = comp.replace('saradha', 'saradha realty')
        return comp

ignore = ['development limited', 'private limited', 'cement private limited', 'automobiles limited', 'company pvt. ltd.', 'india ltd', 
'and travels ltd.', 'pvt. ltd.', 'pvt ltd', 'pvt.ltd.', 'ltd.', 'ltd', 'communication']
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
                                i=correct(lavensteinTrue, i.lower())
                                if 'salary' in i.lower():
                                        s='Salary'
                                        comments[count] = ''
                                # elif checkin2(i.lower()):
                                        # s='Interconnected'
                                        # comments[count] = ''
                                elif 'cash' in i or 'self' in i:
                                        s='Cash'
                                        comments[count] = ''
                                elif 'atm' in i or 'nfs' in i:
                                        s='ATM'
                                        comments[count] = ''
                                elif 'various' in i:
                                        s='Various'
                                        comments[count] = ''
                                elif s=='':
                                        for j in org:
                                                if  j.lower() in i:
                                                        s=j
                                                        comments[count] = ''
                                                        break
                                                elif checkin1(j.lower()) in i:
                                                        s=j
                                                        # print j
                                                        comments[count] = ''
                                                        break
                                                # elif 'saradha' in i: #j.lower() != 'saradha' 
                                                #         s='saradha realty india ltd'
                                                #         comments[count] = ''
                                                #         break
                                        if s=='' and 'saradha' in i:
                                                s='Saradha Realty India Ltd'
                                                comments[count] = ''
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