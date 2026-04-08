class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums={}
        
        for i,num in enumerate(nums):
            complement= target-num
            if complement in sums:
                return [sums[complement],i]
            sums[num] = i