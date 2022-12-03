def backpack_rearrangement(backpack):
    backpack_separated = backpack.split("\n")
    for backpack in backpack_separated:
        index_to_split = int(len(backpack) / 2)
        compartment_one = backpack[:index_to_split]
        compartment_two = backpack[index_to_split:]

    return compartment_two, compartment_one

print(backpack_rearrangement("vJrwpWtwJgWrhcsFMMfFFhFp"))