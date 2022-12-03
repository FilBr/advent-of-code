# rock paper scissors game
LOSE = 0
DRAW = 3
WIN = 6

rules = {
    'rock': {
        'rock': DRAW,
        'paper': LOSE,
        'scissors': WIN,
        'score': 1
    },
    'paper': {
        'rock': WIN,
        'paper': DRAW,
        'scissors': LOSE,
        'score': 2
    },
    'scissors': {
        'rock': LOSE,
        'paper': WIN,
        'scissors': DRAW,
        'score': 3
    }
}

mapping = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

score = 0

with open('assets/input.txt') as f:
    for line in f.readlines():
        line = line.strip().split()
        score += rules[mapping[line[1]]][mapping[line[0]]] + \
            rules[mapping[line[1]]]['score']

print(score)

# Part 2
rules = {
    # Rock
    'A': {
        'X': LOSE + rules['scissors']['score'],
        'Y': DRAW + rules['rock']['score'],
        'Z': WIN + rules['paper']['score']
    },
    # Paper
    'B': {
        'X': LOSE + rules['rock']['score'],
        'Y': DRAW + rules['paper']['score'],
        'Z': WIN + rules['scissors']['score']
    },
    # Scissors
    'C': {
        'X': LOSE + rules['paper']['score'],
        'Y': DRAW + rules['scissors']['score'],
        'Z': WIN + rules['rock']['score']
    },
}

score = 0

with open('assets/input.txt') as f:
    for line in f.readlines():
        line = line.strip().split()
        score += rules[line[0]][line[1]]

print(score)
