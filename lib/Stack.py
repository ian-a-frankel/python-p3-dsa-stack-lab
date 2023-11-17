class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, value):
        n = 1
        while n < len(self.items) + 1:
            if self.items[len(self.items) - n] == value:
                return n - 1
            n += 1
        return -1