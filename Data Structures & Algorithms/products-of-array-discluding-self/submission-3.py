class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        zeroExist= False
        numsExist= False
        z=0
        output=[0]*len(nums)
        for num in nums:
            if num !=0:
                product *= num
                numsExist=True
            else:
                zeroExist=True
                z+=1
                continue
        for i, num in enumerate(nums):
            if num!=0:
                if not zeroExist:
                    output[i]=product//num
                else:
                    output[i]=0
            if num==0 and not numsExist:
                output[i]=0
            elif num==0 and numsExist and z==1:
                output[i]=product
            elif num==0 and numsExist and z>1:
                output[i]=0
        return output
                