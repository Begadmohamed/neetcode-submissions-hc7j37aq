class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsMap= {}
        for num in nums:
            if num in numsMap :
                return True
            else:
                numsMap[num]=1
        return False
