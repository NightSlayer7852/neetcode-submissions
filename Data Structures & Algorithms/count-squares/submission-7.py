class CountSquares:

    def __init__(self):
        self.hashmap = defaultdict(int)
        self.hashset = set()

    def add(self, point: List[int]) -> None:
        x, y = point
        self.hashset.add((x, y))
        self.hashmap[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point
        for nx, ny in self.hashset:
            if x != nx and y != ny and abs(x - nx) == abs(y - ny) :
                if (nx, y) in self.hashset and (x, ny) in self.hashset:
                    print(x,y)
                    print(nx, ny)
                    print(nx, y)
                    print(x, ny)
                    a, b, d = self.hashmap[(nx, ny)], self.hashmap[(nx, y)], self.hashmap[(x, ny)]
                    print(a, b, d)
                    res += a * b * d
        return res