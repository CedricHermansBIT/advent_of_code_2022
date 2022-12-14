walls=[]
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        spline=line.strip().split(" -> ")
        for i in range(len(spline)-1):
            walls.append([eval("("+spline[i]+")"),eval("("+spline[i+1]+")")])

smallestX=min([x for coord in walls for x,y in coord])
largestX=max([x for coord in walls for x,y in coord])
largestY=max([y for coord in walls for x,y in coord])+2
dx=largestX-smallestX+1

def visualize(map):
    for line in map:
        print("".join(line))


map=[["."] * (dx) for i in range(largestY+1)]

for wall in walls:
    x1,y1=wall[0]
    x2,y2=wall[1]
    if x1==x2:
        if y2<y1:
            y1,y2=y2,y1
        for y in range(y1,y2+1):
            map[y][x1-smallestX]="#"
    elif y1==y2:
        if x2<x1:
            x1,x2=x2,x1
        print(x1,x2)
        for x in range(x1,x2+1):
            map[y1][x-smallestX]="#"

units=0
startX=500-smallestX
while map[0][startX]!="o":
    units+=1
    #print(units)
    s=[startX,0]
    while True:
        # check if we can move down
        #print(s)
        #print(largestY)
        if ((s[1]+1) < largestY) and map[s[1]+1][s[0]]==".":
            s[1]+=1
        # check if we are not on the edge
        elif s[0]-1 < 0:
            # add "." to the left
            for line in map:
                line.insert(0,".")
            dx+=1
            s[0]+=1
            startX+=1
        elif s[0]+1 >= dx:
            # add "." to the right
            for line in map:
                line.append(".")
            dx+=1
        # check if we can move left
        elif ((s[1]+1) < largestY) and map[s[1]+1][s[0]-1]=="." and map[s[1]+1][s[0]] in ["o","#"]:
            s[0]-=1
            s[1]+=1
        # check if we can move right
        elif ((s[1]+1) < largestY) and map[s[1]+1][s[0]+1]=="." and map[s[1]+1][s[0]] in ["o","#"]:
            s[0]+=1
            s[1]+=1
        # no valid moves
        else:
            map[s[1]][s[0]]="o"
            break
    visualize(map)
    # return to the top in terminal using escape sequence
    print("\033[{}A".format(largestY+2))

    
    #print(s)
print(units)
