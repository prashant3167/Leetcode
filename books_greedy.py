def bestFit(data, n, c):

    res = 0

    bins = []
    for _ in range(n):
        bins.append([])
    bin_rem = [0] * n

    for i in range(n):
        j = 0
        while j < res:
            if bin_rem[j] >= data[i][-1]:
                bin_rem[j] = bin_rem[j] - data[i][-1]
                data[i].pop()
                bins[j].extend(data[i])
                break
            j += 1

        if j == res:
            bin_rem[res] = c - data[i][-1]
            data[i].pop()
            bins[res].extend(data[i])
            res = res + 1
    return bins[0:res]


array = [
    [1, 2, 3],
    [20],
    [2, 4, 8],
    [1, 1],
    [15],
    [11, 2, 4],
    [40],
    [1, 2],
    [1, 3, 2],
    [48],
]
c = 30


def sort_function(data):
    return sum(data)


data = sorted(array, key=sort_function, reverse=True)

[data[i].append(sum(data[i])) for i in range(len(data))]

n = len(data)
ans = []
for i in range(n):
    if data[i][-1] >= c:
        data[i].pop()
        ans.append(data[i])
    else:
        data = data[i:]
        break

ans = ans + bestFit(data, len(data), c)
print(ans)
