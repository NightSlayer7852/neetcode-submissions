class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list) # userId -> [[ time, tweetId]]
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if len(self.tweetMap[followeeId]) > 0:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                minheap.append([time, tweetId, followeeId, index - 1])
        heapq.heapify(minheap)
        while minheap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minheap)
            res.append(tweetId)
            if index >= 0:
                ntime, ntweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minheap, [ntime, ntweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
