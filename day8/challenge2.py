
trees=[]
#with open("testinput.txt","r") as ifile:
with open("challengeinput.txt","r") as ifile:
    for line in ifile:
        trees.append(list(map(int,list(line.strip()))))

mask=[[0]*len(trees[0]) for i in range(len(trees))]
#print(trees)

for y in range(len(trees)):
    for x in range(len(trees[0])):
        result=1
        treesize=trees[y][x]
        # up
        t=0
        for i in range(y-1,-1,-1):
            t+=1
            if trees[i][x]>=treesize:
                break
        result*=t
        t=0
        # down
        for i in range(y+1,len(trees)):
            t+=1
            if trees[i][x]>=treesize:
                break
        result*=t
        t=0
        # left
        for i in range(x-1,-1,-1):
            t+=1
            if trees[y][i]>=treesize:
                break
        result*=t
        t=0
        # right
        for i in range(x+1,len(trees[0])):
            t+=1
            if trees[y][i]>=treesize:
                break
        result*=t
        mask[y][x]=result

print(max(max(m) for m in mask))

