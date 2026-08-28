from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_anagrams = defaultdict(list)
        for st in strs:
            sorted_string = ''.join(sorted(st))
            sorted_anagrams[sorted_string].append(st)
        return list(sorted_anagrams.values())
        