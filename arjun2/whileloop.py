directions = ["ali", "west", "nrth", "south", "nw", "sw", "ew", "ne"]
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
    elif choose_directions == "west":
        print("you go to west")
        break

else:
    print("you have choosen the proper dir:")
