class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # initial check for length
        if len(s) != len(t):
            return False

        # build frequency array
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        # if any vals is not 0 then it cannot be an anagram
        for val in count:
            if val != 0:
                return False
        return True

