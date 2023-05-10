class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        if self.is_empty():
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        if self.is_empty():
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def length_of_link_list(self):
        if self.is_empty():
            return 0
        count = 1
        current = self.head
        while current.next:
            count += 1
            current = current.next
        return count

    def __getitem__(self, index):
        if self.is_empty():
            return "链表为空"
        elif self.length_of_link_list() - 1 < index:
            return "索引值溢出"
        else:
            count, current = 0, self.head
            while current.next and count < index:
                count += 1
                current = current.next
            return current

    def insert_at_index(self, data, index):
        if self.is_empty():
            return "链表为空"
        elif index == 0:
            return self.insert_at_beginning(data)
        elif index == self.length_of_link_list() - 1:
            return self.insert_at_end(data)
        else:
            new_node = Node(data)
            pre = self[index - 1]
            new_node.next = pre.next
            pre.next = new_node



mylinklist = LinkList()

for i in range(100):
    mylinklist.insert_at_beginning(i + 1)
mylinklist.insert_at_index(10000, 10)
print(mylinklist[10].data)
