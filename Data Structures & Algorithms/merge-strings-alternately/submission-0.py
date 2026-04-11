class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        l,m= len(word1),len(word2)

        for i in range(max(l,m)):
            if i< l:
                res+=word1[i]
            if i< m:
                res+=word2[i]
        return res