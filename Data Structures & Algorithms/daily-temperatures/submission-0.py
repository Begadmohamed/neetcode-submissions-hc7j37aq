class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        count=[0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                index= stack[-1]
                count[index]= i-index
                stack.pop()
            stack.append(i)
        return count
            
