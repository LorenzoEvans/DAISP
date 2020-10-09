

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.elements = [None] * capacity
        pass

    # '''
    # Fill this in.
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

    # If you are overwriting a value with a different key, print a warning.
    # '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    pair = Pair(key, value)
    if hash_table.elements[index] is not None:
        print(f"You are overwriting element '{str(hash_table.elements[index].value)}' at index '{index}' with value '{value}'")
    hash_table.elements[index] = pair

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    val = 0
    if hash_table.elements[index] is None:
        print(f"No value found at index {index}")
    elif hash_table.elements[index] is not None:
        val = hash_table.elements[index].value
        del hash_table.elements[index]
    return val




'''
Fill this in.

Should return None if the key is not found.
'''
def hash_table_retrieve(hash_table, key):

    for i in hash_table.elements:
        if i is None:
            continue
        elif i is not None and i.key is key:
            print(f"Element with key '{key}' was found at index {hash_table.elements.index(i)}, value: '{i.value}'")
            return i.value



def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")
    hash_table_retrieve(ht, "line")
    element_list = []
    for x in ht.elements:
        if x is None:
            element_list.append(x)
        elif x is not None:
            element_list.append(x.value)
    print('ele_list: ', element_list)
    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")

Testing()
