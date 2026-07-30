class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        shortestWord = min(strs,key=len)
        for i,c in enumerate(shortestWord):
            for j in range(len(strs)):
                if c == strs[j][i]:
                    continue
                else:
                    return commonPrefix
            commonPrefix+=c
        return commonPrefix

print(Solution().longestCommonPrefix(["dog","racecar","car"]))

# O(n*m) checking common prefix accross all strings, it is O(n*m) since it could be terminated as soon as we find something that is not common

# min(strs,key = len) to get shortest word in python 