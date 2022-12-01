def calorie_counting_max(puzzle_input):
    cals_by_elves = puzzle_input.split("\n\n")
    total_cals_per_elves = []
    for cals_by_elf in cals_by_elves:
        total_cals_per_elves.append(sum([int(x) for x in cals_by_elf.split("\n")]))
    return max(total_cals_per_elves)


def calorie_counting_top_three(puzzle_input):
    cals_by_elves = puzzle_input.split("\n\n")
    total_cals_per_elves = []
    for cals_by_elf in cals_by_elves:
        total_cals_per_elves.append(sum([int(x) for x in cals_by_elf.split("\n")]))
    total_cals_per_elves.sort(reverse=True)
    return total_cals_per_elves[0] + total_cals_per_elves[1] + total_cals_per_elves[2]
