# Setup

data = []

with open("assets/input.txt", 'r') as f:
    for line in f.readlines():
        data.append(line.strip())

lowercase_offset = 1 - ord('a')
uppercase_offset = 27 - ord('A')


# Part 1
priority_score = 0

for line in data:
    split = len(line) // 2
    first_half = list(line[:split])
    second_half = list(line[split:])

    common = set(first_half).intersection(set(second_half)).pop()

    if common.islower():
        priority_score +=  ord(common) + lowercase_offset
    else:
        priority_score += ord(common) + uppercase_offset

print(priority_score)


# Part 2
priority_score = 0

for i in range(0, len(data), 3):
    group = [list(group) for group in data[i:i+3]]
    common = set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop()

    if common.islower():
        priority_score +=  ord(common) + lowercase_offset
    else:
        priority_score += ord(common) + uppercase_offset

print(priority_score)