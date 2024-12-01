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
#with open("challengeinput.txt","r") as ifile:
with open("testinput.txt","r") as ifile:
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
def simulate(currentValves,steps,time,p,deltap,valves,opened=[],pressures=[]):
    global maxPressure
    print(currentValves,steps,time,p,deltap,opened,pressures)
    pressures.append(deltap)
    
    if time==0:
        p+=deltap
        if p>maxPressure:
            maxPressure=p
        return
    p+=deltap
    for i in range(len(steps)):
        if currentValves[i]!="AA":
            #print("decreasing",currentValves[i])
            steps[i]-=1
            #print(steps[i])
        # if step==0, we need to open the valve and add the rate to deltap
        if steps[i]<=0 and currentValves[i] !="AA":
            if currentValves[i] not in opened:
                #print("opening",currentValves[i])
                opened.append(currentValves[i])
                deltap+=valves[currentValves[i]].rate
        
    # if one ore more steps are 0, we need to go to a next valve, since we only have 2 entities, we can check this manually
    #print(steps,time,p)
    print(steps)
    if steps[0]==0:
        #print("yay")
        if not0Valves!=len(opened):
            for valve,d1 in valves[currentValves[0]].distances.items():
                if valve not in opened:
                    currentValves[0]=valve
                    if steps[1]==0:
                        if not0Valves!=len(opened):
                            for valve2,d2 in valves[currentValves[1]].distances.items():
                                print(opened,valve2)
                                if valve2 not in opened:
                                    currentValves[1]=valve2
                                    simulate(currentValves,[d1,d2],time-1,p,deltap,valves,opened)
                        else:
                            finishSim(time,p,deltap)
                    else:
                        simulate(currentValves,[d1,steps[1]],time-1,p,deltap,valves,opened)
        else:
            finishSim(time,p,deltap)
    elif steps[1]==0:
        if not0Valves!=len(opened):
            for valve,d in valves[currentValves[1]].distances.items():
                if valve not in opened:
                    currentValves[1]=valve
                    simulate(currentValves,[steps[0],d],time-1,p,deltap,valves,opened)
        else:
            finishSim(time,p,deltap)
    else:
        simulate(currentValves,steps,time-1,p,deltap,valves,opened)

def finishSim(time,p,deltap):
    global maxPressure
    p+=deltap*time
    if p>maxPressure:
        print("new max",p)
        maxPressure=p

#print([(valve,valves[valve].distances) for valve in valves])
print(valves["AA"].distances)
print(valves)
currentValve=["AA","AA"]
simulate(currentValve,[0,0],26,0,0,valves)
print(maxPressure)

