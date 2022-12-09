import math

head=[0,0]
tail=[0,0]
unique_positions = set()

def distance(pos1,pos2):
    return math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)

#with open("testinput.txt","r") as ifile:
with open("challengeinput.txt","r") as ifile:
    for line in ifile:
        move, dist = line.split()
        dist = int(dist)
        for i in range(dist):
            match move:
                case "U":
                    head[1] += 1
                case "D":
                    head[1] -= 1
                case "L":
                    head[0] -= 1
                case "R":
                    head[0] += 1

            if distance(head,tail) >=2:
                match move:
                    case "U":
                        tail[1] += 1
                        if head[0]!=tail[0]:
                            tail[0]=head[0]
                    case "D":
                        tail[1] -= 1
                        if head[0]!=tail[0]:
                            tail[0]=head[0]
                    case "L":
                        tail[0] -= 1
                        if head[1]!=tail[1]:
                            tail[1]=head[1]

                    case "R":
                        tail[0] += 1
                        if head[1]!=tail[1]:
                            tail[1]=head[1]
            #print(head,tail)
            unique_positions.add(tuple(tail))

print(len(unique_positions))
