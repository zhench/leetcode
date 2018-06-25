
import datetime
import collections
# from nums import numsbig


class Solution(object):
    def removeDuplictes(self, nums):
        """
        :type nums: List[int]
        :rtype :int
        """
        i = 0
        flagNum = None
        for num in nums:
            if flagNum != num:
                nums[i] = num
                flagNum = num
                i += 1
        return i

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                result += prices[i + 1] - prices[i]

        return result

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dics = collections.Counter(nums)
        print(type(dics))
        for item in dics:
            print(dics[item])
        for dic in dics.values():
            if dic > 1:
                return True
        return False

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a = 0
        for i in nums:
            a ^= i
        return a

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums = []
        if len(nums1) > len(nums2):
            for num in nums2:
                if num in nums1:
                    nums.append(num)
        else:
            for num in nums1:
                if num in nums2:
                    nums.append(num)
        return nums

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        strnums = [str(num) for num in nums if num != 0]
        nums[:] = [int(i) for i in strnums] + [0] * (len(nums) - len(strnums))

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        raw = [{},{},{},{},{},{},{},{},{}]  
        col = [{},{},{},{},{},{},{},{},{}]  
        cell = [{},{},{},{},{},{},{},{},{}]  
          
        for i in range(9):  
            for j in range(9):                                   
                num = (3*(i//3) + j//3)#找单元  
                temp = board[i][j]  
                if temp != ".":  
                    if temp not in raw[i] and temp not in col[j] and temp not in cell[num]:  
                        raw [i][temp] = 1  
                        col [j][temp] = 1  
                        cell [num][temp] =1  
                    else:  
                        return False      
        return True
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()#需要镜像一下，才能完成顺时针旋转90度
        matrix[:]=map(list,zip(*matrix))


if __name__ == "__main__":
    start = datetime.datetime.now()

    nums2 = [1, 2, 3, 4]
    nums4 = [0, 0, 1]
    sol = Solution()
    # i = sol.singleNumber(nums)
    # nums1=sol.intersect(nums,nums2)
    # print(nums1)
    end = datetime.datetime.now()
    # print(i)
    print(end - start)
    print('test')
    sol.moveZeroes(nums4)
    print(nums4)

    board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

    print(sol.isValidSudoku(board))

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol.rotate(matrix)
    print(matrix)
