class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> checkedNums;
        for (int i = 0; i < nums.size(); i++)
        {
            if (checkedNums.count(nums.at(i)))
            {
                return true;
            }
            checkedNums.insert(nums.at(i));
        }
        return false;
    }
};
