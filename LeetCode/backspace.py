def backspaceCompare(S: str, T: str) -> bool:
    a = []
    b=[]
    for i in S:
        a.append(i)
    for i in T:
        b.append(i)
        
    deletes = 0
    counter = len(a)-1
    while counter >= 0:
        print(a)
        if a[counter] == '#':
            deletes = deletes + 1
            
        elif a[counter] is not '#' and deletes > 0:
            a.remove(a[counter])
            deletes = deletes - 1
            
        counter = counter - 1


    sol1 = []
    for i in a:
        if i is not '#':
            sol1.append(i)

    deletes = 0
    counter = len(b)-1
    while counter >= 0:
        if b[counter] == '#':
            deletes = deletes + 1
            
        if b[counter] is not '#' and deletes>0:
            b.remove(b[counter])
            deletes = deletes - 1
            
        counter = counter - 1
    

    sol2 = []
    for i in b:
        if i is not '#':
            sol2.append(i)
            
    print(a)
    print(b)
                
    if sol1 == sol2:
        return True
    else:
        return False
backspaceCompare("du###vu##v#fbtu","du###vu##v##fbtu")
