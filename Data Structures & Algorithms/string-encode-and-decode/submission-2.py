class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            s=s+i+'\n'
        return s
    def decode(self, s: str) -> List[str]:
        l=s.split('\n')
        l.pop()
        return l