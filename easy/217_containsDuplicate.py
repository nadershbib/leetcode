# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(list(dict.fromkeys(nums))) != len(nums)


# print(Solution().containsDuplicate())


# order doesn't matter so set is totally acceptable here.

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(set(nums)) != len(nums)


# longer cute way, better for interviews


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#        unique  = set()
#        for num in nums:
#             if num in unique:
#                 return True
#             unique.add(num)
#        return False
            