
def manhattan(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

pairs=[]
#with open("testinput.txt","r") as ifile:
with open("challengeinput.txt","r") as ifile:
    for line in ifile:
        sensor,beacon=line.split("x=")[1:3]
        sensorX,sensorY=sensor.split(", y=")
        sensorX=int(sensorX)
        sensorY=int(sensorY.split(": ")[0])
        beaconX,beaconY=beacon.split(", y=")
        beaconX=int(beaconX)
        beaconY=int(beaconY)
        pairs.append([sensorX,sensorY,beaconX,beaconY])

#Lets think about the problem, do we need to check every single point? 
#No, we just need to check the borders of the area that the beacons cover because the undetected
#beacon will be next to one of the borders! It will still be a lot of points but more doable than checking everything!
   #
  ###
 #####
###S###
 #####
  ###
   #

#minmax=(0,20)
minmax=(0,4000000)
edges=set()
for pair in pairs:
    sensorX,sensorY,beaconX,beaconY=pair
    d=manhattan(sensorX,sensorY,beaconX,beaconY)
    for i in range(d+1):
        #print(i)
        if (sensorX-i)>=minmax[0] and (sensorY-d-1+i)>=minmax[0]:
            edges.add((sensorX-i,sensorY-d-1+i))
        if (sensorX+i)<=minmax[1] and (sensorY+d+1-i)<=minmax[1]:
            edges.add((sensorX+i,sensorY+d+1-i))

copyEdges=edges.copy()
#visualize the edges, Only for testinput!!!!
# for y in range(20):
#     for x in range(20):
#         if (x,y)==(14,11):
#             print("S",end="")
#         elif (x,y) in edges:
#             print("#",end="")
#         else:
#             print(".",end="")
#     print()


# Now we have all the edges, lets check if they are in the area of one of the sensors, if so, remove them from the set
for pair in pairs:
    sensorX,sensorY,beaconX,beaconY=pair
    d=manhattan(sensorX,sensorY,beaconX,beaconY)
    removableEdges=[edge for edge in copyEdges if edge in edges and manhattan(edge[0],edge[1],sensorX,sensorY)<=d]
    for edge in removableEdges:
        edges.remove(edge)
    # for edge in copyEdges:
    #     if edge in edges:
    #         if manhattan(edge[0],edge[1],sensorX,sensorY)<=d:
    #             edges.remove(edge)
print(len(edges))
print(edges)
for edge in edges:
    print(edge[0]*4000000+edge[1])
#visualize the edges, Only for testinput!!!!
# for y in range(20):
#     for x in range(20):
#         if (x,y)==(14,11):
#             print("S",end="")
#         elif (x,y) in edges:
#             print("#",end="")
#         else:
#             print(".",end="")
#     print()
