a=1
b=6
for i in range (1,a+b):
    print(i)
x="we win"
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print(x[5])
q="hgvmhsvvcsdcb"
print(q[4:-2]+ q[0:-2])
n= "9,223;372:036 854,775;807"
print(n[1::4])
y=n[2::4]
print(y)

values = " ".join(char if char not in y else " " for char in n).split()





print([int(val) for val in values])

s1="he is"
s2="there is"
s3="it is"
print(s1+s2+s3)

