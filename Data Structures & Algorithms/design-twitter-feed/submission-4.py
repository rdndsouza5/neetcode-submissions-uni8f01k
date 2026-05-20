class Twitter:

    def __init__(self):
        self.count = 0
        self.followerMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.tweetMap[userId].append([self.count, tweetId])
        self.count  -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        self.followerMap[userId].add(userId)
        minHeap = []
        for followeeId in self.followerMap[userId]:
            print(followeeId)
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) -1
                
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count,tweetId,  followeeId, index-1])
       
        print("minheap", minHeap)
        heapq.heapify(minHeap)
        maxItems = 10
        while len(res)<10 and minHeap:
            print(minHeap)
            count, tweetId, followeeId, nextIdx = heapq.heappop(minHeap)
            if nextIdx >=0:
                count2, tweetId2 = self.tweetMap[followeeId][nextIdx]
                heapq.heappush(minHeap, [count2, tweetId2, followeeId, nextIdx -1 ])
            res.append(tweetId)
            maxItems-=1
            
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
        
