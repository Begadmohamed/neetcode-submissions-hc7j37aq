class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #x=(target-pos)/speed
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack=[]
        count=0
        for pos, spd in cars:
            time = (target - pos) / spd
            if stack and time <= stack[-1]:
                continue
            elif stack and time > stack[-1]:
                stack.append(time)
            else:
                stack.append(time)
        return len(stack)

