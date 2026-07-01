# 155. Min Stack - medium
'''
    Design a stack that has push, pop, top, and getMin at O(1) time.

    Constraints:
      - Signed int
      - pop, top, getMin will always be called on non-empty stacks, so no error checking if the stack is empty

    My idea is to store the min value along with the value at every push. So instead of just storing an int, we can store a tuple that consists of the value itself and the current min value, which is the just the min value at the top of the stack. We first need to compare the new value against the current min value and push the smaller of the two alongside with the new value.

    Another approach is to use two stacks - one to store the values, and one to store the min values. We only push onto the min stack when a new min is found. We also need to check whether the item we are popping is at the top of the min stack, at which we would also need to pop. This approach is more memory efficient compared to the first approach.
'''
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if self.stack:
            min_value = self.stack[-1][1]
        else:
            min_value = value

        if value <= min_value:
            min_value = value
        
        self.stack.append((value, min_value))

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()