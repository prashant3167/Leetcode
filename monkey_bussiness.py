# Questionhttps://adventofcode.com/2022/day/11

# Inputs
# Monkey 0:
#   Starting items: 80
#   Operation: new = old * 5
#   Test: divisible by 2
#     If true: throw to monkey 4
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 75, 83, 74
#   Operation: new = old + 7
#   Test: divisible by 7
#     If true: throw to monkey 5
#     If false: throw to monkey 6

# Monkey 2:
#   Starting items: 86, 67, 61, 96, 52, 63, 73
#   Operation: new = old + 5
#   Test: divisible by 3
#     If true: throw to monkey 7
#     If false: throw to monkey 0

# Monkey 3:
#   Starting items: 85, 83, 55, 85, 57, 70, 85, 52
#   Operation: new = old + 8
#   Test: divisible by 17
#     If true: throw to monkey 1
#     If false: throw to monkey 5

# Monkey 4:
#   Starting items: 67, 75, 91, 72, 89
#   Operation: new = old + 4
#   Test: divisible by 11
#     If true: throw to monkey 3
#     If false: throw to monkey 1

# Monkey 5:
#   Starting items: 66, 64, 68, 92, 68, 77
#   Operation: new = old * 2
#   Test: divisible by 19
#     If true: throw to monkey 6
#     If false: throw to monkey 2

# Monkey 6:
#   Starting items: 97, 94, 79, 88
#   Operation: new = old * old
#   Test: divisible by 5
#     If true: throw to monkey 2
#     If false: throw to monkey 7

# Monkey 7:
#   Starting items: 77, 85
#   Operation: new = old + 6
#   Test: divisible by 13
#     If true: throw to monkey 4
#     If false: throw to monkey 0

# Monkey divisibility check
mdc = {0: 2, 1: 7, 2: 3, 3: 17, 4: 11, 5: 19, 6: 5, 7: 13}
# Monkey to monkey transfer
m2m = {
    0: [4, 3],
    1: [5, 6],
    2: [7, 0],
    3: [1, 5],
    4: [3, 1],
    5: [6, 2],
    6: [2, 7],
    7: [4, 0],
}
# Monkey Operation
mo = {0: "*5", 1: "+7", 2: "+5", 3: "+8", 4: "+4", 5: "*2", 6: "**2", 7: "+6"}
# Monkey holds
msi = {
    0: [80],
    1: [75, 83, 74],
    2: [86, 67, 61, 96, 52, 63, 73],
    3: [85, 83, 55, 85, 57, 70, 85, 52],
    4: [67, 75, 91, 72, 89],
    5: [66, 64, 68, 92, 68, 77],
    6: [97, 94, 79, 88],
    7: [77, 85],
}
# Monkey_inspected
mi = [0]*8


def monkey_operation(monkey_index):
    while(len(msi[monkey_index])!=0):
        item = msi[monkey_index].pop(0)
        # Check with operation
        item_v2 = eval(f"{item}{mo[monkey_index]}")
        # After getting bored
        item_v3 = item_v2 // 3
        # Divisibilility check
        index = 0 if item_v3 % mdc[monkey_index]==0 else 1
        # Push to another monkey
        msi[m2m[monkey_index][index]].append(item_v3)
        mi[monkey_index]+=1
    
def main():
    for _ in range(20):
        for i in range(8):
            monkey_operation(i)
    mi.sort(reverse=True)
    return mi[0]*mi[1]


print(main())
