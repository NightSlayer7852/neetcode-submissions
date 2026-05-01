class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        while n != 1:
            if n in hashset:
                return False
            hashset.add(n)
            n = sum(int(x) ** 2 for x in str(n))
            print(n)
        return True