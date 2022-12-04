
options = {0: (0, 1), 45: (1, 1), 90: (1, 0), 135: (1, -1),
           180: (0, -1), 225: (-1, -1), 270: (-1, 0), 315: (-1, 1)}

position = (0, 0)
direction = 0
with open("challengeinput.txt", "r") as ifile:
    # with open("testinput.txt","r") as ifile:
    for line in ifile:
        spline = line.strip().split()
        match spline[0]:
            case "draai":
                angle = int(spline[1])
                direction = (direction+angle) % 360
            case "loop" | "spring":
                steps = int(spline[1])
                position = (position[0]+steps*options[direction]
                            [0], position[1]+steps*options[direction][1])
print(position[0]+position[1])
