def backtrack(arr, index, subarrays, max_sum):
    if index == len(arr):
        return len(subarrays), [list(subarray) for subarray in subarrays]

    min_subarrays = float("inf")
    best_solution = None

    for i in range(len(subarrays)):
        if sum(subarrays[i]) + arr[index] <= max_sum:
            subarrays[i].append(arr[index])
            num_subarrays, solution = backtrack(arr, index + 1, subarrays, max_sum)
            if num_subarrays < min_subarrays:
                min_subarrays = num_subarrays
                best_solution = solution
            subarrays[i].pop()

    subarrays.append([arr[index]])
    num_subarrays, solution = backtrack(arr, index + 1, subarrays, max_sum)
    if num_subarrays < min_subarrays:
        min_subarrays = num_subarrays
        best_solution = solution
    subarrays.pop()

    return min_subarrays, best_solution


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
max_capacity = 30

question_chapter_packing = {}

available_questions = []
final_answer = []
for i in array:
    key = sum(i)
    if key < max_capacity:
        available_questions.append(key)
    else:
        final_answer.append(i)
        continue
    if key in question_chapter_packing:
        question_chapter_packing[key].append(i)
    else:
        question_chapter_packing[key] = [i]


min_subarrays, result = backtrack(available_questions, 0, [], max_capacity)

for i in range(len(result)):
    x = []
    for j in result[i]:
        mapped_chapter = question_chapter_packing[j].pop()
        x.extend(mapped_chapter)
    final_answer.append(x)
print(final_answer)
