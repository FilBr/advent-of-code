import numpy as np

data = []
elf = []

with open("assets/input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        if len(line) == 0:
            data.append(np.sum(elf))
            elf = []
        else:
            elf.append(int(line))

data.sort(reverse=True)

print(f"Part 1: {data[0]}")
print(f"Part 2: {np.sum(data[:3])}")
