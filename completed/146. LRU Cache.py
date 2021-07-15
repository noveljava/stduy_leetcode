class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_info = []
        self.memory = {}

    def get(self, key: int) -> int:
        if key not in self.lru_info:
            return -1

        self.lru_info.remove(key)
        self.lru_info.insert(0, key)

        return self.memory[key]

    def put(self, key: int, value: int) -> None:
        if len(self.lru_info) == self.capacity and key not in self.lru_info:
            self.lru_info.pop()

        if key in self.lru_info:
            self.lru_info.remove(key)

        self.lru_info.insert(0, key)
        self.memory[key] = value

        return None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    # lRUCache = LRUCache(2)
    # lRUCache.put(1, 1)  # cache is {1 = 1}
    # lRUCache.put(2, 2)  # cache is {1 = 1, 2 = 2}
    # assert 1 == lRUCache.get(1)  # return 1
    # lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    # assert -1 == lRUCache.get(2)  # returns - 1(not found)
    # lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    # assert -1 == lRUCache.get(1)  # return -1(not found)
    # assert 3 == lRUCache.get(3)  # return 3
    # assert 4 == lRUCache.get(4)  # return 4

    lRUCache = LRUCache(2)
    assert -1 == lRUCache.get(2)
    lRUCache.put(2, 6)
    assert -1 == lRUCache.get(1)
    lRUCache.put(1, 5)
    lRUCache.put(1, 2)
    assert 2 == lRUCache.get(1)
    assert 6 == lRUCache.get(2)
