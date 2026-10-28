import heapq

class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.follows = defaultdict(set)
        self.postTime = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.posts[userId], (self.postTime, tweetId))
        self.postTime += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        fullList = self.posts[userId].copy()
        for followee in self.follows[userId]:
            fullList.extend(self.posts[followee])
        return list(map(lambda x: x[1], heapq.nlargest(10, fullList)))

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
            self.follows[followerId].remove(followeeId)
        except KeyError:
            pass
        
