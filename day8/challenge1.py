
def check_line(line,mask,y,reversed=False):
    minsize=-1
    for x,tree in enumerate(line):
        if minsize<tree:
            if reversed:
                mask[y][len(line)-x-1]=1
            else:
                mask[y][x]=1
            minsize=tree
    return mask

def check_column(column,mask,x, reversed=False):
    minsize=-1
    for y,tree in enumerate(column):
        if minsize<tree:
            if reversed:
                mask[len(column)-y-1][x]=1
            else:
                mask[y][x]=1
            minsize=tree
    return mask


trees=[]
#with open("testinput.txt","r") as ifile:
with open("challengeinput.txt","r") as ifile:
    for line in ifile:
        trees.append(list(map(int,list(line.strip()))))

mask=[[0]*len(trees[0]) for i in range(len(trees))]
for y,line in enumerate(trees):
    #rows left to right
    mask=check_line(line,mask,y)
    #rows right to left
    line.reverse()
    mask=check_line(line,mask,y,reversed=True)
    #reset line
    line.reverse()

#swap rows and columns

trees=list(map(list,zip(*trees)))
for x,column in enumerate(trees):
    #columns top to bottom
    mask=check_column(column,mask,x)
    #columns bottom to top
    column.reverse()
    mask=check_column(column,mask,x,reversed=True)
print(sum(sum(m) for m in mask))
