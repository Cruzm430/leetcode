#https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0 
        right_sum = sum(nums)
        for idx, num in enumerate(nums):
            right_sum -= num
            if left_sum == right_sum:
                return idx
            else:
                left_sum += num
        else:
            return -1
