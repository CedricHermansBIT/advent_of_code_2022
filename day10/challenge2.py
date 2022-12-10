cycles=0
x=1

def drawPixel(x,cycles):
    if (x-1)<=(cycles-1)%40<=(x+1):
        print("#",end="")
    else:
        print(".",end="")
    if cycles%40==0:
        print("")


with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        spline=line.split()
        if spline[0]=="noop":
            cycles+=1
            drawPixel(x,cycles)
        elif spline[0]=="addx":
            cycles+=1
            drawPixel(x,cycles)
            cycles+=1
            drawPixel(x,cycles)
            x+=int(spline[1])
            
