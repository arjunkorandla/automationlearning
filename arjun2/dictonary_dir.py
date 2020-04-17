locations = {1:"you are in the begining",
             2:"you are in the entrence",
             3:"you are started",
             4:"yu are in the midle",
             5:"you are almost done",
             6:"you achived"
             }

exits=[{"q":0},
       {"n":2,"s":3,"e":4,"w":6},
       {"w":1,"e":2,"n":6},
       {"e":2,"w":4,"n":5},
       {"s":2,"w":5,"n":3,"e":6}]

loc = 1
while True:
    avaliableexits = ""
    for dirctions in exits[loc].keys():
        avaliableexits+=dirctions + ","
    print(locations[loc])

    if loc==0:
        break
    dirctions = input("please enter the diactions:"+ avaliableexits).upper()
    print()
    if dirctions in exits[loc]:
        loc = exits[loc][dirctions]
    else:
        print(("you can not go in that diractions"))
