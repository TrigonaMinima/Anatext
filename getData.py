import commons

def input(sheet, curr_row, cd, org, orgAcc, acc, reducedAcc, comments, transaction, chq, trf, amt, lavensteinTrue):
        temp = 0
        # reads company name
        value1 = sheet.cell_value(curr_row, 0)
        if value1=='SARADHA':
                value1='Saradha Realty India Ltd'
        if value1 not in org:
                org.append(value1)
                orgAcc[value1] = []
                for i in commons.checkin1(value1.lower()).split():
                        if i not in lavensteinTrue:
                                lavensteinTrue.append(i)

        # reads account number
        value = sheet.cell_value(curr_row, 2)
        if value not in acc:
                acc.append(value)
                orgAcc[value1].append(value)
                temp = value%100000
                reducedAcc[str(temp).strip('0').strip('.')]=value

        # reads transaction comments
        value = sheet.cell_value(curr_row, 4)
        comments[curr_row] = value
        if type(value) in [float, int]:
                chq[curr_row] = value
        elif 'cd' in value.lower() or 'cc' in value.lower():
                cd[curr_row] = value
                comments[curr_row] = ''
        elif ''.join(x for x in value if x.isdigit()) in [float, int]:
                chq[curr_row] = value
        elif 'trf' or 'transfer' in value.lower():
                trf[curr_row] = value
                # comments[curr_row] = ''

        # reads credit and debit amount
        value = sheet.cell_value(curr_row, 6)
        value1 =  sheet.cell_value(curr_row, 7)
        amount=0
        if value == '':
                amount+=value1
        elif value1 == '':
                amount+=value
        else:
                amount+=value+value1
        amt[curr_row] = amount