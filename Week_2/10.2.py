import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    lst = []
    
    while idx < len(input_data):
        cmd = int(input_data[idx])
        idx += 1
        
        if cmd == 0:
            break
            
        elif cmd == 1:
            x = int(input_data[idx])
            p = int(input_data[idx + 1])
            idx += 2
            lst.insert(p, x)
            
        elif cmd == 2:
            p = int(input_data[idx])
            idx += 1
            del lst[p]
            
        elif cmd == 3:
            if not lst:
                print("-1")
            else:
                print(*lst)
                
        elif cmd == 4:
            p1 = int(input_data[idx])
            p2 = int(input_data[idx + 1])
            idx += 2
            val = lst.pop(p1)
            lst.insert(p2, val)
            
        elif cmd == 5:
            lst.reverse()
            
        elif cmd == 6:
            x = int(input_data[idx])
            idx += 1
            if lst and x > 0:
                x %= len(lst)
                lst = lst[x:] + lst[:x]
                
        elif cmd == 7:
            x = int(input_data[idx])
            idx += 1
            if lst and x > 0:
                x %= len(lst)
                lst = lst[-x:] + lst[:-x] if x != 0 else lst

if __name__ == "__main__":
    solve()