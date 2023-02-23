def insert(item):
    pos = 1
    while TREE[pos] != 0 : #비어있으면 넣고 차있으면 왼쪽으로 갈지 오른쪽으로 갈지? 데이터가 비어있는 동안 내려간다.
        if TREE[pos] == item:
            return

        if TREE[pos] < item:
            pos =pos*2+1
        else:
            pos = pos*2
    TREE[pos] = item




#인덱스를 찾아주는 함수
def find(key):
    pos = 1
    while TREE[pos] != 0:
        if TREE[pos] == key:
            return pos
        if TREE[pos]<key:
            pos= pos*2+1
        else:
            pos = pos*2
    return -1


#이진트리
TREE = [0]*100
lst = [9,4,12,3,6,15,13,17]
for item in lst:
    insert(item)
    print(TREE)

insert(5)
print(TREE)


#힙은 반드시 완전이진트리일것
# 최대힙은 루트에 최대값이
# 최소힙은 루트에 최소값이
# 최소힙은 디큐할때 제일 작은얘가 먼저 나옴...
# 최대힙은 디큐할때 제일 큰얘가 먼저 나옴 디큐하면서 정렬이 된다.


#힙큐이용
import heapq

h= []
lst = [15,4,13,20,11,19]
for item in lst:
    heapq.heappush(h,item)

print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))

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

def deq():
    tmp = TREE[1]
    TREE[1] = TREE[last]
    p = 1
    if TREE[p*2] > TREE[p*2+1]:
        c = p*2
    else:
        c= p*2+1


    return tmp

