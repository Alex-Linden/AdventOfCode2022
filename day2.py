lose = 0
draw = 3
win = 6
rock = 'A' 1
paper = 'B' 2
scissors = 'C' 3
X = lose
Y = draw
Z = win
score = 0
games = []

scoring = {'X': 0, 'Y': 3, 'Z': 6}

for game in games:
    score += scoring[game[2]]
    if game[0] == 'A':
        if game[2] == 'X':
            score += 3
        elif game[2] == 'Y':
            score += 1
        else:
            score += 2
    elif game[0] == 'B':
        if game[2] == 'X':
            score += 1
        elif game[2] == 'Y':
            score += 2
        else:
            score += 3
    else:
        if game[2] == 'X':
            score += 2
        elif game[2] == 'Y':
            score += 3
        else:
            score += 1

