# Quick-Union algorithm for Union-Find
# Arda Sonmez github.com/sonmezarda

class QuickUnion:
    def __init__(self, point_count):
        self.id = []
        for i in range(point_count):
            self.id.append(i)

    def get_root(self, point):
        while(self.id[point] != point): 
            point = self.id[point]
        
        return point

    def is_connected(self, p1, p2):
        return self.get_root(p1) == self.get_root(p2)

    def union(self, p1, p2):
        p1_root = self.get_root(p1)
        p2_root = self.get_root(p2)
        self.id[p1_root] = p2_root

#----
my_quick_union = QuickUnion(10)

my_quick_union.union(4, 2)
my_quick_union.union(5, 4)
my_quick_union.union(9, 5)

my_quick_union.union(7, 6)
my_quick_union.union(8, 6)

print(my_quick_union.is_connected(7, 8))
print(my_quick_union.is_connected(9, 2))
print(my_quick_union.is_connected(9, 1))