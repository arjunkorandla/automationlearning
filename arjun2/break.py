for i in range(0, 100, 7):
    print(i)
    if i>0 and i%11==0:
        break
    print("the requirement is satisfied")
else:
    print("the condiation is nt true")


for i in range(1,20):

    if i%3==0 or i%5==0:
        continue
    print(i)



