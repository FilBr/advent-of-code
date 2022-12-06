SEQ_LEN = [4, 14]

seq = []

for seq_len in SEQ_LEN:
    with open('assets/input.txt') as f:
        i = 0
        while True:
            c = f.read(1)
            i+=1
            if not c:
                print("End of file")
                break
            if len(seq) < seq_len:
                seq.append(c)
            else:
                seq.pop(0)
                seq.append(c)
                if len(seq) == len(set(seq)):
                    print(i)
                    break