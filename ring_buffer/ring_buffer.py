from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        if (len(self.storage) == self.capacity):
            self.current.value = item
            if (self.current.next):
                self.current = self.current.next
            else:
                self.current = self.storage.head
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        if len(self.storage) == 0:
            return list_buffer_contents
        # TODO: Your code here
        else:
          current_node = self.storage.head
          while current_node:
              if (current_node.value):
                  list_buffer_contents.append(current_node.value)  
              current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.storage = [None]*capacity
        self.capacity = capacity
        self.current =0

    def append(self, item):
        if (self.current == self.capacity):
            self.current = 0
        self.storage[self.current] = item
        self.current += 1

    def get(self):
        
        return [i for i in self.storage if i is not None]
