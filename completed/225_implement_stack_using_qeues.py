class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._list: list = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._list.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self._list.pop()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._list[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self._list) == 0
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.top()
param_3 = obj.pop()
param_4 = obj.empty()

print(param_2)
print(param_3)
print(param_4)
