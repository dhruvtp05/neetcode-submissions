class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> freqMap;

        // Count frequencies (fixed += instead of =+)
        for (int i = 0; i < nums.size(); i++) {
            freqMap[nums[i]] += 1;
        }

        // Move map data into a vector of pairs (number, frequency)
        vector<pair<int,int>> freqVector;
        for (auto& p : freqMap) {
            freqVector.push_back({p.first, p.second});
        }

        // Sort by frequency, highest first
        sort(freqVector.begin(), freqVector.end(),
             [](const pair<int,int>& a, const pair<int,int>& b) {
                 return a.second > b.second;
             });

        // Collect top k numbers
        vector<int> result;
        for (int i = 0; i < k; i++) {
            result.push_back(freqVector[i].first);
        }

        return result;
    }
};