with open("challengeinput.txt","r") as ifile:
    calories=[0]
    for line in ifile:
        if line.strip() == "":
            calories.append(0)
        else:
            calories[-1]+=(int(line.strip()))
calories.sort(reverse=True)
            
print(sum(calories[0:3]))
