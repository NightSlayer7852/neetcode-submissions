class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)
    
    def build(self, nums, idx, l, r):
        if l == r:
            self.tree[idx] = nums[l]
            return 
        mid = (l + r) // 2
        self.build(nums, 2 * idx + 1, l, mid)
        self.build(nums, 2 * idx + 2, mid + 1, r)
        self.tree[idx] = max(self.tree[2 *idx + 1],  self.tree[2 * idx + 2])

    def query(self, idx, l, r, ql, qr):
        if r < ql or l > qr:
            return float('-inf')
        
        if ql <= l and r <= qr:
            return self.tree[idx]
        
        mid = (l + r) // 2
    
        return max(
            self.query(2 * idx + 1, l, mid, ql, qr),
            self.query(2 * idx + 2, mid + 1, r, ql, qr),
        )

    def update(self, idx, l, r, pos, val):
        if l == r:
            self.tree[idx] = val
            return 

        mid = (l + r) // 2

        if pos <= mid:
            self.update(2 * idx + 1, l, mid, pos, val)
        else:
            self.update(2 * idx + 2, mid + 1, r, pos, val)
        
        self.tree[idx] = max(self.tree[2 * idx + 1], self.tree[2 * idx + 2])
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        segTree = SegmentTree(nums)
        res = []
        for i in range(segTree.n - k + 1):
            res.append(segTree.query(0, 0 ,segTree.n - 1, i, i + k - 1))
        return res