with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    s=0
    for line in ifile:
        spline= line.split(",")
        a1,a2 = spline[0].split("-")
        b1,b2 = spline[1].split("-")
        a1,a2,b1,b2 = int(a1),int(a2),int(b1),int(b2)
        if (a1>=b1 and a2<=b2) or (b1>=a1 and b2<=a2):
            s+=1
    print(s)
