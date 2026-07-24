class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = list(dict.fromkeys(nums))
        nums[:] = unique + list(range( len(nums) - len(unique)   ))
        return len(unique)



# nums [:] = , only modify the original list without creating a new copy and making it point to another address in the memory, so nums [:] is modifying and still points to same address in memory, nums = ... points completely to a new address in memory

#  when using set to get unique elements and so on, it is O(n) but order isn't preserved
#  dict.fromkeys(nums) quickly extracts the unique numbers and put them as keys since keys are always unique in dictionary can't have duplicated keys, then list to extract keys as a list 

# if num in nums within a list is O(n),linear search, so O(n*n), O(n^2) nested loops, Quadratic time
# hashmap/set -> if num in nums is O(1), O(1)* n = O(n), Linear time, that's why hashmap/set preferred in duplicates problems 

