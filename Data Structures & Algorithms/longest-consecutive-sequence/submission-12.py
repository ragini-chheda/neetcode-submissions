class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a=sorted(list(set(nums)))
        print(a)
        c=0
        b=0
        for index in range(1,len(a)):
            if a[index]==a[index-1]+1:
                c=c+1
                if c>b:
                    b=c
            else:
                c=0
        if nums!=[]:
            b=b+1
        return b