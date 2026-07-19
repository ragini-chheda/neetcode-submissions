class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        a=[]
        print(d)
        for i in range(k):
            key=list(d.keys())
            val=list(d.values())
            b=max(val)
            a.append(key[val.index(b)])
            del d[key[val.index(b)]]
        return a

