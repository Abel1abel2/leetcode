class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest=0
        subs=set()
        n=len(s)
        for r in range(n):
            while s[r] in subs:
                subs.remove(s[l])
                l+=1
            longest=max(longest,r-l+1)
            subs.add(s[r])
        return longest
