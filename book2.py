from pprint import pprint

def knapsack(available_questions, capacity):
    n = len(available_questions)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    selected = [[False] * (capacity + 1) for _ in range(n + 1)]

    # DP Table computation
    for i in range(1, n + 1):
        chapter_sum = available_questions[i - 1][1]  # Number of questions in the chapter
        for w in range(1, capacity + 1):
            if chapter_sum <= w:
                if dp[i-1][w-chapter_sum] + chapter_sum > dp[i-1][w]:
                    dp[i][w] = dp[i-1][w-chapter_sum] + chapter_sum
                    selected[i][w] = True
                else:
                    dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = dp[i-1][w]

    # Trace back the selected items
    res_items = []
    w = capacity
    for i in range(n, 0, -1):
        if selected[i][w]:
            res_items.append(available_questions[i-1])
            w -= available_questions[i-1][1]

    return res_items

def clubQuestions(available_questions, max_capacity):
    bins = []
    # ans = []
    remaining_chapters = [(chapter, sum(chapter)) for chapter in available_questions]
    ans = [sum(chapter) for chapter in available_questions]
    print(ans)
    while remaining_chapters:
        # Use knapsack to find the best chapters to fit in the current bin
        current_bin = knapsack(remaining_chapters, max_capacity)
        
        if not current_bin:
            break

        # Add the selected chapters to a new bin
        bins.append([item[0] for item in current_bin])  # Store the actual chapters

        # Remove the chapters placed in the current bin from remaining_chapters
        for item in current_bin:
            remaining_chapters.remove(item)

    return bins

# Input data: List of chapters with the number of questions in each chapter
array = [[1, 2, 3], [20], [2, 4, 8], [1, 1], [15], [11, 2, 4], [40], [1, 2], [1, 3, 2], [48]]
max_capacity = 30

# Use knapsack-based bin packing solution
bins = clubQuestions(array, max_capacity)

# Print the final bins
pprint(bins)
