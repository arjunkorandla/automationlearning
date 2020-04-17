for i in range(1,12):
    print("the counting value of: {:4}".format(i))
num= "123,156,23,86561,846"
for i in range(0,len(num)):
    print(num[i])

for i in range(0,len(num)):
    if num[i] in '0123456789':
        print(num[i])

for i in range(0,len(num)):
    if num[i] in '0123456789':
        print(num[i],end='')

cleanedNumber=''

for i in range(0,len(num)):
    if num[i] in '0123456789':
        cleanedNumber=cleanedNumber+num[i]
newNumber=int(cleanedNumber)
print(newNumber)
for chr in ("uhdsu","kduyagd","ajdg"):
    print("the char are" + chr)
for p in range(1,16,3):
    for q in range  (1,16,3):
        print("the num {1} is multipled by{0} and sol is{2}".format(p,q,p*q))

for f in range(1,100,3):
    print(f)

for p in range(1,16,3):
    for q in range  (1,16,4):
        print("the num {1} is multipled by{0} and sol is{2}".format(p,q,q*p))
que="""Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health"""
for char in que:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char,end='')

