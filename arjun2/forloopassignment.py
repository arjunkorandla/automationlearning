num = "41,355,161,56516,611,115116"
clnum= ''
for i in range(0,len(num)):
    if num[i] in '123456789':
        clnum += num[i]
newnum = clnum
while  newnum not in clnum:
    print("yes it has")
    break
else:
    print("it doesnt")

print(newnum)
x=24
x+=1
print(x)
x-=6
print(x)
x/=2
print(x)
x**=2
print(x)
x*=2
print(x)
x%=3
print(x)
number: int = 5
multiplier = 8
answer = 0
for i in range(multiplier):
    multiplier*=number
answer=multiplier

number = 5
multiplier = 8
answer = 0



# add your loop after this comment
for i in range(10):
    answer += number

print(answer)
