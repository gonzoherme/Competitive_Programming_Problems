x = input()

side = int(x[0])
bottom = int(x[2])
flagstone = int(x[4])

flag_side = 0
flag_bottom = 0

new_flag_side = ''

if side % flagstone != 0:
    flag_side = (side/flagstone) + 1
    flag_side = str(flag_side)
    for i in flag_side:
        if i == '.':
            break
        new_flag_side = new_flag_side + i
                
else:
    flag_side = (side/flagstone)
    

new_flag_bottom = ''
if bottom % flagstone != 0:
    flag_bottom = (bottom/flagstone) + 1
    flag_bottom = str(flag_bottom)
    for i in flag_bottom:
        if i == '.':
            break
        new_flag_bottom = new_flag_bottom + i
        
else:
    flag_bottom = (bottom/flagstone)

print(int(new_flag_side) * int(new_flag_bottom))
    
