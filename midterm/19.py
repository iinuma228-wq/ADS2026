import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    arr = [0] + [int(x) for x in data[1:1+n]]

    for i in range(1, (n//2)+1):
        left = i * 2
        right  = i * 2 + 1

        if left < n and arr[i] > arr[left]:
            print("NO")
            return

        if right < n and arr[i] > arr[right]:
            print("NO")
            return
    print("YES")

if __name__ == '__main__':
    solve()

     

        
            
