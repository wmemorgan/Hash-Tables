# '''
# Linked List hash table key/value pair
# '''
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

        print(f"output_index: {output_index}")
        return output_index


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        index = self._hash(key) % self.capacity
        print(f"_hash_mod index: {index}")
        return index


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        if None not in self.storage:
            self.resize
            self.storage[self._hash_mod(key)] = (key, value)
        else:
            self.storage[self._hash_mod(key)] = (key, value)
            
        



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        print(
            f"self.storage[self._hash_mod(key)]: {self.storage[self._hash_mod(key)]}")
        if self.storage[self._hash_mod(key)] is not None:
            self.storage[self._hash_mod(key)] = None
        else:
            print("key does not exists")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # print(f"hash_mod: {self._hash_mod(key)}")
        kv = self.storage[self._hash_mod(key)]
        # print(f"kv: {self.storage[self._hash_mod(key)]}")
        if kv is not None:
            return kv[1]
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity * 2
        temp_storage = [None] * self.capacity

        for i in range(self.capacity // 2):
            temp_storage[i] = self.storage[i]
        
        print(f"temp_storage: {temp_storage}")
        self.storage = temp_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))
    print(f"storage: {ht.storage}")

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(f"line_1: {ht.retrieve('line_1')}")
    print(f"line_2: {ht.retrieve('line_2')}")
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))
    ht.remove('line_1')
    ht.insert("line_3", "Linked list saves the day!")
    print(ht.retrieve("line_3"))
    print(f"storage: {ht.storage}")

    print("")
