# class Solution:
#     def isValid(self, s: str) -> bool:
#         open = {"(","[","{"}
#         close = {")","]","}"}
#         valid = {"()","{}","[]"}
#         stack = []
#         for c in s:
#             if not stack:
#                 if c in open:
#                     stack.append(c)
#                     continue
#                 else:
#                     return False
            
#             if stack[-1] in open and c in close:
#                 if stack[-1]+c in valid:
#                     stack.pop()
#                     continue
#                 else:
#                     return False
#             stack.append(c)
#         if not stack:
#             return True
#         return False


# print(Solution().isValid("()[]{}"))


# optimized solution/ using dictionary for the pairs
# solved 7 / 30 / 2026
class Solution:
    def isValid(self,s:str) -> bool:
        pairs = { "(":")","{":"}","[":"]"}
        stack = []
        for c in s:
            if not stack:
                if c in pairs:
                    stack.append(c)
                    continue
                return False
            if c in pairs:
                stack.append(c)
            elif c == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack
             

# iterating once, O(n) time complexity, space complexity O(1) no extra space added
