class Twitter:

    def __init__(self):
        self.follows = {}
        self.posts = {}
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if (userId in self.posts):
            self.posts[userId].append((self.time, tweetId))          
        else:
            self.posts[userId] = [(self.time, tweetId)]
        self.time += 1
        return None

    def getNewsFeed(self, userId: int) -> List[int]:
        my_tweets = self.posts.get(userId, []).copy()
        min_heap = []
        for i in range(len(my_tweets) - 1, -1, -1):
            if (len(my_tweets) - i - 1 > 10):
                break
            else:
                ti, tid = my_tweets[i]
                heapq.heappush(min_heap, (ti, tid))

        # for ti, tid in my_tweets:
        #     heapq.heappush(min_heap, (ti, tid))

        res = []
        follows = []
        if (userId in self.follows):
            follows = list(self.follows[userId])

        for f in follows:
            others_tweets = self.posts.get(f, []).copy()
            
            for i in range(len(others_tweets) - 1, -1, -1):
                if (len(others_tweets) - i - 1 > 10):
                    break
                else:
                    ti, tid = others_tweets[i]
                    heapq.heappush(min_heap, (ti, tid))
        
        for _ in range(len(min_heap)):
            time, tweetId = heapq.heappop(min_heap)
            res.append(tweetId)
        
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
        
