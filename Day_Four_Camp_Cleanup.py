def matching_pairs(lines):
    lines = lines.split("\n")
    counter = 0
    for line in lines:
        group_one, group_two = line.split(",")
        group_one_lower, group_one_upper = group_one.split("-")
        group_two_lower, group_two_upper = group_two.split("-")
        if int(group_two_lower) >= int(group_one_lower) and int(group_one_upper) >= int(group_two_upper) \
            or int(group_one_lower) >= int(group_two_lower) and int(group_two_upper) >= int(group_one_upper):
            counter += 1
    return counter

def matching_pairs_two(lines):
    lines = lines.split("\n")
    counter = 0
    for line in lines:
        group_one, group_two = line.split(",")
        group_one = range(int(group_one.split("-")[0] - 1), int(group_one.split("-")[1] - 1))
        intersection = set(list(group_one)).intersection(range(list(int(group_two.split("-")[0]), int(group_two.split("-")[1]))))
        if len(intersection) > 0:
            counter += 1
    return counter

print(matching_pairs_two("""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""))