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
for assignment in assignments:
    firstsector, secondsector = assignment.split(",")

    #auch doppelte zahlen
    if int(firstsector[0]) > int(secondsector[0]) and int(firstsector[2]) <= int(secondsector[2]) or int(firstsector[0]) < int(secondsector[0]) and int(firstsector[2]) >= int(secondsector[2]):
        count += 1

print(count) 
    






