import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    heap = [-int(x) for x in data[1:1+n]]

    def sift_down(idx, length):
        while True:
            left, right = 2*idx+1, 2*idx+2
            smallest = idx

            if left < length and heap[left] < heap[smallest]:
                smallest = left
            if right < length and heap[right] < heap[smallest]:
                smallest = right
            if smallest == idx:
                break
            heap[idx], heap[smallest] = heap[smallest], heap[idx]
            idx = smallest

    for i in range((n-2) // 2, -1, -1):
        sift_down(i, n)

    while n > 1:
        y = -heap[0]
        
        last = heap.pop()
        n -= 1
        if n > 0:
            heap[0] = last
            sift_down(0, n)

        x = -heap[0]

        diff = y - x
        if diff == 0:
            last = heap.pop()
            n -= 1
            if n > 0:
                heap[0] = last
                sift_down(0, n)
        else:
            heap[0] = -diff
            sift_down(0, n)
    if n == 1:
        print(-heap[0])
    else:
        print(0)


if __name__ == '__main__':
    solve()
