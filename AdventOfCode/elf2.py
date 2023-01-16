# open the file and read the contents
with open("puzzle_input.txt", "r") as file:
    puzzle_input = file.read()

# split the input by new line characters
calories = puzzle_input.split("\n")

# initialize variables to keep track of the current Elf and their total calories
current_elf = 1
elf_calories = 0

# initialize a list to keep track of the calories of all Elves
elf_calories_list = []

for calorie in calories:
    # if the calorie is not an empty string
    if calorie:
        elf_calories += int(calorie)
    else:
        # if it is an empty string, it means we have reached the end of an Elf's inventory
        elf_calories_list.append(elf_calories)
        
        # reset the Elf's calorie count and move on to the next Elf
        elf_calories = 0
        current_elf += 1

# check if the last Elf has more calories than the previous ones
elf_calories_list.append(elf_calories)

# sort the list of calories in descending order
elf_calories_list.sort(reverse=True)

# take the first three elements of the list
top_three = elf_calories_list[:3]

# calculate the total calories of the top three Elves
total_calories = sum(top_three)

# the answer is the total_calories
print("The top three Elves are carrying a total of " + str(total_calories) + " calories.")