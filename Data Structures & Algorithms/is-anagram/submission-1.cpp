class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) { return false; }
        map<char, int> firstMap;
        for (char c : s)
        {
            firstMap[c] += 1;
        }
        map<char,int> secondMap;
        for (char c : t)
        {
            secondMap[c] += 1;
        }
        return (firstMap == secondMap);
    }
};
