stacks = []
moves = []
commands = False

with open('assets/input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if len(line) == 0:
            commands = True
            continue
        if not commands:
            num_stacks = (len(line) + 1) // 4
            if len(stacks) == 0:
                stacks = [[] for _ in range(num_stacks)]
            for idx, stack in enumerate(range(0, len(line), 4)):
                stack = line[stack+1]
                if stack != ' ':
                    try:
                        int(stack)
                    except:
                        stacks[idx].append(stack)
        else:
            move = line.split(' ')
            amount = int(move[1])
            src = int(move[3]) - 1
            dst = int(move[5]) - 1

            moves.append((amount, src, dst))

    stacks = [stack[::-1] for stack in stacks]

# Part 1
p1_stacks = [stack[:] for stack in stacks]
for move in moves:
    amount, src, dst = move
    tmp = []
    for _ in range(amount):
        tmp.append(p1_stacks[src].pop())

    p1_stacks[dst] += tmp

print(''.join([stack[-1] for stack in p1_stacks]))


# Part 2

p2_stacks = [stack[:] for stack in stacks]
for move in moves:
    amount, src, dst = move
    tmp = []
    for _ in range(amount):
        tmp.append(p2_stacks[src].pop())

    p2_stacks[dst] += tmp[::-1]

print(''.join([stack[-1] for stack in p2_stacks]))
