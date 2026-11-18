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

        last_fleet_time = 0
        no_of_fleets = 0
        for t in time_to_reach:
            if (t > last_fleet_time):
                last_fleet_time = t
                no_of_fleets += 1
        
        return no_of_fleets