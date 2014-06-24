import difflib
import commons

def direct_mapping(sheet, comments, org, reducedAcc, orgAcc, mapping, lavensteinTrue, entities):
        count=0
        for i in comments:
                s=''
                if i != '':
                        if type(i) not in [int, float]:
                                i=commons.correct(lavensteinTrue, i.lower())
                                if 'salary' in i.lower():
                                        s='Salary'
                                        comments[count] = ''
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
                                                elif commons.checkin1(j.lower()) in i:
                                                        s=j
                                                        comments[count] = ''
                                                        break
                                                # elif 'saradha' in i: #j.lower() != 'saradha' 
                                                #         s='saradha realty india ltd'
                                                #         comments[count] = ''
                                                #         break
                                        if s=='' and 'saradha' in i:
                                                s='Saradha Realty India Ltd'
                                                comments[count] = ''
                                        if s=='':
                                                for j in commons.keywords:
                                                        if j in i:
                                                                entities.append()

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