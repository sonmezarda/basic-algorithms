# Quick-Find algorithm for Union-Find
# Arda Sonmez github.com/sonmezarda

class QuickFind:
    def __init__(self, point_count):
        self.id = []
        for i in range(point_count):
            self.id.append(i)

    def is_connected(self, p1, p2):
        return self.id[p1] == self.id[p2]

    def union(self, p1, p2):
        p1id = self.id[p1]
        p2id = self.id[p2]
        for i in range(len(self.id)):
            if self.id[i] == p2id:
                self.id[i] = p1id

#----
my_quick_find = QuickFind(10)

my_quick_find.union(4, 2)
my_quick_find.union(5, 4)
my_quick_find.union(9, 5)

my_quick_find.union(7, 6)
my_quick_find.union(8, 6)

print(my_quick_find.is_connected(7, 8))
print(my_quick_find.is_connected(9, 2))
print(my_quick_find.is_connected(9, 1))