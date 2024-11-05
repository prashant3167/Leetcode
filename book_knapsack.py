from pprint import pprint

def knapsack(available_questions, capacity):
    n = len(available_questions)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    selected = [[False] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        chapter_sum = available_questions[i - 1][1]
        
        # print(available_questions[i-1][1])
        for w in range(1, capacity + 1):
            if chapter_sum <= w:
                if dp[i-1][w-chapter_sum] + chapter_sum > dp[i-1][w]:
                    dp[i][w] = dp[i-1][w-chapter_sum] + chapter_sum
                    selected[i][w] = True
                else:
                    dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = dp[i-1][w]

    res_items = []
    w = capacity
  # The code snippet `print(selected)` is used to print the `selected` list, which is a 2D list
  # representing whether an item is selected for each chapter and capacity combination during the
  # knapsack algorithm.
    # print(selected)
    # input()
    for i in range(n, 0, -1):
        # print(i, w)
        if selected[i][w]:
            res_items.append(available_questions[i-1])
            w -= available_questions[i-1][1]
    # input()
    return res_items

def clubQuestions(available_questions, max_capacity):
    bins = []
    remaining_chapters = [(chapter, sum(chapter)) for chapter in available_questions]
    ans = [sum(chapter) for chapter in available_questions]
    # print(ans)
    while remaining_chapters:
        current_bin = knapsack(remaining_chapters, max_capacity)
        
        if not current_bin:
            break

        bins.append([item[0] for item in current_bin])

        for item in current_bin:
            remaining_chapters.remove(item)

    return bins

array = [[1, 2, 3], [20], [2, 4, 8], [1, 1], [15], [11, 2, 4], [40], [1, 2], [1, 3, 2], [48]]
max_capacity = 30

bins = clubQuestions(array, max_capacity)

pprint(bins)
