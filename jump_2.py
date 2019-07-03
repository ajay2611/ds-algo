class Solution:        
    def jump(self, nums: List[int]) -> int:
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