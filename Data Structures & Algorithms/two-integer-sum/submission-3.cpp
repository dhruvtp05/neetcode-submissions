class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> diffs;
        int currentDiff;
        for (int i = 0; i < nums.size(); i++)
        {
            currentDiff = target - nums[i];
            if (diffs.count(currentDiff))
            {
                return {diffs[currentDiff], i};
            }
            diffs.insert({nums[i], i});

        }
        return {};
    }
};
