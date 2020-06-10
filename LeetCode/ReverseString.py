s = 'hello'

length = len(s) -1
final = ''
j = ''
for i in s:
    j = s[length]
    final = final + j
    length = length -1
            
s = final

print(s)
