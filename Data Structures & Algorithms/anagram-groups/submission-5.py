class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for st in strs:
            count = [0] * 26
            for char in st:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(st)
            
        return list(anagrams.values())