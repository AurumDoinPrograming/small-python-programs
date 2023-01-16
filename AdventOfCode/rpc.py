def calculate_score():
    with open("game_strategy.txt", "r") as f:
        strategy_guide = [list(line.strip().split()) for line in f if line.strip()]
    if len(strategy_guide) == 0:
        return "strategy guide is empty"
    score = 0
    for round in strategy_guide:
        opponent_choice = round[0]
        my_choice = round[1]
        if my_choice == "X":
            my_score = 1
        elif my_choice == "Y":
            my_score = 2
        elif my_choice == "Z":
            my_score = 3
        else:
            return "Invalid choice"

        if opponent_choice == "A":
            opponent_score = 1
        elif opponent_choice == "B":
            opponent_score = 2
        elif opponent_choice == "C":
            opponent_score = 3
        else:
            return "Invalid choice"

        if my_score > opponent_score:
            score += my_score + 6
        elif my_score < opponent_score:
            score += my_score
        else:
            score += 3
    return score

print(calculate_score())