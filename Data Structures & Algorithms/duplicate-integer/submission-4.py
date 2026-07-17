class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c=sorted(nums)
        f=False
        for i in range(len(c)-1):
            if c[i]==c[i+1]:
                f=True
        return f
