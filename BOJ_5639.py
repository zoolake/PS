import sys
sys.setrecursionlimit(10**9)

def post_order(tree):
    root = tree[0]
    if len(tree) == 1:
        print(root)
        return

    pivot = len(tree)
    for i in range(1,len(tree)):
        if tree[i] > root:
            pivot = i
            break
    
    if pivot > 1:
        post_order(tree[1:pivot])
    if pivot < len(tree):
        post_order(tree[pivot:])
    print(root)
    

pre_order = []
node = 0
while node <= 10000:
    try:
        value = int(input())
    except:
        break
    pre_order.append(value)
    node += 1

post_order(pre_order)

