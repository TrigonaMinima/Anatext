chars=['#', '-', '!', '@', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '`', '~', ';', ':', '/', ',', '.', '   ', '  ']
frequency = {}
frequency[0] =  ''

def freq():
        count = 1
        for i in comments:
                if i != '':
                        for j in chars:
                                i = i.replace(j, ' ')
                        lis = i.split()
                        for j in lis:
                                if j in frequency:
                                        frequency[j][0] += 1
                                        frequency[j][1].append(str(count))
                                else:
                                        frequency[j][0] = 0
                                        frequency[j][1] = []
                                        frequency[j][1].append(str(count))
