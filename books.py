from pprint import pprint
def binPackingKnapsack(weights, bin_capacity):
    n = len(weights)
    packed = [False] * n
    bins = []

    def knapsack(available_items, capacity):
        dp = [[0] * (capacity + 1) for _ in range(len(available_items) + 1)]
        selected = [[False] * (capacity + 1) for _ in range(len(available_items) + 1)]
        
        for i in range(1, len(available_items) + 1):
            weight = available_items[i-1]
            for w in range(1, capacity + 1):
                if weight <= w:
                    # Option 1: include the current item
                    if dp[i-1][w-weight] + weight > dp[i-1][w]:
                        dp[i][w] = dp[i-1][w-weight] + weight
                        selected[i][w] = True
                    else:
                        dp[i][w] = dp[i-1][w]
                else:
                    dp[i][w] = dp[i-1][w]
        # print(dp)
        res_items = []
        w = capacity
        for i in range(len(available_items), 0, -1):
            if selected[i][w]:
                res_items.append(available_items[i-1])
                w -= available_items[i-1]

        return res_items

    while any(not p for p in packed):
        available_items = [weights[i] for i in range(n) if not packed[i]]
        current_bin = knapsack(available_items, bin_capacity)
        bins.append(current_bin)

        for item in current_bin:
            for i in range(n):
                if weights[i] == item and not packed[i]:
                    packed[i] = True
                    break

    return bins

# Input data
# weights = [40, 4, 42, 8, 43, 4, 3, 19, 30, 6]
weights = [6, 20, 14, 2, 15, 17, 3, 6]
weights.sort()
print(weights)
bin_capacity = 30
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

# Use knapsack-based bin packing solution
bins = binPackingKnapsack(weights, bin_capacity)
print("Bins:", bins)
