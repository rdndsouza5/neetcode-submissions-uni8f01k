class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)

        res = []
        memo = {}
        def backTrack(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return [""]

            result = []
            for j in range(i+1,len(s)+1):
                word = s[i:j]
                if word in wordSet:
                    suffixes = backTrack(j)
                    
                    for suffix in suffixes:
                        if suffix:
                            result.append(word + " " + suffix)
                        else:
                            result.append(word)
            memo[i] = result
            return result
        return backTrack(0)

            