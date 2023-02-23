# import heapq
#
# h= []
# lst = [15,4,13,20,11,19]
# for item in lst:
#     heapq.heappush(h,item)
#
# print(heapq.heappop(h))
# print(heapq.heappop(h))
# print(heapq.heappop(h))

def enq(item):
    global last
    last += 1
    TREE[last] = item #트리에 아이템 넣기
    c = last
    p = c//2 #부모 인덱스
    while p >= 1 and TREE[c] > TREE[p]:  #최대힙 규칙 깨졌으면
        TREE[c],TREE[p] = TREE[p],TREE[c] #교환
        c = p
        p = c//2
#
# def deq():
#     tmp = TREE[1]
#     TREE[1] = TREE[last]
#     p = 1
#     if TREE[p*2] > TREE[p*2+1]:
#         c = p*2
#     else:
#         c= p*2+1
#
#
#     return tmp
#
#


def deq():
    global last
    tmp = TREE[1]
    TREE[1] = TREE[last]
    last -= 1
    p = 1
    c= p*2
    while c <= last: #p가 자식노드가 하나라도 있는 동안
        if c+1<=last and TREE[c] < TREE[c+1]:  #오른쪽 자식노드가 있으면 and 오른쪽 노드가 더 크면
            c += 1
        if TREE[p] < TREE[c]: #힙이 깨졌으면
            TREE[p],TREE[c] = TREE[c],TREE[p]
            p= c
            c=p*2
        else: #힙이 안깨짐
            break
    return tmp



TREE = [0]*100
last = 0
lst = [15,4,13,20,11,19]
for item in lst:
    enq(item)
    print(TREE)

enq(23)
print(TREE)

print(deq())
print(last,TREE)
print(deq())
print(last,TREE)
print(deq())
print(last,TREE)


p = 1
c= p*2
if c+1<=last and TREE[c] < TREE[c+1]:
    c += 1
while c<= last and TREE[p] <TREE[c]:
    TREE[p] ,TREE[c] = TREE[c],TREE[p]
    p = c
    c =p*2
    if c+1 <=last and TREE[c] < TREE[c+1]:
        c+= 1