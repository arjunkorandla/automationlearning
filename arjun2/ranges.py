my_list=range(10)
print(my_list)
odd = list(range(1,10,2))
even = list(range(0,10,2))
print(sorted(odd + even))

smalldecimals =range(0, 60, 2)
my_indexing = smalldecimals[::4]
print("afterindexing{}".format(my_indexing))
print(my_indexing)
print(my_indexing.index(16))

fives=range(0,500,5)
x=int(input("please enter the num: "))
if x in fives:
    print("you have entered the currect num {}".format(x))
else:
    print("you have entered incurrect num")



#fives=range(0,500,5)
#x=int(input("please enter the num: "))
#for x in fives:
 #   print(x)
print(fives == range(0,500,5))

r = range(0,100)
print(r[::-2])
for i in r[::-2]:
    print(i)
print(range(0,100)[::-2]==range(99, -1, -2))





