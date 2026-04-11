class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        countZero=0
        for num in nums:
            if num==0:
                countZero+=1
                continue
            product =num*product
        res=[]
     
        for i in  nums:
            if countZero>1:
                res.append(0)
            elif i==0:
                res.append(product)
            elif countZero==1:
                res.append(0)
            else:
                res.append(int(product/i))
        return res
        
        