
def check_acc(row, string, reducedAcc, orgAcc, mapping, sheet):
        if len(string) < 3 :
                sheet.write('A'+str(row+1), '')
                mapping[row] = ''
        elif len(string) in range(3,6):
                for i in reducedAcc:
                        if string in i:
                                for j in orgAcc:
                                        if reducedAcc[i] in orgAcc[j]:
                                                mapping[row] = j
                                                sheet.write('A'+str(row+1), j)
        else:
                mapping[row] = "Interconnected"
                sheet.write('A'+str(row+1), 'Interconnected')
        return 1


def accnum(sheet, cd, reducedAcc, orgAcc, mapping):
        count=0
        for i in cd:
                # print s
                if 'various' not in cd[i].lower():
                        s=''
                        s=''.join(x for x in cd[i] if x.isdigit())
                        count += check_acc(i, s, reducedAcc, orgAcc, mapping, sheet)
                else:
                        mapping[i] = "Various"
                        sheet.write('A'+str(i+1), 'Various')
                        count += 1
        print count