class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        def isValidMove(curr, nxt):
            diff = 0
            for i, char in enumerate(curr):
                if char != nxt[i]:
                    diff += 1

            return diff == 1

        visited = set(beginWord)
        level = 1
        queue = [beginWord]

        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr == endWord:
                    return level
                for word in wordList:
                    if isValidMove(curr, word) and word not in visited:
                        queue.append(word)
                        visited.add(word)
            level += 1

        return 0
