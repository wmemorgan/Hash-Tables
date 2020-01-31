class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0


    def __len__(self):
        return self.length


    def reset_head_and_tail(self):
        self.head = None
        self.tail = None
        self.length = 0

    def find_node(self, key):
        if self.head is None:
            return None
        elif self.head.key == key:
            return self.head
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
                if curr_node.key == key:
                    return curr_node
            return None


    def add_to_head(self, node):
        if self.tail is None:
            self.head = self.tail = node
        else:    
            old_head = self.head
            self.head = node
            self.head.next = old_head
            self.length += 1


    def update_kv(self, key, value):
        if self.find_node(key) is not None:
            updated_kv = self.find_node(key)
            updated_kv.value = value

    def remove_from_head(self):
        if self.head is None:
            return None

        removed_node = self.head

        if self.length == 1:
            self.reset_head_and_tail()
        else:
            self.head = removed_node.next
            self.length -= 1
        return removed_node
        

    def remove(self, key):
        # Edge case check
        if self.head is None:
            return None
        elif self.find_node(key) is None:
            return None

        if self.head.key == key:
            self.remove_from_head()
        else:
            curr_node = self.head
            while curr_node:
                prev_node = curr_node
                curr_node = curr_node.next
                if curr_node.key == key:
                    removed_node = curr_node
                    curr_node = prev_node
                    curr_node.next = removed_node.next
                    return removed_node

    def print_ll(self):
        if self.head is None:
            return None

        node = self.head
        print("linked list contents:")
        while node:
            print(f"'{node.key}': '{node.value}'")
            node = node.next

