class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

            You may assume that each input would have exactly one solution, and you may not use the same element twice.

            You can return the answer in any order.
        '''
        for First_loop in range(0,len(nums)):
            for second_loop in range ((First_loop + 1),len(nums)):
                if(nums[First_loop] + nums[second_loop] == target):
                    return (First_loop,second_loop)