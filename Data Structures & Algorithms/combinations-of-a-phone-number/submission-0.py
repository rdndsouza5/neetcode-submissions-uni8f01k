class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.mp = {
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8": ['t','u','v'],
            "9":['w','x','y','z'],
        }
        self.res = []
        self.backTrack([],0, digits)
        return self.res

    def backTrack(self,cur: List[str], i: int, digits: str):
        if len(cur)==len(digits) or i >= len(digits):
            self.res.append(''.join(cur))
            return
        print(i)
        print(digits[i])
        for char in self.mp[str(digits[i])]:
            cur.append(char)
            self.backTrack(cur, i+1, digits)
            cur.pop()
