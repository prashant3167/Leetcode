# Knapsack-based approach for grouping chapters

# Define the input
input_book = [[1, 2, 3], [20], [2, 4, 8], [1, 1], [15], [11, 2, 4], [1, 2], [1, 3, 2]]

def knapsack_grouping(book, max_questions):
    # Store the final groups
    regrouped_book = []
    # Keep track of which chapters have been used in a group
    used_chapters = [False] * len(book)

    # Helper function to check the maximum number of questions in a subset without exceeding the limit
    def find_best_group():
        dp = [0] * (max_questions + 1)
        # Store indices for chapters that will be included in this "group"
        chosen_chapters = [None] * (max_questions + 1)

        for i, chapter in enumerate(book):
            if used_chapters[i]:  # Skip already grouped chapters
                continue
            chapter_sum = sum(chapter)
            for j in range(max_questions, chapter_sum - 1, -1):
                if dp[j - chapter_sum] + chapter_sum > dp[j]:
                    dp[j] = dp[j - chapter_sum] + chapter_sum
                    chosen_chapters[j] = i

        # Construct the best possible group from chosen chapters
        best_group = []
        j = max_questions
        while chosen_chapters[j] is not None:
            idx = chosen_chapters[j]
            best_group.append(book[idx])
            used_chapters[idx] = True
            j -= sum(book[idx])

        return best_group

    # Group chapters using the knapsack helper function until all chapters are used
    while not all(used_chapters):
        best_group = find_best_group()
        regrouped_book.append([section for chapter in best_group for section in chapter])

    return regrouped_book

# Apply the function with the maximum limit of 30 questions per chapter
result = knapsack_grouping(input_book, 30)

# Output the result
print(result)