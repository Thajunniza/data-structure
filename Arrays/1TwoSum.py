"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1] 
"""
## this is a sequential check
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind1 = 0
        ind2 = 1
        rtype = []
        for n in range(len(nums)):
            if(ind2) >= len(nums):
                return rtype
            if nums[ind1] + nums[ind2] == target:
                rtype = [ind1,ind2]
                return rtype
            ind1 += 1
            ind2 += 1

    
nums = [2,7,4,1,11,15]
print(twoSum(nums,5))    

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
nums = [2,7,11,15]
print(twoSum(nums,9)) 

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
nums = [3,2,4]
print(twoSum(nums,6))

# Input: nums = [3,1,3], target = 6
# Output: [0,1] 
nums = [3,1,3]
print(twoSum(nums,6))