from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            sumCalc = numbers[i] + numbers[j]

            if sumCalc < target:
                i += 1
            elif sumCalc > target:
                j -= 1
            else:
                return [i + 1, j + 1]

