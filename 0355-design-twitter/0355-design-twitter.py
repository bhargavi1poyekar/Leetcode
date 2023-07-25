class Twitter:

    def __init__(self):
        self.count=0
        self.tweetMap=defaultdict(list)  #userId - [[count,tweetId]]
        self.followMap=defaultdict(set) #userId - followerId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count,tweetId))
        self.count-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap=[]
        recent_tweets=[]
        self.followMap[userId].add(userId)
        for follower in self.followMap[userId]:
            if follower in self.tweetMap:
                idx=len(self.tweetMap[follower])-1
                count,tweetId=self.tweetMap[follower][idx]
                max_heap.append([count,tweetId,follower,idx-1])
        
        heapq.heapify(max_heap)

        while max_heap and len(recent_tweets)<10:
            count,tweetId,follower,index=heapq.heappop(max_heap)
            recent_tweets.append(tweetId)
            if index>=0:
                count, tweetId = self.tweetMap[follower][index]
                heapq.heappush(max_heap,[count,tweetId,follower,index - 1]) 
        return recent_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)