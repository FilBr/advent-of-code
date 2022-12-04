with open('assets/input.txt') as f:
    data = [line.split(',') for line in f.readlines()]

# Part 1
count = 0

for pair in data:
    first, second = pair
    first, second = [int(i) for i in first.split('-')], [int(i) for i in second.split('-')]

    if first[0] <= second[0] <= second[1] <= first[1] or second[0] <= first[0] <= first[1] <= second[1]:
        count += 1

print(count)

# Part 2

count = 0

for pair in data:
    first, second = pair
    first, second = [int(i) for i in first.split('-')], [int(i) for i in second.split('-')]

    if first[0] <= second[0] <= first[1] or second[0] <= first[0] <= second[1]:
        count += 1

print(count)