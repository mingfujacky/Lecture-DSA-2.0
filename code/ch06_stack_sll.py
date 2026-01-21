from ch04_singly_linked_list import SinglyLinkedList

class Stack:
    def __init__(self):
        self._data = SinglyLinkedList()

    def __len__(self):
        # Return the size of the stack.
        return len(self._data)

    def __str__(self):
        # Return the string representation of the stack.
        return str(self._data)

    def __repr__(self):
        # Return the string (internal) representation of the stack.
        return f'Stack({str(self._data)})'

    def is_empty(self):
        return self._data.is_empty()

    def push(self, value):
        # Add a new value to the stack.
        self._data.insert_in_front(value)

    def pop(self):
        # Remove and return the last value added to the stack.
        if self.is_empty():
            raise ValueError("Cannot pop from an empty stack")
        return self._data.delete_from_front()

    def peek(self):
        # Return the last value added to the stack without removing it.
        if self.is_empty():
            raise ValueError("Cannot peek at an empty stack")
        return self._data._head.data
    
if __name__ == "__main__":
    # Example usage of the stack class.
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack.peek())
    stack.push('abc')
    print(repr(stack))    
    print(len(stack))
