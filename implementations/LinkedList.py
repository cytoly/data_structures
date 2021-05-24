from typing import Union


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Union[Node, ()] = None

    def has_next(self) -> bool:
        return self.next is not None


class LinkedList:
    def __init__(self):
        self.head: Union[Node, ()] = None
        self.length = 0

    def __len__(self) -> int:
        # current_node = self.head
        # count = 0
        # while current_node is not None:
        #     count += 1
        #     current_node = current_node.next
        # return count
        return self.length

    def prepend(self, data) -> ():
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def append(self, data) -> ():
        current_node = self.head
        while current_node.has_next():
            current_node = current_node.next
        new_node = Node(data)
        current_node.next = new_node
        self.length += 1

    def all(self) -> Union[list, str]:
        if self.length == 0:
            return "empty"
        current_node = self.head
        output = []
        while current_node:
            output.append(current_node.data)
            current_node = current_node.next
        return output

    def pop_start(self):
        if self.length == 0:
            return print("empty")
        self.head = self.head.next
        self.length -= 1

    def pop(self):
        current_node = self.head
        if self.length <= 1:
            self.pop_start()
            return
        while current_node.next.has_next():
            current_node = current_node.next
        current_node.next = None
        self.length -= 1

    def insret(self, index: int, data) -> ():
        if self.length < index or index < 0:
            return print("are you dumb?")
        if index == 0:
            self.prepend(data)
            return
        if index == self.length:
            self.append(data)
            return
        new_node = Node(data)
        count = 0
        current = self.head
        while count < index-1:
            count += 1
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.length += 1

    def clear(self):
        self.head = None
        self.length = 0


class test(LinkedList):
    def pop(self): ...


if __name__ == "__main__":
    ll = LinkedList()
    ll.prepend(69)
    ll.append(420)
    print(len(ll))
    print(ll.all())
    ll.pop()
    ll.pop_start()
    print(ll.all())
    ll.insret(0, "hello world")
    ll.insret(1, "testing")
    ll.insret(2, "nerd")
    print(ll.all())
    ll.clear()
    print(ll.all())