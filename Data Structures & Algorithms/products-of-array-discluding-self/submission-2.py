class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        suf = [1] * len(nums)

        pre[0] = nums[0]
        suf[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i]

        for j in range(len(nums) - 1, 0, -1):
            suf[j - 1] = suf[j] * nums[j - 1]
        
        res = []
        for i in range(0, len(nums)):
            if i == 0:
                res.append(suf[1])
            elif i == len(nums) - 1:
                res.append(pre[len(nums) - 2])
            else:
                res.append(pre[i - 1] * suf[i + 1])
        
        return res

