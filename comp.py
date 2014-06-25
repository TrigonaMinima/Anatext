import difflib
import commons


def junk(string):
    for i in string:
        if i.isdigit():
            return True
    if string in commons.junkKeywords:
        return True
    return False


def entity_recog_org(i, count, entities, comments):
    s = ''
    temp = commons.correct(commons.keywords1, i)
    comments[count] = ''
    lis = temp.split()
    name = ''
    for j in commons.keywords1:
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
            name = name.replace(' tech ', ' technologies ')
            name = name.replace(' comm ', ' communication ')
            for j in entities:
                if name in j and len(j) >= name:
                    s = j
                elif len(j) < name:
                    entities.pop(j)
                    entities.append(name)
                    s = name
            if s == '':
                entities.append(name)
                s = name
            break
    return s

def entity_recog_name(i, count, entities, comments):
    s = ''
    temp = commons.correct(commons.keywords2, i)
    comments[count] = ''
    lis = temp.split()
    name = ''
    for j in commons.keywords2:
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
            for j in entities:
                if name in j and difflib.SequenceMatcher(None, j, name).ratio() > 0.800:
                    if len(j) >= name:
                        s = j
                    else:
                        entities.append(name)
                        s = name
            if s == '':
                entities.append(name)
                s = name
            break
    return s

def direct_mapping(sheet, comments, org, reducedAcc, orgAcc, mapping, lavensteinTrue, entities1, entities2, lavensteinTrue2, acc):
    count = 0
    for i in comments:
        s = ''
        if i != '':
            if type(i) not in [int, float]:
                i = commons.correct(lavensteinTrue+commons.normalWords, i.lower())
                if 'salary' in i:
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
                        s = entity_recog_org(i, count, entities1, comments)
                    if s == '':
                        s = entity_recog_name(i, count, entities2, comments)
                    if s == '' and ('chq' in i or 'cheque' in i):
                        s = 'Cheque'
                    if s == '' and 'neft' in i:
                        s = 'NEFT'
                    if s == '' and 'rtgs' in i:
                        s = 'RTGS'
                    if s == '' and ('clg' in i or 'clearing' in i):
                        s = 'Clearing'
                    if s == '' and 'trf to' in i and len(i.split()) > 2:
                        temp = i.split()[2]
                        if temp != '' and temp.isdigit():
                            temp = float(temp)
                            if temp in acc:
                                for j in orgAcc:
                                    if temp in orgAcc[j]:
                                        s = j
                                        comments[count] = ''
                                        break
                            else:
                                s = 'Unidentified account'
                    if s == '' and i.replace(' ', '').isdigit() and len(i.replace(' ', '')) > 6:
                        s = 'interconnected'
            else:
                for k in reducedAcc:
                    if float(i) == reducedAcc[k]:
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
