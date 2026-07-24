class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInt = {
            "I":1,
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "XL":40,
            "L":50,
            "XC":90,
            "C":100,
            "CD":400,
            "D":500,
            "CM":900,
            "M":1000
        }

        sum = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and (s[i]+s[i+1]) in romanToInt:
                sum+=romanToInt[s[i]+s[i+1]]
                i+=2
            else:
                sum+=romanToInt[s[i]]
                i+=1
        return sum


print(Solution().romanToInt("III"))

# O(n) iterating once over the string, O(1) space complexity 
# a clever solution would be is if current element < next element, you substract current from total, Ex: IV = 4, which is -1 + 5 = 4, see ? same value 4 , very clever solution.
    











