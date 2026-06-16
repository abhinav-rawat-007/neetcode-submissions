class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for char in strs:
            key = tuple(sorted(char))
            if key in groups:
                groups[key].append(char)
            else:
                groups[key] = [char]
        return list(groups.values())
        



        