def predict_score_with_all_decision(strategy):
    shape_points = {"X": 1, "Y": 2, "Z": 3}
    winning_combos = {"X": "C", "Y": "A", "Z": "B"}
    shape_translation = {"A": "X", "B": "Y", "C": "Z"}
    score = 0
    for line in strategy.split("\n"):
        opponent_input = line.split(" ")[0]
        user_input = line.split(" ")[1]
        if winning_combos[user_input] == opponent_input:
            score += 6
        elif user_input == shape_translation[opponent_input]:
            score += 3
        score += shape_points[user_input]
    return score

def predict_score_with_outcome(strategy):
    shape_points = {"X": 1, "Y": 2, "Z": 3}
    winning_combos_reverse = {"C": "X", "A": "Y", "B": "Z"}
    shape_translation = {"A": "X", "B": "Y", "C": "Z"}
    shape_translation_rev = {"X": "A", "Y": "B", "Z": "C"}
    score = 0
    for line in strategy.split("\n"):
        opponent_input = line.split(" ")[0]
        user_need = line.split(" ")[1]
        opponent_input_points = shape_points[shape_translation[opponent_input]]
        if user_need == "X":
        #Need to lose
            a = winning_combos_reverse[opponent_input]
            b = shape_translation_rev[a]
            score += shape_points[winning_combos_reverse[b]]
        elif user_need == "Y":
        #Need to draw.
            score += opponent_input_points + 3
        else:
        #Need to win
            score += shape_points[winning_combos_reverse[opponent_input]] + 6
    return score


