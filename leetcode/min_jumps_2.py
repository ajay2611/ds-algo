"""
https://leetcode.com/problems/jump-game-ii/
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

"""

class Solution:
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        
        left = 0
        right = nums[0]
        count = 1
        
        while right < len(nums) - 1:
            nextt = 0
            for i in range(left, right + 1):
                nextt = max(nextt, i+nums[i])
            
            left, right = right, nextt
            count += 1
            
        return count

    def jump_dp(self, nums):
        min_jumps = [0] * len(nums)
        index = 0
        
        for i in range(0, len(nums)):
            value = i + nums[i]
            for k in range(index + 1, value + 1):
                if k > len(nums) - 1:
                    break
                if min_jumps[k]:
                    min_jumps[k] = min(min_jumps[k], min_jumps[i] + 1)
                else:
                    min_jumps[k] = min_jumps[i] + 1
                
            index = max(index, value)
              
        return min_jumps[-1]


if __name__ == '__main__':
    nums = [2,3,1,1,4]
    print(Solution().jump(nums))