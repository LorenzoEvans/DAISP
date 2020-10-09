# What problem are Hash - Tables trying to solve:
    # The issue of searching a collection being linear by nature.
    # For instance, given a target value in an array, you have to look at
    # every object in the array, in order to see if it's the target value.
# Hash-tables allow for constant time look up.
    # HT's do this, by using a hashing function to get/store/delete values,
    # in constant time.
# Hash-tables are very similar to objects and dictionaries, in short,
# it's about having variable keys, as opposed to integer indexes.

# Hash tables use hash-functions, to map strings to integers, using the modulo operation.
    # Modulo allows us to constrain values to a certain range. 
# Once you hash a string, you can store the value in it's *underlying array*.

# Hash functions are deterministic, fast, and minimal duplication of output values.
    # This allows for the avoidance of collisions.
    # A perfect table, maps one input, to one output exactly.

def my_hash(string_val) :
    total = 0
    string_enc = string_val.encode()
    for i in string_enc:
        total += i
    return total % 8

val_arr = [None] * 8
ind = my_hash('hello')
val_arr[ind] = 90
print(my_hash('hello'))
print(val_arr)

def get_val(string_val, array_val):
        return array_val[my_hash(string_val)]
print(get_val('hello', val_arr))