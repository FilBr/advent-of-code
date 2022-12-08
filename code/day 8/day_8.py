import numpy as np

data = np.array([[int(n) for n in row.strip('\n')]
                 for row in open("assets/input.txt").readlines()])

# Part 1
vert_min = 1
vert_max = len(data)-1

hor_min = 1
hor_max = len(data[0])-1

total_trees = len(data)*len(data[0])
hidden_trees = 0

for i in range(vert_min, vert_max):
    for j in range(hor_min, hor_max):
        left = data[i, :j]
        right = data[i, j+1:]
        up = data[:i, j]
        down = data[i+1:, j]
        if data[i][j] <= np.max(left) and data[i][j] <= np.max(right) and data[i][j] <= np.max(up) and data[i][j] <= np.max(down):
            hidden_trees += 1

print(total_trees - hidden_trees)


# Part 2
best_scenic_score = 1
for i in range(0, len(data)):
    for j in range(0, len(data[0])):
        left = data[i, :j]
        right = data[i, j+1:]
        up = data[:i, j]
        down = data[i+1:, j]
        scenic_score = 1
        scenic_scores = []
        for view in [left[::-1], right, up[::-1], down]:
            for num, tree in enumerate(view):
                if tree >= data[i][j] or num == len(view)-1:
                    scenic_scores.append(num+1)
                    break

        for score in scenic_scores:
            scenic_score *= score
        if scenic_score > best_scenic_score:
            best_scenic_score = scenic_score

print(best_scenic_score)
