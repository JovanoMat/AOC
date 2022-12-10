# regex library
import re

# get input from file
file = open("day6input.txt", "r");
input = file.read();
file.close()

# input = "bvwbjplbgvbhsrlpgdmjqwftvncz"

count = 0;
lastFour = "";

for letter in input:
    if count < 4:
        count += 1
        lastFour += letter
        continue
    
    else:
        if re.search(r"^(?!.*(.).*\1)[a-zA-Z]*$", lastFour):
            print(f"The first start-of-packet marker is at {count}, when looking at groups of four!")

            break

        else:
            lastFour = lastFour[1:] + letter
            count += 1




# Part 2

count = 0;
lastFourteen = "";

for letter in input:
    while count < 14:
        count += 1
        lastFourteen += letter
        continue
    
    
    if re.search(r"^(?!.*(.).*\1)[a-zA-Z]*$", lastFourteen):
        print(f"The first start-of-packet marker is at {count}, when looking at groups of fourteen!")

        break

    else:
        lastFourteen = lastFourteen[1:] + letter
        count += 1


