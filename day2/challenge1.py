# A, X = ROCK and score=1
# B, Y = PAPER and score=2
# C, Z = SCISSORS and score=3
# Win = 6, Draw = 3, Lose = 0}

scores = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}

with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    score=0
    for line in ifile:
        spline = line.strip()
        score += scores[spline]

print(score)

        
