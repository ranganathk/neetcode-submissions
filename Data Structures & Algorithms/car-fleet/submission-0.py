class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        n = len(position)
        for i in range(n):
            tup = (position[i], speed[i])
            combined.append(tup)

        combined.sort(key=lambda x: x[0], reverse=True)
    
        time_to_reach = []

        for pos, sp in combined:
            time = (target - pos)/sp
            time_to_reach.append(time)

        for k in range(1, n):
            if (time_to_reach[k] <= time_to_reach[k-1]):
                time_to_reach[k] = time_to_reach[k-1]
        
        return len(set(time_to_reach))
        