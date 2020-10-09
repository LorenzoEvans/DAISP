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
        
    def node_swap(self, key_1, key_2):
        if key_1 == key_2: 
            return 

        prev_1 = None
        cur_1 = self.head

        while cur_1 and cur_1.data != key_1:
            prev_1 = cur_1
            cur_1 = cur_1.next

        prev_2 = None
        cur_2 = self.head

        while cur_2 and cur_2.data != key:
            return

        if not cur_1 or cur_2:
            return
        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2
        if prev_2:
            prev_2.next = cur_1 
        else:
            self.head = cur_1

        print(prev_1.data)
        print(cur_1.data)
lnkd_lst = LinkedList()

lnkd_lst.append("A")
lnkd_lst.append("B")
lnkd_lst.append("C")
lnkd_lst.append("D")
lnkd_lst.node_swap("B", "C")

# print(lnkd_lst.head.data)

# def node_swapper(ll, t1, t2):

#     cur_val = ll.head

#     while cur_val.data is not t1:
#         cur_val = cur_val.next
#         print(cur_val.data)
#         # if cur_val.next is t1:
#         #     t_2 = cur_val.next.next.data
#         #     t_1 = cur_val.next.data
#         #     print(t_2, t_1)


# print(node_swapper(lnkd_lst, "B", "C"))