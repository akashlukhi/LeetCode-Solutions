class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        max_len = 0
        start_index = 0
        for i in range(0, len(s)):
            if s[i] in d:
                start_index = max(start_index, d[s[i]] + 1)

            max_len = max(max_len, i-start_index + 1)
            d[s[i]] = i
        return max_len
