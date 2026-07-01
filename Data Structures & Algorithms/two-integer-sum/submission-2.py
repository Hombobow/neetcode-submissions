class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = defaultdict(list)
        for i, num in enumerate(nums):
            if len(num_indices[target - num]) != 0:
                return [num_indices[target - num][0], i]
            num_indices[num].append(i)
