import numpy as np
from collections import defaultdict

directories = defaultdict(dict)
files, level = [], []
total_size = 0

def ls(directories, insert, levels):
    if not len(levels):
        for size, name in insert:
            directories[name] = size if isinstance(
                size, int) else {}
        return directories
    else:
        directories[levels[0]] = ls(directories[levels[0]], insert, levels[1:])
        return directories

with open('assets/input.txt', 'r') as f:
    for line in f.readlines():
        args = line.strip('\n').split(' ')
        if args[0] == '$':
            if len(files):
                directories = ls(directories, files, level)
                files = []
            if args[1] == 'cd':
                if args[-1] == '/':
                    level = []
                    continue
                if args[-1] == '..':
                    level.pop()
                else:
                    level.append(args[2])
        else:
            try:
                info = int(args[0])
                total_size += info
            except:
                info = args[0]
            files.append((info, args[1]))

# Part 1
def dir_sizes(directories, sizes):
    if all(isinstance(v, int) for v in directories.values()):
        dir_size = int(np.sum(list(directories.values())))
        sizes.append(dir_size)
        return dir_size, sizes
    else:
        partial_sum = 0
        for name, size in directories.items():
            if isinstance(size, int):
                partial_sum += size
            else:
                inner_size, sizes = dir_sizes(directories[name], sizes)
                partial_sum += inner_size
        sizes.append(partial_sum)
        return partial_sum, sizes


_, sizes = dir_sizes(directories, [])
print(np.sum([size for size in sizes if size <= 100000]))

# Part 2
req_space = total_size - 70000000 + 30000000
print(sizes[np.argmin([size if size > 0 else float('inf') for size in np.array(sizes) - req_space])])