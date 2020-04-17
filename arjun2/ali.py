directions = ["ali", "west", "nrth", "south", "nw", "sw", "ew", "ne","arjun","35.65"]
choose_directions = ""
while choose_directions not in directions:
    choose_directions = input("please choose proper directions:")
    if choose_directions not in directions:
        # TODO: write code... choose_directions   not in directions :
        print("youu have reached max limit")
        break

    elif choose_directions == "ali":
        print("you are belle pizza owner")
        break
    elif choose_directions == "arjun":
        print("you are a student")
        break
    elif choose_directions == "35.65" :
        print("it is mega special")
        break


else:
    print("you have choosen the proper dir:")

myjoinlist = ",".join(directions)
print(myjoinlist)
list(myjoinlist)
print(myjoinlist)
print(dict(directions))
