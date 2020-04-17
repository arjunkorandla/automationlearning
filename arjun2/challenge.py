# the line imit was excideed we cn doit by / this or makin it indendent.
ipaddress = input("please enter the ip address,please check the line limit before yu exicute so"
                   that it mat couse the run away the word limit:")
if ipaddress[-1] != ".":
    ipaddress += "."
segment = 1
segment_length = 0
# character=""
for character in ipaddress:
    if character == '.':
        print("segemnt has {} and characters {} in it".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1
    # if character!=0:
#   print("segemnt has {} and characters {} in it".format(segment,segment_length))
