possibilities = []
num = 9669
num = str(num)
first = ''
c = 0
for i in num:
    first = num
    if first[c] == 6:
        first[c] = 9
    else:
        first[c] = '6'
        c = c + 1

    first = int(first)
    possibilities.append(first)

possibilities = sorted(possibilities)
print (possibilities[len(possibilities)-1])
