# 후위순회
# def postorder(i):
#     if i : #존재하는 정점이면
#         postorder(left[i])
#         postorder(right[i])
#         print(i, end=' ')
#     return


T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split()) #노드개수,단말노드개수,값을 출력할 노드번호
    TREE= [0]*(N+1)
    for i in range(M):
        node,num = map(int,input().split())
        TREE[node] = num  #단말 노드의 값을 저장
    for i in range(N,L+1,-1):
        TREE[i//2] += TREE[i]
    print(f'#{tc} {TREE[L]}')
