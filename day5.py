import numpy as np
import re

input = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''.split("\n")


matrixLen = 0;
instructions = list();


for line in input:
    if line == "":
        continue

    elif re.search(r"^[1-9]$", line[1]):

        for element in line.split(" "):
            if element == "":
                continue
            elif int(element) > matrixLen:
                matrixLen = int(element)

    elif "move" in line:
        line = line.split(" ")
        instruction = (int(line[1]), int(line[3]), int(line[5]))
        instructions.append(instruction)

    else:
        continue


crates = list();
for e in range(matrixLen):
    crates.append(list())


print(instructions)
print(crates)




createStatus = np.matrix(crates);





