class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.previous_node = None
        self.length = 0

    def append(self, value):
        self.length += 1
        if self.head == None:
            self.head = Node(value, None)
            self.previous_node = self.head
            #print(self.head.value, self.previous_node.value)
        elif self.previous_node.next_node == None:
            self.previous_node.next_node = Node(value, None)
            self.previous_node = self.previous_node.next_node
            #print(self.previous_node.value)

    def prepend(self, value):
        self.length += 1
        if self.head == None:
            self.head = Node(value, None)
        else:
            previous_head = self.head
            self.head = Node(value, previous_head)

    def size(self):
        return self.length

    def return_head(self):
        return self.head.value

    def tail(self):
        return self.previous_node.value

    def at(self, index):
        count = 0
        itr = self.head
        while itr:
            if count == index:
                return itr.value
            itr = itr.next_node
            count += 1
        return None

    def pop(self):
        self.length -= 1
        self.previous_node.next_node = None

    def to_s(self):
        nodes = []
        itr = self.head
        while itr:
            nodes.append(itr.value)
            itr = itr.next_node
        return str(nodes)

    def contains(self, value):
        itr = self.head
        while itr:
            if itr.value == value:
              return True
            itr = itr.next_node
        return False

    def find(self, value):
        count = 0
        itr = self.head
        while itr:
            if itr.value == value:
                return count
            itr = itr.next_node
            count += 1
        return None

    def insert_at(self, value, index):
        count = 0
        itr = self.head
        while itr:
            if index == 0:
                self.head = Node(value, self.head)
                break
            elif count == index or index == count + 1:
                itr.next_node = Node(value, itr.next_node)
                break
            itr = itr.next_node
            count += 1

    def remove_at(self, index):
        count = 1
        itr = self.head
        while itr:
            if index == 0:
                itr.next_nod = self.head
                break
            if count == index:
                itr.next_node = itr.next_node.next_node
                break
            itr = itr.next_node
            count += 1

linked_list = LinkedList()
linked_list.append(10)
# linked_list.prepend(30)
# linked_list.prepend(40)
linked_list.append(30)
linked_list.append(20)
linked_list.append(40)
linked_list.append(50)
linked_list.remove_at(0)

print(linked_list.to_s())
#print(linked_list.length)