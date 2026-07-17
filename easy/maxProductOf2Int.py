class Solution:
    def maxProduct(self,n) -> int:
        biggest2digits = sorted(str(n))[-2:]
        return int(biggest2digits[0])*int(biggest2digits[1])



print(Solution().maxProduct(54321))


# sorting is O(n log(n) )
# doable in O(n) with tracking biggest 2 digits while iterating