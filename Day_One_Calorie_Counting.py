def calorie_counting(puzzle_input):
    cals_by_elves = puzzle_input.split("\n\n")
    total_cals_per_elves = []
    print(cals_by_elves)
    for cals_by_elf in cals_by_elves:
        total_cals_per_elves.append(sum([int(x) for x in cals_by_elf.split("\n")]))
    return max(total_cals_per_elves)
