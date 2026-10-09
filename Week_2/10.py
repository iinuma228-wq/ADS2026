class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_length(head):
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    return length

def insert_node(head, x, p):
    new_node = Node(x)
    if p == 0:
        new_node.next = head
        return new_node
    
    curr = head
    for _ in range(p - 1):
        curr = curr.next
    
    new_node.next = curr.next
    curr.next = new_node
    return head

def delete_node(head, p):
    if p == 0:
        return head.next
    
    curr = head
    for _ in range(p - 1):
        curr = curr.next
    
    curr.next = curr.next.next
    return head

def print_list(head):
    if not head:
        print(-1)
        return
    
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    print(*result)

def move_node(head, p1, p2):
    # 1. Извлекаем узел с позиции p1
    if p1 == 0:
        target = head
        head = head.next
    else:
        prev = head
        for _ in range(p1 - 1):
            prev = prev.next
        target = prev.next
        prev.next = target.next

    # 2. Вставляем его на позицию p2
    if p2 == 0:
        target.next = head
        return target
    
    curr = head
    for _ in range(p2 - 1):
        curr = curr.next
    
    target.next = curr.next
    curr.next = target
    return head

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def shift_left(head, x):
    length = get_length(head)
    if length <= 1 or x == 0:
        return head
    
    # Ищем x-й узел (новый хвост)
    new_tail = head
    for _ in range(x - 1):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    
    # Идем до старого хвоста
    old_tail = new_head
    while old_tail.next:
        old_tail = old_tail.next
        
    old_tail.next = head
    new_tail.next = None
    
    return new_head

def shift_right(head, x):
    length = get_length(head)
    if length <= 1 or x == 0:
        return head
    
    # Правый сдвиг на x равен левому сдвигу на (length - x)
    return shift_left(head, length - x)

# --- Главный цикл обработки команд ---
head = None

while True:
    try:
        line = input().split()
    except EOFError:
        break
        
    if not line:
        continue
        
    cmd = int(line[0])
    
    if cmd == 0:
        break
    elif cmd == 1:
        x, p = int(line[1]), int(line[2])
        head = insert_node(head, x, p)
    elif cmd == 2:
        p = int(line[1])
        head = delete_node(head, p)
    elif cmd == 3:
        print_list(head)
    elif cmd == 4:
        p1, p2 = int(line[1]), int(line[2])
        head = move_node(head, p1, p2)
    elif cmd == 5:
        head = reverse_list(head)
    elif cmd == 6:
        x = int(line[1])
        head = shift_left(head, x)
    elif cmd == 7:
        x = int(line[1])
        head = shift_right(head, x)