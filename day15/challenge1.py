
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
        pairs.append((sensorX,sensorY,beaconX,beaconY))
        
#inspectLine=10
inspectLine=2000000
noBeacons=set()
for pair in pairs:
    sensorX,sensorY,beaconX,beaconY=pair
    d=manhattan(sensorX,sensorY,beaconX,beaconY)
    currentX=sensorX
    while d>=manhattan(sensorX,sensorY,currentX,inspectLine):
        #print(manhattan(sensorX,sensorY,currentX,inspectLine))
        noBeacons.add((currentX,inspectLine))
        currentX-=1
    currentX=sensorX+1
    while d>=manhattan(sensorX,sensorY,currentX,inspectLine):
        noBeacons.add((currentX,inspectLine))
        currentX+=1
    if beaconY==inspectLine:
        noBeacons.remove((beaconX,beaconY))

print(len(noBeacons))
        