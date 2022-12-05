crates=[]
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        if '[' in line:
            spline=line.replace("\n","").replace('[',' ').replace(']',' ').replace('    ', '-').replace('   ','-').replace(' ','').split('-')
            if crates==[]:
                crates=spline
            else:
                crates=[x+y for x,y in zip(crates,spline)]
        elif "move" in line:
            spline=list(map(int,line.strip().replace("move ","").replace("from ","").replace("to ","").split()))
            crates[spline[2]-1] = crates[spline[1]-1]\
                    [0:int(spline[0])]+crates[spline[2]-1]
            crates[spline[1]-1] = crates[spline[1]-1][(int(spline[0])):]

print("".join([c[0] for c in crates]))
