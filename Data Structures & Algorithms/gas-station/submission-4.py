class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum (cost):
            return -1
        total = 0
        index = 0
        for i in range(n):
            g, c = gas[i], cost[i]
            total += g - c
            if total < 0:
                total = 0
                index = i + 1
        return index