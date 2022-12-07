file = open("day4input.txt", "r");
assignments = file.read().split("\n");
file.close()

# assignments = '''2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8'''.split("\n")

count = 0;
# check every elve-pairs assignment
for assignment in assignments:

    # split that assignments two sectors in a list
    firstsector, secondsector = assignment.split(",")

    #splitting each sector range into only the numbers
    firstsector = firstsector.split("-")
    secondsector = secondsector.split("-")

    # get the start and end sector of the first range
    firstSecFNum = int(firstsector[0])
    firstSecLNum = int(firstsector[1])

    # get the start and end sector of the second range
    secondSecFNum = int(secondsector[0])
    secondSecLNum = int(secondsector[1])

    # checking
    if firstSecFNum >= secondSecFNum and firstSecLNum <= secondSecLNum \
        or firstSecFNum <= secondSecFNum and firstSecLNum >= secondSecLNum:

        count += 1

print("A total of ", count, "sectors are being completely overlapped by their other half in the pair!")


count = 0;
# check every elve-pairs assignment
for assignment in assignments:

    # split that assignments two sectors in a list
    firstsector, secondsector = assignment.split(",")

    #splitting each sector range into only the numbers
    firstsector = firstsector.split("-")
    secondsector = secondsector.split("-")

    # get the start and end sector of the first range
    firstSecFNum = int(firstsector[0])
    firstSecLNum = int(firstsector[1])

    # get the start and end sector of the second range
    secondSecFNum = int(secondsector[0])
    secondSecLNum = int(secondsector[1])

    # checking
    if firstSecLNum >= secondSecFNum and secondSecLNum >= firstSecFNum:
        count += 1


print("There are a total of ", count, "overlaps of assgined sectors in every assignment!")







