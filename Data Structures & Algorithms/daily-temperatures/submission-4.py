class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            cur = 0
            maxTmp = temperatures[i]
            for j in range(i+1, len(temperatures)):
                cur+=1
                maxTmp= max(maxTmp, temperatures[j])
                if temperatures[i]<temperatures[j]:
                    break
            if temperatures[i]==maxTmp:
                res.append(0)
            else:
                res.append(cur)

        return res