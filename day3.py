#testString = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw"
#rucksacks = testString.split("\n")

# get input via file and save as string
file = open("day3input.txt", "r");
rucksacks = file.read().split("\n");
file.close()

# define lists for letters and prios
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
prios = list(range(1,53))

# define variable to count total priority
totalPrio = 0;

# foreach rucksack in the list
for rucksack in rucksacks:

    # get the compsize by splitting the rucksack size into two
    compSize = int(len(rucksack)/2)

    # define first and second compartment
    firstComp = rucksack[0:compSize]
    secondComp = rucksack[compSize:]

    # define variable to save if one rucksack is finished checking
    foundInRucksack = False;    

    # foreach letter in the first and secon comp
    for letterF in firstComp:
        for letterS in secondComp:
            # check if they are the same and if the pair hasn't been found yet
            if letterF == letterS and foundInRucksack == False:
                # assign the foundInRucksack variable to True, since the pair has been found
                foundInRucksack = True

                # get the position of the found letter that is in both compartments, and get the related priority and add it to the sum
                posLetterF = letters.index(letterF)
                totalPrio += prios[posLetterF]

    # after all the letters have been checked, and the pair has been found, set the foundInRucksack variable to False, to check the next rucksack
    foundInRucksack = False;


print("The total priority comes out to" , totalPrio, "points!")

# Reset all variables
totalPrio = 0;
rucksackCount = 0;
currentGroup = list();
foundInGroup = False;

# check each rucksack
for rucksack in rucksacks:
    # add a new rucksack to the current group, if the group doesn't have 3 rucksacks yet
    currentGroup.append(rucksack)
    if len(currentGroup) != 3:
        continue;
    else:
        # check every letter
        for letterfir in currentGroup[0]:
            for lettersec in currentGroup[1]:
                for letterthi in currentGroup[2]:
                    # if a same letter in all the rucksacks has been found, add the prio to the total prio
                    if letterfir == lettersec == letterthi and foundInGroup == False:
                        foundInGroup = True

                        posLetter = letters.index(letterfir)
                        totalPrio += prios[posLetter] 
                    
        # reset the current group and the foundInGroup variable
        currentGroup = list();
        foundInGroup = False;


print("The total priority, when looking at groups of three rucksacks, comes out to" , totalPrio, "points!")




