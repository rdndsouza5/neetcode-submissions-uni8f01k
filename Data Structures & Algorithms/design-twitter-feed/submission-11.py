class Twitter:

    def __init__(self):
        self.count = 0
        self.followerMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []
        print(self.followerMap[userId])
        followees = self.followerMap[userId].copy()
        followees.add(userId)
        for folowee in followees:
            if self.tweetMap[folowee]:
                pos = len(self.tweetMap[folowee])
                pos -=1
                if pos>=0:
                    cnt, tweetId = self.tweetMap[folowee][pos]
                    heapq.heappush(maxHeap, [cnt, tweetId,folowee, pos])
      
        limit = 10
        print(maxHeap)
        while maxHeap and limit:
            cnt, tweetId, followeeId, pos = heapq.heappop(maxHeap)
            pos -=1
            if pos>=0:
                cnt, tweetId2 = self.tweetMap[followeeId][pos]
                heapq.heappush(maxHeap,[cnt, tweetId2, followeeId, pos])
            res.append(tweetId)
            limit -=1
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)