class Twitter:

    def __init__(self):
        self.follows = {}
        self.posts = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if (userId in self.posts):
            self.posts[userId].append(tweetId)
        else:
            self.posts[userId] = [tweetId]
        return None

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = self.posts.get(userId, []).copy()
        res = []
        follows = []
        if (userId in self.follows):
            follows = list(self.follows[userId])

        for per in follows:
            maxHeap = maxHeap + self.posts[per]

        heapq.heapify(maxHeap)
        while len(maxHeap) > 10:
            heapq.heappop(maxHeap)

        while maxHeap:
            ele = heapq.heappop(maxHeap)
            res.append(ele)
        
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if (followerId in self.follows):
            self.follows[followerId].add(followeeId)
        else:
            fls = set()
            fls.add(followeeId)
            self.follows[followerId] = fls
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId in self.follows):
            if (followeeId in self.follows[followerId]):
                self.follows[followerId].remove(followeeId)
        return