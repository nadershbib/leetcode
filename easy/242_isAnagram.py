# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t) 

# sorted is O(n log n) time complexity < O(n) using frequency counter 

# space complexity for sorted is O(n) since it is creating a new list.

# using frequency counter :) 
# O(n) solution, O(n*3) -> O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = {}
        s2 = {}
        # freq counters for both s / t
        for c in s:
            s1[c] = s1.get(c,0) + 1 
        for c in t:
            s2[c] = s2.get(c,0) + 1

        for char in s1:
            if char not in s2:
                return False
            if s1[char] != s2[char]:
                return False      
        return True
        
        