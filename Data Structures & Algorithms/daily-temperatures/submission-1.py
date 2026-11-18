class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        my_temp_stack = []
        result = [0] * n

        for i in range(n):
            while (my_temp_stack and temperatures[i] > my_temp_stack[-1][0]):
                ele = my_temp_stack.pop()
                result[ele[1]] = i - ele[1]
            
            my_temp_stack.append([temperatures[i], i])

        return result
            
