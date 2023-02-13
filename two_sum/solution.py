from typing import List, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Tuple[int, int]:
        unique_numbers = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            temp_target = target - num

            if num != temp_target and temp_target in unique_numbers:
                return i, unique_numbers[temp_target]
            elif num == temp_target and unique_numbers[num] != i:
                return i, unique_numbers[num]
            else:
                continue
