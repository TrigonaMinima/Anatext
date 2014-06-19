def cash(transaction, mapping, comments, sheet):
        for i in transaction:
                if transaction[i].lower() in ['cash', 'csh']:
                        if mapping[i] == '':
                                sheet.write('A'+str(i+1), 'Cash')
                                comments[i] = ''
                        else:
                                sheet.write('A'+str(i+1), 'Cash - '+mapping[i])

