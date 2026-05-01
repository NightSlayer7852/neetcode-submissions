class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        hand.sort()
        for x in hand:
            if count[x] == 0:
                continue
            for i in range(groupSize):
                if count[x + i] == 0:
                    return False
                count[x + i] -= 1
        return True
