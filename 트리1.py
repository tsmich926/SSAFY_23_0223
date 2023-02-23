# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

#전위순회
def preorder(i):
    if i : #존재하는 정점이면
        print(i,end= ' ')
        preorder(left[i])
        preorder(right[i])
    return


# def preorder(i):
#     print(i,end= ' ')
#     if left[i] :
#         preorder(left[i])
#     if right[i]:
#         preorder(right[i])
#     return

# #중위순회
def inorder(i):
    if i : #존재하는 정점이면
        inorder(left[i])
        print(i, end=' ')
        inorder(right[i])
    return


# #후위순회
def postorder(i):
    if i : #존재하는 정점이면
        postorder(left[i])
        postorder(right[i])
        print(i, end=' ')
    return



V = int(input())
arr = list(map(int,input().split()))
E = V-1 #간선수
left = [0]*(V+1) #부모를 인덱스로 왼쪽 자식 저장
right = [0]*(V+1) #.. 오른쪽 자식 저장
par = [0]*(V+1)
# child = [[] for _ in range(V+1)]
for i in range(E):
    p,c = arr[i*2],arr[i*2+1]
    #왼쪽에 자식이 들어있으면
    if left[p] ==0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p
    #child[p].append(c)
root = 1
while par[root] != 0: #자식을 인덱스로 부모를 확인했을때 0이 아니면 부모가 있는것
    root += 1
preorder(3)
print()
inorder(3)
print()
postorder(3)

#힙
#완전이진트리로 노드중 키값이 가장 큰 노드나 가장 작은 노드를 찾기 위해 만든 자료구조
#최대힙 부모의 키값이 자식노드의 키 값보다 크다
#최소힙

#최대 100개의 키
#최대힙


heap = [0]*101 #완전이진트리 1번-100번 인덱스 준비
last = 0 #완전이진트리의 마지막 정점 번호

def enq(n):
    global last
    last += 1 #완전이진트리에 마지막 정점을 추가하고
    heap[last] = n #마지막 정점에 저장
    c = last #부모가 있고 부모 > 자식 조건검사를 위해
    p = c//2 
    while p > 0 and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c],heap[p]
        c= p    #옮긴 자리에서 부모와 비교
        p = c//2
    return


def deq():
    global last
    tmp = heap[1] #루트 임시저장
    #마지막 정점의 값을 루트로 이동
    heap[1] = heap[last]
    last -= 1
    p = 1
    c = p*2 #왼쪽자식번호
    while c <= last: #자식이 하나 이상 있으면
        if c+1 <= last and heap[c] < heap[c+1]:#오른쪽 자식도 있고 오른쪽 자식의 키가 더 크면
            c += 1 #비교대상을 오른쪽 자식으로 변경
        if heap[c] > heap[p]: #자식이 부모보다 더 크면
            heap[c] ,heap[p] = heap[p],heap[c] #교환
            p = c
            c = p * 2
        else:
            break
    return tmp

enq(5)
print(heap[1])
enq(15)
print(heap[1])
enq(8)
print(heap[1])
enq(20)
print(heap[1])

while last>0:
    print(deq())




