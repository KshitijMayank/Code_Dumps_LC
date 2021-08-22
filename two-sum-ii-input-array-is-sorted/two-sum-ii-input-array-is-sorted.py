class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            d[numbers[i]] = i+1
        for i in range(len(numbers)):
            rem = target - numbers[i]
            if rem in d and d[rem] != i:
                return [i+1,d[rem]]
        
        