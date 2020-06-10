s = 'PPALLL'
counter = 0
absent = 0
for i in s:
    if i == 'A':
        absent = absent + 1


    if i == 'L' and s[counter + 1] == 'L' and s[counter + 2] :
        break
        print('False')
    counter = counter  + 1
    
        
        

if absent > 1:
    print('False')
else:
    print('True')
