#
# @lc app=leetcode id=1093 lang=python3
#
# [1093] Statistics from a Large Sample
#

# @lc code=start
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum, maximum, mode = None, None, None
        mean, median = None, 0
        max_value = 0 
        sum_c, c = 0, 0
        total = sum(count)
        x = None
        if total%2==0:
            x = [total//2,(total//2)+1]
        else:
            x = [(total//2)+1]
        # print(x)
        for i in range(len(count)):
            if count[i] != 0:
                if minimum==None:
                    minimum = format(i, '.5f')
                maximum = format(i, '.5f')
                if count[i]>max_value:
                    max_value=count[i]
                    mode = format(i, '.5f')
            sum_c += (i*count[i])
            # print(c, c+count[i])
            if c<x[0]<=c+count[i]:
                median += i
            if len(x)>1 and c<x[1]<=c+count[i]:
                median += i
            c += count[i]
            # if c<=x[0]<
            count[i] = c
        mean = format(sum_c/c, '.5f')
        median = format(median/len(x), '.5f')  
        ans = [minimum, maximum, mean, median, mode]
        float_list_5_decimal = [round(float(num), 5) for num in ans]
        return float_list_5_decimal   
            
        
# @lc code=end

