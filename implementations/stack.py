# array implementation
class Stack(object):
    def __init__(self, limit=5):
        self.limit = limit
        self.stk = []

    def is_empty(self):
        return len(self.stk) <= 0

    def push(self, data):
        if len(self.stk) >= self.limit:
            raise OverflowError("stack limit reached")
        self.stk.append(data)

    def pop(self):
        if self.is_empty():
            return print("StackUnderFlow!")
        return self.stk.pop()

    def peek(self):
        if self.is_empty():
            return print("StackUnderFlow!")
        return self.stk[-1]

    def size(self) -> int:
        return len(self.stk)


if __name__ == "__main__":
    stk = Stack(3)

    # inserting the elements
    stk.push(1)
    stk.push(2)
    stk.push(3)

    # popping and peeking
    print(stk.peek()) # 3
    item = stk.pop()
    print(item) # 3
    print(stk.peek())
    print(stk.size())
    print(stk.is_empty()) # False