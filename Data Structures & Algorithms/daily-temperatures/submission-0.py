class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        for i in range(n):
            current_temp = temperatures[i]
            no_of_days = 0
            for j in range(i+1, n):
                no_of_days += 1
                if (temperatures[j] > temperatures[i]):
                    result[i] = no_of_days
                    break
            

        return result