import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs={}
        heap=[]
        for num in nums:
            freqs[num]=freqs.get(num,0)+1
        
        for num,count in freqs.items():
            heapq.heappush(heap,(count,num))
        
        return [num for count, num in heapq.nlargest(k, heap)]