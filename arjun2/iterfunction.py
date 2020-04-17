num="123456789"
#for char in num:
 #   print(char)
myiter = iter(num)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
for char in iter(num):
    print(char)

week=["monday","tuesday","wednesday","thursday","friday","sat","sun"]
myiterator=iter(week)
for i in range(0, len(week)):
    my_next=(next(myiterator))
    print(my_next)
print((myiterator))
print(myiterator)

