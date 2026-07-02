class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
        
        output = []
        if zeros == 0:
            prod = 1
            for num in nums:
                prod *= num
            
            for num in nums:
                output.append(int(prod/num))
        elif zeros == 1:
            prod = 1
            for num in nums:
                if num != 0:
                    prod *= num
            
            for num in nums:
                if num != 0:
                    output.append(0)
                else:
                    output.append(int(prod))
        else:
            return [0] * len(nums)

        return output