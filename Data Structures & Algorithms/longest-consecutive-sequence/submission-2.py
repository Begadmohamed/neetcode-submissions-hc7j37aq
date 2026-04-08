class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len=0
        mem=set()
        boundaries={}
        for num in nums:
            if num in mem:
                continue
            mem.add(num)
            # get boundaries of sequence
            left = boundaries.get(num - 1, 0)  
            right = boundaries.get(num + 1, 0) 
            total = left + right + 1           

            
            boundaries[num - left] = total
            boundaries[num + right] = total
            boundaries[num] = total

            max_len = max(max_len, total)

        return max_len