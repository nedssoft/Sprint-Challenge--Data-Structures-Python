from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) == self.capacity:
            if self.current is None:
                self.storage.head.value = item
                self.current = self.storage.head.next
            else:
                current = self.storage.head
                while current:
                    if current.value == self.current.value:
                        current.value = item
                self.current = self.current.next
        else:
            self.storage.add_to_tail(item)

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
        pass

    def append(self, item):
        pass

    def get(self):
        pass
