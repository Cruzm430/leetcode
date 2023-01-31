#https://leetcode.com/problems/running-sum-of-1d-array/?envType=study-plan&id=level-1

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum_array = []
        previous_sum = 0
        for idx in range(len(nums)):
            running_sum_array.append(previous_sum + nums[idx])
            previous_sum = previous_sum + nums[idx]

        return running_sum_array
            