def dijkstra(maze,src,dest):
    distances={}
    previous={}
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            distances[(i,j)]=float('inf')
            previous[(i,j)]=None
    
    distances[src]=0
    queue=set()
    queue.add(src)
    while queue:
        print(queue)
        u=queue.pop()
        if u==dest:
            break
        for v in neighbors(maze,u):
            alt=distances[u]+1
            if alt<distances[v]:
                distances[v]=alt
                previous[v]=u
                queue.add(v)
    #print(distances)
    return distances[dest]

def neighbors(maze,u):
    y,x=u
    neighbors=[]
    if y>0 and ((ord(maze[y-1][x])-ord(maze[y][x]))<=1):
        neighbors.append((y-1,x))
    if y<len(maze)-1 and ((ord(maze[y+1][x])-ord(maze[y][x]))<=1):
        neighbors.append((y+1,x))
    if x>0 and ((ord(maze[y][x-1])-ord(maze[y][x]))<=1):
        neighbors.append((y,x-1))
    if x<len(maze[y])-1 and ((ord(maze[y][x+1])-ord(maze[y][x]))<=1):
        neighbors.append((y,x+1))
    return neighbors

def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j]=='S':
                return (i,j)
    return None

def find_end(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j]=='E':
                return (i,j)
    return None

    
maze=[]
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        maze.append(list(line.strip()))
start=find_start(maze)
end=find_end(maze)
maze[start[0]][start[1]]='a'
maze[end[0]][end[1]]='z'
print(dijkstra(maze,start,end))

