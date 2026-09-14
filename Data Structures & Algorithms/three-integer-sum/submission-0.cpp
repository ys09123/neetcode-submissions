class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();

        sort(nums.begin(), nums.end());

        vector<vector<int>> ans;

        for (int i = 0; i < n - 2; i++) {

            // Skip duplicate i
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            int j = i + 1;
            int k = n - 1;

            while (j < k) {

                int sum = nums[i] + nums[j] + nums[k];

                if (sum < 0) {
                    j++;
                }
                else if (sum > 0) {
                    k--;
                }
                else {
                    ans.push_back({nums[i], nums[j], nums[k]});

                    // Skip duplicate j
                    while (j < k && nums[j] == nums[j + 1])
                        j++;

                    // Skip duplicate k
                    while (j < k && nums[k] == nums[k - 1])
                        k--;

                    j++;
                    k--;
                }
            }
        }

        return ans;
    }
};