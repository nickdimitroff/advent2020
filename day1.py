with open("day1.txt") as f:
    inputs = [int(line.strip()) for line in f]

for i in inputs:
    for j in inputs:
        if i + j == 2020:
            print(i * j)
        for k in inputs:
            if i + j + k == 2020:
                print(i * j * k)