
def enq(n):
    global last

    last += 1
    heap[last] = n
    c = last
    p = c//2
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c],heap[p]
        c= p    #옮긴 자리에서 부모와 비교
        p = c//2
    return


T= int(input())
for tc in range(1,T+1):
    N =int(input()) #마지막 노드의 번호
    heap = [0] * (N + 1)
    nums = list(map(int,input().split()))
    last = 0
    for item in nums:
        enq(item)


    sumV = 0
    leaf = N // 2
    while leaf >= 1:
        sumV += heap[leaf]
        leaf = leaf // 2
    print(f'#{tc} {sumV}')



