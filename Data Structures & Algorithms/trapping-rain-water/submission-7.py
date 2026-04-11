class Solution:
    def trap(self, height: List[int]) -> int:
        l,r,water=0,len(height)-1,0
        maxl,maxr=height[0],height[r]
        while(l<r):
            if maxl<maxr:
                l+=1
                maxl=max(maxl,height[l])

                water+=maxl-height[l]
            else:
                r-=1
                maxr=max(maxr,height[r])
                water+=maxr-height[r]
        return water
                


            
                