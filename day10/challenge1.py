cycles=0
total=0
x=1

def check_cycle(cycles,x):
    if cycles==20 or (cycles-20)%40==0:
        print(cycles,x)
        global total
        total+=cycles*x

with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        spline=line.split()
        if spline[0]=="noop":
            cycles+=1
            check_cycle(cycles,x)
        elif spline[0]=="addx":
            cycles+=1
            check_cycle(cycles,x)
            cycles+=1
            check_cycle(cycles,x)
            x+=int(spline[1])

print(total)
