class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        ShortestWord = min(strs,key=len)
        for i,c in enumerate(ShortestWord):
            for j in range(len(strs)):
                if c != strs[j][i]:
                    return commonPrefix
            commonPrefix+=c
        return commonPrefix

print(Solution().longestCommonPrefix(["dog","racecar","car"]))

# O(n*m) since shortest word length (n) is different than the number of strings left to check (m) -> n*m

# min(strs,key = len) to get shortest word in python 