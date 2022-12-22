
import re


commands = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split("\n")


sizeByDir = list()

dirs = list()

max = 100000;

amountInCurrentDir = 0;

dirHistory = list();
currentDir = ""; 

for command in commands:
    commandcount = 0;
    if "cd" in command:
        currentDir = command.split(" ")[2]
        dirHistory.append(currentDir)
        
        if currentDir == "..":
            
            print("Not implemented")

    

    if re.search(r"^\d", command):
        amountInCurrentDir += int(command.split(" ")[0])            

    commandcount += 1


