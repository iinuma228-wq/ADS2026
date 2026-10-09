class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, title):
        new_node = Node(title)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print("ok")

    def add_back(self, title):
        new_node = Node(title)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        print("ok")

    def erase_front(self):
        if not self.head:
            print("error")
            return
        
        removed_val = self.head.val
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            
        print(removed_val)

    def erase_back(self):
        if not self.tail:
            print("error")
            return
        
        removed_val = self.tail.val
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            
        print(removed_val)

    def front(self):
        if not self.head:
            print("error")
        else:
            print(self.head.val)

    def back(self):
        if not self.tail:
            print("error")
        else:
            print(self.tail.val)

    def clear(self):
        self.head = None
        self.tail = None
        print("ok")

def solve():
    dll = DoublyLinkedList()
    
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
            
        if not line:
            continue
            
        parts = line.split(maxsplit=1)
        cmd = parts[0]
        
        if cmd == "add_front":
            dll.add_front(parts[1])
        elif cmd == "add_back":
            dll.add_back(parts[1])
        elif cmd == "erase_front":
            dll.erase_front()
        elif cmd == "erase_back":
            dll.erase_back()
        elif cmd == "front":
            dll.front()
        elif cmd == "back":
            dll.back()
        elif cmd == "clear":
            dll.clear()
        elif cmd == "exit":
            print("goodbye")
            break

if __name__ == '__main__':
    solve()