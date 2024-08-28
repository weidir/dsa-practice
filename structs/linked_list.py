# Linked List

class Node:
    """
    An object for storing a single node of a linked list
    Attributes:
        data: contains the data on this node
        next_node: references the next node in the linked list
    """

    def __init__(self, data, next_node = None, name: str = None):
        self.data = data
        self.next_node = next_node
        self.name = name

    def __repr__(self):
        next_node = f"name: {self.next_node.name if self.next_node is not None else None}; data: {self.next_node.data if self.next_node is not None else None}"
        return f"Node(name: {self.name}; data: {self.data}; next_node: {next_node})"
    

class LinkedList:
    """
    A class that implements a singly linked list
    """

    def __init__(self, head: Node = None, tail: Node = None):
        self.head = head
        self.tail = tail
    
    def __repr__(self):
        str_value_list = [str(x) for x in self.values_to_list()]
        return f"LinkedList({'-> '.join(str_value_list)}) \nhead: {self.head}; tail: {self.tail}; size: {self.size()}"

    def empty(self):
        return self.head == None
    
    def size(self):
        if not self.empty():
            size = 1
            node = self.head
            while node.next_node is not None:
                size += 1
                node = node.next_node
            return size
        else:
            return 0
    
    def find_tail(self):
        if not self.empty():
            node = self.head
            while node.next_node is not None:
                node = node.next_node
            self.tail = node
        else:
            return 0
    
    # Constant time complexity: O(1)
    def prepend(self, node: Node):
        node.next_node = self.head
        self.head = node

    # Linear time complexity: O(n)
    def append(self, node: Node):
        if self.tail is None:
            self.find_tail()
        self.tail.next_node = node
        self.tail = node
    
    # Linear time complexity: O(n)
    def values_to_list(self):
        if self.head is not None:
            node_value_list = []
            node = self.head

            while node:
                node_value_list.append(node.data)
                node = node.next_node

            return node_value_list

        else:
            print("Cannot traverse empty linked list")
            return None

    # Linear time complexity: O(n)
    def search(self, value):
        if self.head is not None:
            node = self.head

            while node:
                if node.data == value:
                    return node
                
                node = node.next_node
            
            return None
        else:
            print("Cannot search empty linked list")
            return None
    
    # Linear time complexity: O(n)
    def index(self, index):
        if self.head is not None:
            idx = 0
            node = self.head

            while node:
                if idx == index:
                    return node
                
                node = node.next_node
                idx += 1
            
            return None
        else:
            print("Cannot index empty linked list")
            return None
        

    # Linear time complexity: O(n)
    def insert(self, index, node):
        if index == 0:
            self.prepend(node)
        else:
            before_node = self.index(index - 1)
            after_node = before_node.next_node
            before_node.next_node = node
            node.next_node = after_node

            if after_node is None:
                self.tail = node
    
    # Linear time complexity: O(n)
    def remove(self, value):
        if self.head is not None:
            idx = 0
            node = self.head

            while node:
                if node.data == value:
                    if idx == 0:
                        print("Removing head node")
                        self.head = node.next_node
                    else:
                        prev_node.next_node = node.next_node
                        if node.next_node is None:
                            self.tail = prev_node
                    break
                
                prev_node = node
                node = node.next_node
                idx += 1
            
            return None

        else:
            print("Cannot remove node from empty linked list")
            return None
        

        

if __name__ == "__main__":
    N1 = Node(data=1, name="N1")
    N2 = Node(data=5, name="N2")
    N3 = Node(data=10, name="N3")


    L1 = LinkedList(head=N1)
    L1.prepend(N2)
    L1.append(N3)

    assert L1.size() == 3
    assert L1.head == N2
    assert L1.tail == N3
    assert L1.search(5) == N2
    assert L1.search(1) == N1
    assert L1.search(10) == N3
    assert L1.index(0) == N2
    assert L1.index(1) == N1
    assert L1.index(2) == N3
    print("All checks passed")