for i in range(15):
    print("it starts  with{0:>2} and digit place of{0:>03b}".format(i))
    print("{0:>2} it has the range of {0:>02x}".format(i))
a=0x20
w=32
print(a+w)
print(0x56)#this is hexa value
print(0b010101000011111)#this is binary
powers=[]
for power in range(15, -1, -1):
    powers.append(2 ** power)
print(powers)
x=int(input("please enter the number:"))
printing= False
for power in powers:
    bit= x//power
    if bit !=0:
        printing = True
    if  printing:
        print(bit,end="")
    x %= power


