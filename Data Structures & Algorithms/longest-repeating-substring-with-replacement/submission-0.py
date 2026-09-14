class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}

        maxi = 0
        l = 0
        r = 0
        n = len(s)
        maxFreq = 0

        while r < n:
            mp[s[r]] = 1 + mp.get(s[r], 0)
            maxFreq = max(maxFreq, mp[s[r]])

            while (r - l + 1) - maxFreq > k:
                mp[s[l]] -= 1
                l += 1
            
            maxi = max(maxi, r - l + 1)
            r += 1
        
        return maxi