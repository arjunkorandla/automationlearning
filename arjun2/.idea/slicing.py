parrot = "are you learning python!"
print(parrot)
print(parrot[:6])
print(parrot[6:])

print(parrot[:6]  + parrot[6:])
print(parrot[0:8:2])
print(parrot[0:8:3])

a="abcdefghijklmnopqrstuvwxyz"
print(a[16:13:-1])
print(a[5::-1])
print(a[:-9:-1])
print(a[:-9:-2])
print(a[-24:-12])
print("there are {0} states in india {1},{2},{3},{4},{5}".format(28,"tg","dl","up","ap","kw"))

print("""jan:{1}
feb:{2}
mar:{3}
apr:{1}
may:{2}
june:{3}
july:{3}
aug:{2}
sept:{1}
oct:{1}
nov:{3}
dec:{1}""".format(28,29,30,31))
print("'there are {0} months they are :'jan:{1},feb:{2},mar:{3},apr:{1},may:{2},june:{3},july:{2},aug:{1},sept:{3},oct:{2},nov:{1},dec:{3}".format(12,29,30,31))
print("pi value is approxmatily {0:12} : ".format(22/7))
print("pi value is approxmatily {0:12f} : ".format(22/7))
print("pi value is approxmatily {0:12.50f} : ".format(22/7))
print("pi value is approxmatily {0:<12} : ".format(22/7))
print("pi value is approxmatily {0:50} : ".format(22/7))
print("pi value is approxmatily {0:12.54f} : ".format(22/7))
for i in range(1,13):
    print("number is {} squared {}, is cubed {}, is fourth power {}:".format(i,i**2,i**3,i**4))

age=24
name="arjun"
print(name   + f"my name is {name} and my age is{age}")
print("my age is %d and my name is %s :" %(age, name) )
pi=(22/7)
print("the value of pi %54.12f is" %pi)
