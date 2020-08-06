class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.counter = 0
    def print_list(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next
    def append(self, data):
        n_node = Node(data)
        if self.head is None:
            self.head = n_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = n_node
        self.counter += 1

    def prepend(self, data):
        cur_val = self.head
        self.head = Node(data)
        self.head.next = cur_val
        self.counter += 1
    
    def insert_after(self, data, target):
        if self.head.data is target:
            self.prepend(data)
            return
        cur_val = self.head
        while cur_val.next is not target:
            cur_val = cur_val.next
            if cur_val.data is target:
                next_val = cur_val.next
                cur_val.next = Node(data)
                cur_val.next.next = Node(next_val.data)
                return
        self.counter += 1
    def insert_before(self, data, target):
        if self.head.data is target:
            self.prepend(data)
            return
        cur_val = self.head
        while cur_val.data is not target:
            cur_val = cur_val.next
            if cur_val.next.data is target:
                # print("cur_val.next.data is: ",cur_val.next.data)
                next_node = cur_val.next
                # print("next_node is: ", next_node.data)
                n_node = Node(data)
                cur_val.next = n_node
                n_node.next = next_node
                return
        self.counter += 1
    def remove(self, target):
        cur_val = self.head
        if cur_val.data is target:
            self.head = cur_val.next
        while cur_val.data is not target:
            cur_val = cur_val.next
            if cur_val.next.data is target:
               cur_val.next = cur_val.next.next
               return
        self.counter -= 1
                
    def remove_at_index(self, index: int):
        counter = 0
        cur_val = self.head
        while counter is not index:
            last_val = cur_val
            cur_val = cur_val.next
            counter += 1
            if counter == index:
                last_val.next = None
                return
        self.counter -= 1
    def check_length(self):
        return self.counter

l_l = LinkedList()
l_l.append("A") # 0
l_l.append("B") # 1
l_l.append("C") # 2
l_l.append("D") # 3
l_l.remove_at_index(3)
l_l.print_list()
print(l_l.check_length())