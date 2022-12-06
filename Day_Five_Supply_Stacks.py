import re


def supply_stacks(initial_stack, steps):
    steps = steps.split("\n")
    for step in steps:
        step_re = re.findall(r"move\s*(\d+)\s*from\s*(\d+)\s*to\s*(\d+)", step)
        for x in range(int(step_re[0][0])):
            initial_stack[int(step_re[0][2]) - 1].append((initial_stack[int(step_re[0][1]) - 1].pop()))
    return initial_stack


def supply_stacks_retain_order(initial_stack, steps):
    steps = steps.split("\n")
    for step in steps:
        step_re = re.findall(r"move\s*(\d+)\s*from\s*(\d+)\s*to\s*(\d+)", step)
        add = []
        for x in range(int(step_re[0][0])):
            add.append((initial_stack[int(step_re[0][1]) - 1].pop()))
        initial_stack[int(step_re[0][2]) - 1] = initial_stack[int(step_re[0][2]) - 1] + add[::-1]

    return initial_stack
