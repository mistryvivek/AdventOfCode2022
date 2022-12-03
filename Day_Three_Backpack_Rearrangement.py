def backpack_rearrangement(backpack):
    backpack_separated = backpack.split("\n")
    priorities = 0
    for backpack in backpack_separated:
        index_to_split = int(len(backpack) / 2)
        compartment_one = backpack[:index_to_split]
        compartment_two = backpack[index_to_split:]

        intersection = set(list(compartment_two)).intersection(list(compartment_one))
        for value in list(intersection):
            priorities += ord(value.lower()) - ord("a") + 1
            if value.isupper():
                priorities += 26
    return priorities


def missing_badges(backpack):
    backpack_separated = backpack.split("\n")
    priorities = 0
    for x in range(0, len(backpack_separated), 3):
        intersection = set(list(backpack_separated[x])).intersection(list(backpack_separated[x + 1]),
                                                                     list(backpack_separated[x + 2]))
        for value in list(intersection):
            priorities += ord(value.lower()) - ord("a") + 1
            if value.isupper():
                priorities += 26
    return priorities
