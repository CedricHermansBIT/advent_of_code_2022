with open("challengeinput.txt","r") as ifile:
    calories=[0]
    for line in ifile:
        if line.strip() == "":
            calories.append(0)
        else:
            calories[-1]+=(int(line.strip()))

# Elf with most calories
print(max(calories))
print(calories.index(max(calories))+1)
