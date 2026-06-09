class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set()
        for i in wordDict:
            wordSet.add(i)

        res = []
        sentence= []
        def backTrack(i):
            if i >=len(s):
                copy = ' '.join(sentence)
                res.append(copy)
                return

            result = []
            for j in range(i,len(s)):
                if s[i:j+1] in wordSet:
                    sentence.append(s[i:j+1])
                    backTrack(j+1)
                    sentence.pop()
        backTrack(0)
        return res

            