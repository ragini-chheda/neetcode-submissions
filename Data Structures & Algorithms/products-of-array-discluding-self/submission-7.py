class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        output=[]
        l=len(nums)
        for i in range(l):
            a=nums
            b=a.pop(i)
            output.append(math.prod(nums))
            a.insert(i,b)
        return output