# https://leetcode.com/problems/matrix-diagonal-sum/


def diagonalSum(List):
        length = len(List)
        middle = length // 2 
        isOdd = length % 2 == 1 
        sum = 0
        for i in range(len(List)):
            sum+=List[i][i]
            if  isOdd and i == middle:
                continue
            sum+=List[i][length - i - 1]
        return sum

print(diagonalSum(
    [
             [7,3,1,9],
             [3,4,6,9],
             [6,9,6,6],
             [9,5,8,5]
    ]))


        