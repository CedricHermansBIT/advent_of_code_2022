# A = Rock = 1
# B = Paper = 2
# C = Scissors = 3
# X = Lose
# Y = Draw
# Z = Win
# Win = 6, Draw = 3, Lose = 0}

scores = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    score=0
    for line in ifile:
        spline = line.strip()
        score += scores[spline]

print(score)

        
