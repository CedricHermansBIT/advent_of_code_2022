priorities=0
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile.read().splitlines():
        overlap = (set(line[0:len(line)//2])&set(line[len(line)//2:])).pop()
        priorities += ord(overlap)-64+26 if ord(overlap)<97 else ord(overlap)-96
    print(priorities)
