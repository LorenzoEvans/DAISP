class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def get_stack(self):
        return self.items
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    def peek(self):
        return self.items[-1]
    

def rev_str(str1):
    s = Stack() # We use a stack, for LIFO ordering.
    result_str = "" # Declare an empty string to hold our reversed string.
    for i in range(len(str1)): # We're going to push every char in the string onto the stack.
        s.push(str1[i])
    while len(s.items) > 0:n # Once we're done, we want to loop through the stack,
        char_ = s.pop()      # with a variable, which will hold an item popped off the top of the stack,
                             # which is effective, because the item at the top of the stack, is the same 
                             # as the item at the end of the string. 
        result_str += char_  # We can then use this variable, as a value to concatenate on the end of our string.
    return result_str        # Once our string is done being built, we return it.
print(rev_str("Hello")) # Should output "ollEh"