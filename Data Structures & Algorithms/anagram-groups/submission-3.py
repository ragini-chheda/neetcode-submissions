class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort(key=lambda w: sorted(w))
        result = []
        current_group = []
        for i in range(len(strs)):
            if i > 0 and sorted(strs[i]) != sorted(strs[i-1]):
                result.append(current_group)
                current_group = []
            current_group.append(strs[i])
        if current_group:
            result.append(current_group)
        return result