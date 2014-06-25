import difflib
import commons


def junk(string):
    for i in string:
        if i.isdigit():
            return True
    if string in commons.junkKeywords:
        return True
    return False


def direct_mapping(sheet, comments, org, reducedAcc, orgAcc, mapping, lavensteinTrue, entities, lavensteinTrue2):
    count = 0
    for i in comments:
        s = ''
        if i != '':
            if type(i) not in [int, float]:
                i = commons.correct(lavensteinTrue, i.lower())
                if 'salary' in i.lower():
                    s = 'Salary'
                    comments[count] = ''
                elif 'cash' in i or 'self' in i:
                    s = 'Cash'
                    comments[count] = ''
                elif 'atm' in i or 'nfs' in i:
                    s = 'ATM'
                    comments[count] = ''
                elif 'various' in i:
                    s = 'Various'
                    comments[count] = ''
                elif s == '':
                    for j in org:
                        if j.lower() in i:
                            s = j
                            comments[count] = ''
                            break
                        elif commons.checkin1(j.lower()) in i:
                            s = j
                            comments[count] = ''
                            break
                    if s == '' and 'saradha' in i:
                        s = 'Saradha Realty India Ltd'
                        comments[count] = ''
                    if s == '':
                        temp = commons.correct(commons.keywords, i)
                        comments[count] = ''
                        lis = temp.split()
                        name = ''
                        for j in commons.keywords:
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
                                name = name.replace(' p ', ' private ')
                                name = name.replace(' i ', ' india ')
                                name = name.replace(' pv ', ' pvt ')
                                name = name.replace(' comm ', ' communication ')
                                entities.append(name)
                                s = name
                                # for i in commons.checkin1(name).split():
                                #         if i not in lavensteinTrue2:
                                #                 lavensteinTrue2.append(i)
                                break
                    if s=='' and ('chq' in i or 'cheque' in i):
                        s = 'Cheque'
                    if s=='' and 'neft' in i:
                        s = 'NEFT'
                    if s=='' and 'rtgs' in i:
                        s = 'RTGS'
                    if s=='' and ('clg' in i or 'clearing' in i):
                        s = 'Clearing'
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
        count += 1
        sheet.write('A' + str(count), s)
    print count
