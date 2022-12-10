# regex library for regex opertions
import re


# get input from file
file = open("day5input.txt", "r");
input = file.read().split("\n");
file.close()

# create a second list with the input for the second part


# input = '''    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2'''.split("\n")



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


count = 0;
for line in input:
    if count == matrixLen:
        break
    else:

        if "    " in line:
            line = line.replace("    ", " ")


        for e in range(matrixLen):
            lineSplitted = line.split(" ")
            if lineSplitted[e] == "":
                continue
            else:
                crates[e].insert(0, lineSplitted[e])

        count += 1



for count, src, des in instructions:
    # for a in range(count):
        # crates[des-1].append(crates[src-1][-1])
        # crates[src-1].pop()
    
    for a in range(count):
        crates[des-1].append(crates[src-1][-count+a])
        crates[src-1].pop(-count+a)

    



top = list();
for e in range(matrixLen):
    top.append(crates[e][-1].strip("[").strip("]"))


print(f'The top crates when the CrateMover 9001 ist done are: {"".join(top)}!')








