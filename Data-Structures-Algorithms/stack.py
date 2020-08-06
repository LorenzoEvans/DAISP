class Stack():
    def __init__(self):
        self.items = [
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
        if not self.is_empty():
            return self.items[-1]

def is_match(par1, par2):
    matched = par1 + par2
    match_list = ["()", "{}", "[]"]
    print("matched is: ", matched)
    if matched is match_list[0]:
        return True
    elif matched is match_list[1]:
        return True
    elif matched is match_list[2]:
        return True
    else:
        return False


def is_balanced(paren_string):
    s = Stack()
    is_balanced, index = True, 0
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop() 
                if not is_match(top, paren): # <- A wild assumption appeared! 
                    is_balanced = False
        index += 1
    if s.is_empty() and is_balanced:
        return True
    else: return False


# print("Is the string balanced? ",is_balanced("[{]}(])[")) # This broke the function.

#  So, this solution isn't particularly robust.
#  Let's try and think about why this is.
#  The way we ordered our string, clashes with lines 66, and 67.
#  These two lines of code make assumptions about the order in which
#  matching elements will appear- it assumes that the companion to paren,
#  will be at the *top* of the stack, when it could be anywhere on the stack.

# # I think a better solution would be to rely on a map.
# # We can keep track of the distinct occurrences of each parenthesis,
# # and at the end, any "type" of parentheses that don't have equal occurrences,
# # will render the string unbalanced.
# # {
# # "(" : 4
# # ")" : 4 // So far, so good.
# # "[" : 3
# # "{" : 2
# # "}" : 2 // Still good, but then..
# # "]" : 5 // ! We know this string is unbalanced because 5 != 3.
# # }

# # Note to self, becoming good with maps, is equivalent to becoming better with dealing with frequencies of events or values.

def dec_to_bin(dec_num):
    s = Stack()
    bin_num = ""
    while dec_num > 0:
        rem = dec_num % 2
        dec_num = dec_num // 2
        s.push(rem)
    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num

# A
# B
# Q
# C
# D