file = open("day1input.txt", "r");
invAllElves = file.read().split("\n");
file.close()

#print(invAllElves)

# list to save the total amount of calories by elve
sumCalByElve = list();

# define variable that represents the current sum of an elve
currentSum = 0;

# for each checked item in the list
for item in invAllElves:
    # first check if the line is empty
    if item == "":
        # if so, append the current sum to the list and reset the current sum
        sumCalByElve.append(currentSum);
        currentSum = 0;
        continue
        # else, add the current value to the current sum
    else:
        currentSum += int(item)

# get the biggest value from the list
maxCalories = max(sumCalByElve);

print("Biggest sum of calories one elve is carrying is", maxCalories, "calories! Which accomodates to", maxCalories/1000, "kilocalories!");
     
# first sort the list by value size, then get the sum of the last three value, which are the biggest ones
sortedList = sorted(sumCalByElve);
topThreeCalories = sum(sortedList[-3:]);

print("The three elves with the most calories together have", topThreeCalories, "calories! Which accomodates to", topThreeCalories/1000, "kilocalories!");







