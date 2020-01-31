# '''
# Linked List hash table key/value pair
# '''
from linkedlist import LinkedList

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        output_index = 0
        WEIRD_PRIME = 31
        for indx in range(min(len(key), 100)):
            value = ord(key[indx]) - 96
            output_index = (output_index + WEIRD_PRIME + value) % len(key)

        return output_index
        

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        index = self._hash(key) % self.capacity
        return index


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.
        '''
        if None not in self.storage:
            self.resize()

        if self.storage[self._hash_mod(key)] is None:
            self.storage[self._hash_mod(key)] = LinkedList(
                LinkedPair(key, value))
        elif self.storage[self._hash_mod(key)].find_node(key) is not None:
            self.storage[self._hash_mod(key)].update_kv(key, value)
        else:
            self.storage[self._hash_mod(key)].add_to_head(
                LinkedPair(key, value))


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.
        '''
        slot = self.storage[self._hash_mod(key)]
        if slot.find_node(key) is not None:
            slot.remove(key)
            # Garbage collection
            if slot.length == 0:
                self.storage[self._hash_mod(key)] = None
        else:
            print("key does not exists")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        '''
        slot = self.storage[self._hash_mod(key)]
        if slot is not None:
            if slot.find_node(key) is not None:
                return slot.find_node(key).value
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''
        self.capacity = self.capacity * 2
        temp_storage = [None] * self.capacity

        for i in range(self.capacity // 2):
            temp_storage[i] = self.storage[i]
        
        self.storage = temp_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")

    print("")

    # Test storing beyond capacity
    print(f"line_1: {ht.retrieve('line_1')}")
    print(f"line_2: {ht.retrieve('line_2')}")
    print(f"storage: {ht.storage}")

    # Test resizing
    print("\nTest resizing")
    old_capacity = len(ht.storage)
    ht.insert("line_3", "Linked list saves the day!")
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.")
    print(f"storage: {ht.storage}\n")

    # Test if data intact after resizing
    print("\nTest data after resizing:")
    print(f"line_1: {ht.retrieve('line_1')}")
    print(f"line_2: {ht.retrieve('line_2')}")
    print(f"storage: {ht.storage}")
    print(f"remove line_2: ")
    ht.remove('line_2')
    print(f"storage: {ht.storage}")

    print("")

"""
ll = LinkedList(LinkedPair('dog', 'bark'))
ll.add_to_head(LinkedPair('cat', 'meow'))
ll.print_ll()
print("update existing key/value pair:")
ll.update_kv('dog', 'woof')
ll.print_ll()
ll.add_to_head(LinkedPair('cow', 'moo'))
ll.print_ll()
print("remove existing key/value pair:")
ll.remove('cat')
ll.print_ll()
"""
