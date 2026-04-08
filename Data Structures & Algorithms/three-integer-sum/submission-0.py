class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        size = len(nums)
        # Fix i and move j&k like a 2sum question
        # where nums[j]+nums[k]=-nums[i](Target)
        for i in range(size - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = size - 1
            target = -nums[i]

            while j < k:
                s = nums[j] + nums[k]

                if s == target:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif s < target:
                    j += 1
                else:
                    k -= 1

        return triplets