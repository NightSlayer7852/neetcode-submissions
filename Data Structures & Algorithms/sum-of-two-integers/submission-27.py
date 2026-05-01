class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_int = 0x7fffffff
        mask = 0xffffffff
        while b != 0:
            tmp = ((a & b) << 1) & mask
            a  = (a ^ b) & mask
            b = tmp & mask
        return a if a <= max_int else a - (1 << 32)