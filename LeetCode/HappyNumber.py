n = input("Check if it's a happy number: ")
k = n
database = []
solution = ''

while True:
                
    n = str(k)
    k=0
    
    for i in n:
        k = k + int(i)**2

    if k in database:
        solution = 'false'
        break
    database.append(k)
    
            
    if k == 1:
        solution = 'true'
        break                                                           
            

print(solution)

