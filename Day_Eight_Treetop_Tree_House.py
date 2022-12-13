def visible_trees(quadcopter_input):
    y_counter = 0
    visited = []
    visible = 0
    matrix = []
    for array in quadcopter_input.split("\n"):
        greater_then = -1
        x = 0
        while int(array[x]) > greater_then:
            visible += 1
            visited.append((x, y_counter))
            greater_then = int(array[x])
            x += 1

        greater_then = -1
        x = 0
        while int(array[len(array) - 1 - x]) > greater_then:
            greater_then = int(array[x])
            x += 1
            if not tuple((x, y_counter)) in visited:
                visible += 1
                visited.append((x, y_counter))
        y_counter += 1

        matrix.append(list(array))

    for x in range(len(matrix[0])):
        y = 0
        greater_then = -1
        while int(matrix[x][y]) > greater_then:
            greater_then = int(matrix[x][y])
            y += 1
            if not tuple((x, y)) in visited:
                visible += 1
                visited.append((x, y))


    for x in range(len(matrix[0])):
        y = 0
        greater_then = -1
        while int(matrix[x][len(array) - 1 - y]) > greater_then:
            greater_then = int(matrix[x][y])
            y += 1
            if not tuple((x, y)) in visited:
                visible += 1
                visited.append((x, y))


    return visible

print(visible_trees("""30373
25512
65332
33549
35390"""))

