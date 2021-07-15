class MyCircularQueue:

    def __init__(self, k: int):
        self._list: list = [0] * k
        self._max_number = k
        self._front_index = 0
        self._rear_index = -1

    def enQueue(self, value: int) -> bool:
        if self._front_index == self._rear_index:
            return False

        self._list[self._front_index] = value

        if self._rear_index == -1:
            self._rear_index = self._front_index

        self._front_index = (self._front_index+1) % self._max_number
        return True

    def deQueue(self) -> bool:
        if self._rear_index == -1:
            return False

        self._rear_index = (self._rear_index+1) % self._max_number
        if self._rear_index == self._front_index:
            self._rear_index = -1

        return True

    def Front(self) -> int:
        return -1 if -1 == self._rear_index else self._list[self._rear_index]

    def Rear(self) -> int:
        return -1 if -1 == self._rear_index else self._list[((self._front_index-1)%self._max_number)]

    def isEmpty(self) -> bool:
        return -1 == self._rear_index

    def isFull(self) -> bool:
        return self._rear_index == self._front_index
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# Me : [null,true,4,true,true,9,true,false,false,false,true,true]
# Expected : [null,true,4,true,true,9,true,false,true,false,true,true]

obj = MyCircularQueue(2)
print(obj.enQueue(4))
print(obj.Rear())
print(obj.enQueue(9))
print(obj.deQueue())
print(obj.Front())
print(obj.deQueue())
print(obj.deQueue())
print(obj.isEmpty())
print(obj.deQueue())
print(obj.enQueue(6))
print(obj.enQueue(4))
[[2],[4],[],[9],[],[],[],[],[],[],[6],[4]]