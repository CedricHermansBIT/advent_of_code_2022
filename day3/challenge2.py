score=0
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=ifile.read().splitlines()
    for i in range(0,len(lines),3):
        overlap = (set(lines[i])&set(lines[i+1])&set(lines[i+2])).pop()
        score += ord(overlap)-64+26 if ord(overlap)<97 else ord(overlap)-96
    print(score)
