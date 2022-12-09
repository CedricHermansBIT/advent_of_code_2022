import math

knots=[[0,0] for i in range(10)]
unique_positions = set()
moves=[None for i in range(10)]

def distance(pos1,pos2):
    return math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)

def visualize(knots):
    for y in range(min(knots,key=lambda x:x[1])[1],max(knots,key=lambda x:x[1])[1] + 1):
        for x in range(min(knots,key=lambda x:x[0])[0],max(knots,key=lambda x:x[0])[0] + 1):
            if [x,y] in knots:
                print(knots.index([x,y]),end="")
            else:
                print(".",end="")
        print()
    print()


#with open("testinput2.txt","r") as ifile:
with open("challengeinput.txt","r") as ifile:
    for line in ifile:
        print(line)
        move, dist = line.split()
        moves[0]=move
        dist = int(dist)
        for i in range(dist):
            match move:
                case "U":
                    knots[0][1] -= 1
                case "D":
                    knots[0][1] += 1
                case "L":
                    knots[0][0] -= 1
                case "R":
                    knots[0][0] += 1
            for j in range(1,len(knots)):
                if (d:=distance(knots[j-1],knots[j])) >=2:
                    #print(d)
                    match moves[j-1]:
                        case "U":
                            knots[j][1] -= 1
                            moves[j]=moves[j-1]
                            if knots[j-1][0]>knots[j][0]:
                                moves[j]="R"
                                knots[j][0]+=1
                            elif knots[j-1][0]<knots[j][0]:
                                moves[j]="L"
                                knots[j][0]-=1
                        case "D":
                            knots[j][1] += 1
                            moves[j]=moves[j-1]
                            if knots[j-1][0]>knots[j][0]:
                                knots[j][0]+=1
                                moves[j]="R"
                            elif knots[j-1][0]<knots[j][0]:
                                knots[j][0]-=1
                                moves[j]="L"
                        case "L":
                            knots[j][0] -= 1
                            moves[j]=moves[j-1]
                            if knots[j-1][1]<knots[j][1]:
                                knots[j][1]-=1
                                moves[j]="U"
                            elif knots[j-1][1]>knots[j][1]:
                                knots[j][1]+=1
                                moves[j]="D"
                        case "R":
                            knots[j][0] += 1
                            moves[j]=moves[j-1]
                            if knots[j-1][1]<knots[j][1]:
                                knots[j][1]-=1
                                moves[j]="U"
                            elif knots[j-1][1]>knots[j][1]:
                                knots[j][1]+=1
                                moves[j]="D"
            unique_positions.add(tuple(knots[-1]))
        #visualize(knots)

visualize(list(unique_positions))
print(len(unique_positions))
