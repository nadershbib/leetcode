# https://leetcode.com/problems/unique-middle-element/


# one liner is better, count is already O(n), no need for a manual for loop
class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
           middleElement = nums[len(nums) // 2]
           count = 0
           for num in nums:
                if num == middleElement:
                     count+=1
                     if count > 1:
                          return False 
           return True
                    



print(Solution().isMiddleElementUnique([1,2,3,4,3]))