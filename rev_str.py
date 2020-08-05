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
    s = Stack()
    result_str = ""
    for i in range(len(str1)):
        s.push(str1[i])
    while len(s.items) > 0:
        char_ = s.pop()
        result_str += char_
    return result_str
print(rev_str("Hello"))