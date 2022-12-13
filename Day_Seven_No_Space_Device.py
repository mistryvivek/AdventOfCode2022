def space_detection(commands):
    navigated = []
    dir_size = {}
    for command in commands.split("\n"):
        if command == "$ cd ..":
            navigated.pop()
        elif command.startswith("$ cd"):
            navigated.append(command.replace("$ cd ",""))
        elif command == "$ ls" or command.startswith("dir"):
            continue
        else:
            for dir in navigated:
                if dir in dir_size.keys():
                    dir_size[dir] += int(command.split()[0])
                else:
                    dir_size[dir] = int(command.split()[0])

    print(dir_size)

    total = 0
    for value in dir_size.values():
        if value <= 100000:
            total += value
            print(total)

    return total

