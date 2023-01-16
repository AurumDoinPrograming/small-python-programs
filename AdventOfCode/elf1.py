# open the file and read the contents
with open("puzzle_input.txt", "r") as file:
    puzzle_input = file.read()

# split the input by new line characters
calories = puzzle_input.split("\n")

# initialize variables to keep track of the current Elf and their total calories
current_elf = 1
elf_calories = 0

# initialize a variable to keep track of the Elf with the most calories
max_calories = 0
max_elf = 0

for calorie in calories:
    # if the calorie is not an empty string
    if calorie:
        elf_calories += int(calorie)
    else:
        # if it is an empty string, it means we have reached the end of an Elf's inventory
        if elf_calories > max_calories:
            max_calories = elf_calories
            max_elf = current_elf
        
        # reset the Elf's calorie count and move on to the next Elf
        elf_calories = 0
        current_elf += 1

# check if the last Elf has more calories than the previous ones
if elf_calories > max_calories:
    max_calories = elf_calories
    max_elf = current_elf

# the answer is the max_calories
print("Elf " + str(max_elf) + " is carrying the most calories with a total of " + str(max_calories) + " calories.")
