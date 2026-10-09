import sys
from collections import deque

def solve():
    dq = deque()
    
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
            
        cmd = parts[0]
        
        if cmd == "add_front":
            dq.appendleft(parts[1])
            print("ok")
        elif cmd == "add_back":
            dq.append(parts[1])
            print("ok")
        elif cmd == "erase_front":
            print(dq.popleft() if dq else "error")
        elif cmd == "erase_back":
            print(dq.pop() if dq else "error")
        elif cmd == "front":
            print(dq[0] if dq else "error")
        elif cmd == "back":
            print(dq[-1] if dq else "error")
        elif cmd == "clear":
            dq.clear()
            print("ok")
        elif cmd == "exit":
            print("goodbye")
            break

if __name__ == "__main__":
    solve()