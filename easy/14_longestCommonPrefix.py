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


# the top solution is basically sort them list of strings, compare first and last word characters if they're matching everthing else in between should be matching, since when you sort list of strings alphabetically everything should be close to each other to the other words, so taking first and last word are the furthest from each other from alphabetical order hence you should compare those 2, if there's a mismatch you terminate, if not all words in between would fucking align when it comes to the prefix.

