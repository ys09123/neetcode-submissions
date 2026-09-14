class Solution {
public:
    int maxArea(vector<int>& heights) {
        int n = heights.size();
        int l = 0, r = n - 1;
        int ans = 0;
        while(l < r) {
            int breadth = min(heights[l], heights[r]);
            int length = r - l;

            int area = breadth * length;
            ans = max(ans, area);

            if(heights[l] < heights[r]) l++;
            else r--;
        }
        return ans;
    }
};
