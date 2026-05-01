class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        hashset = set()
        res = []
        val = 1
        for i, c in enumerate(s):
            hashset.add(c)
            count[c] -= 1
            if count[c] == 0:
                hashset.remove(c)
            if not hashset:
                res.append(val)
                val = 0
            val += 1
        return res