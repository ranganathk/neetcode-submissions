class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tempPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                curr_path_price = prices[s] + p
                if curr_path_price < tempPrices[d]:
                    tempPrices[d] = curr_path_price
            
            prices = tempPrices
        
        if (prices[dst] == float("inf")):
            return -1
        
        return int(prices[dst])
