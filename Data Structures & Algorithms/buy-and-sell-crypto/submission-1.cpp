class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();
        int maxProfit = 0;
        int day = prices[0];
        int diff;
        
        for (int i = 0; i < length; i++)
        {
            diff = prices[i] - day;
            maxProfit = max(diff, maxProfit);

            if (diff <= 0)
            {
                day = prices[i];
            }
        }
        return maxProfit;
    }
};
