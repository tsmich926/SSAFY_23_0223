#후위순회
# for tc in range(1,2):
#     N = int(input()) #정점의 개수
#     value = ['-'] * (N + 1)
#     rightc = [0] * (N + 1)
#     leftc = [0] * (N + 1)
#     lst = []
#
#     for i in range(N):
#         lst = list(input().split())
#         # st2.a
#         # ppend(lst[1:])
#         print(lst)
#         idx = int(lst[0])
#         value[idx] = lst[1]
#         if len(lst) == 3:
#             leftc[idx] = lst[2]
#             rightc[idx] = lst[3]
#         if len(lst) == 2:
#             rightc[idx] = lst[3]
#         print(lst)



#v1과2를 계산해서 리턴
def process(v1,v2,v):
    if v == '-':
        ans= v1-v2
    elif v == '+':
        ans = v1+v2
    elif v == '*':
        ans = v1*v2
    elif v == '/':
        ans = v1//v2
    return ans

def postorder(root):
    v = TREE[root][0]
    if v.isdigit() :
        return int(v)
        #루트가 의미있는 값이면
    else:
        lvalue = postorder(int(TREE[root][1])) #루트의 왼쪽 서브트리의 루트
        rvalue = postorder(int(TREE[root][2])) #루트의 오른쪽 서브트리의 루트
        res = process(lvalue,rvalue,TREE[root][0]) #0번째에 연산자가 붙어있으므로
        return res


for tc in range(1,2):
    N = int(input()) #정점의 개수
    TREE = [[] for _ in range(N+1)]

    for i in range(N):
        inp = input().split()
        idx =int(inp[0])
        TREE[idx] =inp[1:]

    postorder(1)
    print(f'{tc} {res}')