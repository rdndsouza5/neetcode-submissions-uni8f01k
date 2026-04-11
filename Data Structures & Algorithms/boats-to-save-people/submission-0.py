class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i,j=0, len(people)-1
        count=0
        people.sort()
        while i<=j:
          
            if people[i]+people[j]>limit:
                j-=1
                count+=1
            else:
                i+=1
                j-=1
                count+=1
        return count