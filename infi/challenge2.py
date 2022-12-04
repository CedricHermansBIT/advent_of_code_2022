import turtle

turtle.Screen().bgcolor("white")

options={0:(0,1), 45: (1,1), 90: (1,0), 135: (1,-1), 180: (0,-1), 225: (-1,-1), 270: (-1,0), 315: (-1,1)}
turtle.left(90)
direction=0
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        spline=line.strip().split()
        match spline[0]:
            case "draai":
                angle=int(spline[1])
                if angle>0:
                    turtle.right(angle)
                else:
                    turtle.left(-angle)
            case "loop":
                steps=int(spline[1])*5
                turtle.forward(steps)
            case "spring":
                steps=int(spline[1])*5
                turtle.penup()
                turtle.forward(steps)
                turtle.pendown()
input()