class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._list: list = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._list.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self._list.pop(0)
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self._list[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self._list) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.empty())