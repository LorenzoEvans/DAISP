
# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.elements = [None] * capacity # maybe array we built?
        self.count = 0


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = ((hash << 5) + hash) + ord(x)
    hash_val = hash % max & 0xFFFFFFFF
    return hash_val

# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    node = LinkedPair(key, value)
    if hash_table.elements[index] is not None:
        print(f"You are overwriting element '{str(hash_table.elements[index].value)}' at index '{index}' with value '{value}'")
    hash_table.elements[index] = node

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    val = 0
    if hash_table.elements[index] is None:
        print(f"No value found at index '{index}'")
    elif hash_table.elements[index] is not None:
        val = hash_table.elements[index].value
        del hash_table.elements[index]
    return val
# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    val = -1
    for x in hash_table.elements:
        if x is None:
            continue
        if x is not None and x.key is key:
            val = x.value
            print(f"Element with key '{key}' found at index '{hash_table.elements.index(x)}', value: '{x.value}'")
    return val


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_cap = hash_table.capacity * 2
    new_ele = [None] * new_cap
    for i in hash_table.elements:
        new_ele.append(i)
    hash_table.capacity = new_cap
    hash_table.elements = new_ele
    return hash_table

def Testing():
    ht = HashTable(2)
    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")
    old_capacity = len(ht.elements)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.elements)
    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")
Testing()
