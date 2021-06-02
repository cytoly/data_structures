class Stack:
    def __init__(self, limit=5):
        self.limit = limit
        self.__top = -1
        self.__stk = []

    def is_empty(self):
        return self.__top <= -1

    def push(self, data):
        if self.__top >= self.limit:
            raise OverflowError("stack limit reached")
        self.__top += 1
        self.__stk.append(data)

    def pop(self):
        if self.is_empty():
            return print("StackUnderFlow!")
        self.__top -= 1
        return self.__stk.pop()

    def peek(self):
        if self.is_empty():
            return print("StackUnderFlow!")
        return self.__stk[self.__top]

    def size(self) -> int:
        return self.__top + 1


if __name__ == "__main__":
    stk = Stack(20)
    stk.push(2)
    stk.push(3)
    stk.push(5)
    print(stk.size())
    print(stk.is_empty())
    print(stk.peek())
    print(stk.pop())
    print(stk.pop())
    print(stk.pop())
    print(stk.is_empty())
