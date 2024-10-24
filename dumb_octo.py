import numpy as np
from itertools import product

# with open("./day_11.in") as fin:
#     raw_data = fin.read().strip()
octo=[[6, 7, 8, 8, 3, 8, 3, 4, 3, 6], [5, 5, 2, 6, 8, 2, 7, 4, 4, 1], [4, 5, 8, 2, 4, 3, 5, 8, 6, 6], [5, 1, 5, 2, 5, 4, 7, 2, 7, 3], [3, 7, 4, 6, 4, 3, 3, 6, 2, 1], [2, 4, 6, 5, 1, 4, 5, 3, 6, 5], [6, 3, 2, 4, 8, 8, 7, 1, 2, 8], [8, 5, 3, 7, 5, 5, 8, 7, 4, 5], [4, 7, 1, 8, 4, 2, 7, 5, 6, 2], [2, 2, 8, 3, 3, 2, 4, 7, 4, 6]]

# octo = [[5, 4, 8, 3, 1, 4, 3, 2, 2, 3], [2, 7, 4, 5, 8, 5, 4, 7, 1, 1], [5, 2, 6, 4, 5, 5, 6, 1, 7, 3], [6, 1, 4, 1, 3, 3, 6, 1, 4, 6], [6, 3, 5, 7, 3, 8, 5, 4, 7, 8], [4, 1, 6, 7, 5, 2, 4, 6, 4, 5], [2, 1, 7, 6, 8, 4, 1, 7, 2, 1], [6, 8, 8, 2, 8, 8, 1, 1, 3, 4], [4, 8, 4, 6, 8, 4, 8, 5, 5, 4], [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]]
octo = np.array(octo, dtype=int)
print(octo)
ans = 0
N=len(octo)

for i in range(100):
    flashed  = np.zeros((N, N), dtype=bool)
    
    for i, j in product(range(N), repeat=2):
        octo[i, j] += 1
    
    while True:
        keep_going = False
        change = np.zeros((N, N), dtype=int)
        for i, j in product(range(N), repeat=2):
            if not flashed[i , j] and octo[i, j]>9:
                keep_going = True
                flashed[i, j]=1
                for ii, jj in product(range(-1, 2), repeat=2):
                    if ii==jj==0:
                        continue
                    di = i +ii
                    dj = j+jj
                    if not (0 <= di < N and 0 <= dj < N):
                        continue
                    change[di, dj] +=1
        octo += change
        if not keep_going:
            break
    for i, j in product(range(N), repeat=2):
        if flashed[i, j]:
            ans +=1
            octo[i, j] =0

print(ans)
                
                    