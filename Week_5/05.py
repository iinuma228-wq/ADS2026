import sys

def main():
    # Read entire input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    heap = []
    s = 0
    out = []
    
    idx = 2
    total_tokens = len(input_data)
    
    while idx < total_tokens:
        cmd = input_data[idx]
        if cmd == "insert":
            val = int(input_data[idx + 1])
            idx += 2
            
            heap_len = len(heap)
            if heap_len < m:
                s += val
                heap.append(val)
                # Inline push / sift-up
                i = heap_len
                while i > 0:
                    parent = (i - 1) // 2
                    if heap[parent] > heap[i]:
                        heap[parent], heap[i] = heap[i], heap[parent]
                        i = parent
                    else:
                        break
            elif heap[0] < val:
                # Optimized replace-root / sift-down (heappushpop equivalent)
                s += val - heap[0]
                heap[0] = val
                i = 0
                while True:
                    left = 2 * i + 1
                    right = 2 * i + 2
                    smallest = i
                    
                    if left < heap_len and heap[left] < heap[smallest]:
                        smallest = left
                    if right < heap_len and heap[right] < heap[smallest]:
                        smallest = right
                        
                    if smallest == i:
                        break
                        
                    heap[i], heap[smallest] = heap[smallest], heap[i]
                    i = smallest
        else: # print command
            idx += 1
            out.append(str(s))
            
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()