class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))

def make_list(data):
    if not data or data[0] == 0:
        return None
    head = Node(data[1])
    curr = head
    for val in data[2:]:
        curr.next = Node(val)
        curr = curr.next

    return head

list1 = make_list(data1)
list2  = make_list(data2)


dum = Node(0)
curr  = dum
while list1 and list2:
    if list1.val <= list2.val:
        curr.next = list1
        list1 = list1.next
    else:
        curr.next = list2
        list2 = list2.next
    curr = curr.next

curr.next = list1 if list1 else list2

result = []
curr = dum.next
while curr:
    result.append(curr.val)
    curr = curr.next

print(*result)
