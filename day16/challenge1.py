class valve:
    def __init__(self, rate:int, connections:list):
        self.rate=rate
        self.connections=connections
        self.distances=dict()

def dijkstra(valves,src,dest):
    distances={}
    previous={}
    for i in valves:
        distances[i]=float('inf')
        previous[i]=None
    
    distances[src]=0
    queue=set()
    queue.add(src)
    while queue:
        #print(queue)
        u=queue.pop()
        if u==dest:
            break
        for v in valves[u].connections:
            alt=distances[u]+1
            if alt<distances[v]:
                distances[v]=alt
                previous[v]=u
                queue.add(v)
    #print(distances)
    return distances[dest]


#All of the valves begin closed. You start at valve AA, but it must be damaged or jammed or something: its flow rate is 0, so there's no point in opening it. However, you could spend one minute moving to valve BB and another minute opening it; doing so would release pressure during the remaining 28 minutes at a flow rate of 13, a total eventual pressure release of 28 * 13 = 364. Then, you could spend your third minute moving to valve CC and your fourth minute opening it, providing an additional 26 minutes of eventual pressure release at a flow rate of 2, or 52 total pressure released by valve CC.

#Making your way through the tunnels like this, you could probably open many or all of the valves by the time 30 minutes have elapsed. However, you need to release as much pressure as possible, so you'll need to be methodical.        

valves=dict()
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        line=line.strip()
        name=line[6:8]
        connections=line.split("valves ")[1].split(", ") if "valves " in line else line.split("valve ")[1].split(", ")
        newvalve=valve(int(line.split("=")[1].split(";")[0]),connections)
        valves[name]=newvalve

# calculate distances to all other valves
for valve in valves:
    for valve2 in valves:
        if valve!=valve2 and valves[valve2].rate>0:
            valves[valve].distances[valve2]=dijkstra(valves,valve,valve2)

not0Valves=len([valve for valve in valves if valves[valve].rate>0])
print(not0Valves)

# every distance decreases the timer by the distance+1 (to open the valve)
# we don't need to revisit valves that are already open
# we want to have the highest pressure at the end of the time

maxPressure=0
def simulate(currentValve,time,p,deltap,valves,opened=[],pressures=[]):
    #print(time)
    #print(time,deltap)
    #print(pressures)
    global maxPressure
    if time<0:
        if p>maxPressure:
            maxPressure=p
            print("new max pressure: "+str(maxPressure))
            print(opened)
            print(len(pressures))
            print(pressures)
        return
    if not0Valves!=len(opened):
        #print(opened,valves[currentValve].distances)
        for valve,distance in valves[currentValve].distances.items():
            temp=deltap
            if valve not in opened:
                if distance>=time:
                    newPressure=p+deltap*(time)
                else:
                    newPressure=p+deltap*(distance+1)# + valves[valve].rate
                temp+=valves[valve].rate
                simulate(valve,time-distance-1,newPressure,temp,valves,opened+[valve],pressures+[deltap]*distance+[deltap+valves[valve].rate])
    else:
        p+=deltap*(time)
        #print("yay")
        #print(time,p,deltap,opened,pressures)
        if p>maxPressure:
            maxPressure=p
            print("new max pressure: "+str(maxPressure))
            print(opened)
            print(pressures)
            #exit()
        return
print(valves)
currentValve="AA"
simulate(currentValve,30,0,0,valves)
print(maxPressure)

#print([(valve,valves[valve].distances) for valve in valves])
