import os
import sys

input_file = sys.argv[1]
lines = [line for line in open(input_file, "r").readlines()]
lines = map(lambda l: l.replace("\n", ""), lines)
# This variable hold a 2d array of the elfs calories
elf_cals = []
# This variable the index of the ciurrent elf
elf_identifier = 0

for line in lines:
    # replace \n with empty string
    line = line.replace("\n", "")
    if line == "":
        print("Empty line")
        elf_identifier += 1
    else:
        if len(elf_cals) <= elf_identifier:
            elf_cals.append([])
        elf_cals[elf_identifier].append(int(line))

elfs_total_cals = list(map(lambda elf: sum(elf), elf_cals))
# Find the elf with the most calories and store the index
elf_with_most_cals = elfs_total_cals.index(max(elfs_total_cals)) + 1

print("The elf with the most calories is the elf number: {} 🎅⛄️".format(elf_with_most_cals + 1))
print("That elf has eaten {} calories 🍪🍪🍪".format(max(elfs_total_cals)))
