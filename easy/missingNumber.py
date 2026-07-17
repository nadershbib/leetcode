# brute force approach 
# https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        n = len(nums)
        # Gaussian formula, sum one up to N -> n(n+1) / 2
        sumZeroToN = n*(n+1) // 2 
        return sumZeroToN - totalSum 
    

# brute force approach O(n^2), since remove runs a loop to find the element it wants to delete, so nested loops

def missingNum (nums):
    numsZeroToN = [i for i in range(len(nums) +1 )]
    for num in nums:
       numsZeroToN.remove(num)
    return numsZeroToN[0]


print(missingNum([0,3,2]))
    