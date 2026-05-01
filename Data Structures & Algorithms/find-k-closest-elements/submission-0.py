class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        score = 0
        for i in range(k):
            score += abs(arr[i] - x)
        
        res = [0, k]

        for r in range(k, len(arr)):
            temp = score
            temp -= abs(arr[r - k] - x)
            temp += abs(arr[r] - x)
            if temp < score:
                res = [r - k + 1, r + 1]
            
        return arr[res[0] : res [1]]