class Solution:
    def findSource(self, source: str, tickets: List[List[str]]) -> int:
        tempDest = None
        index = 0
        for i in range(len(tickets)):
            if tickets[i][0] == source:
                if not tempDest:
                    tempDest = tickets[i][1]
                    index = i
                else:
                    if (tickets[i][1] < tempDest):
                        index = i
        return index 

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = ["JFK"]
        source = "JFK"

        while (len(tickets) > 0):
            index = self.findSource(source, tickets)
            flight = tickets.pop(index)
            res.append(flight[1])
            source = flight[1]

        return res

            
