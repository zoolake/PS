import sys
import collections

class Node:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

# 전위 preorder
def preorder(node):
    print(node.root, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])
# 중위 inorder
def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.root, end='')
    if node.right != '.':
        inorder(tree[node.right])
# 후위 postorder
def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.root, end='')


input = sys.stdin.readline
N = int(input())
tree = collections.defaultdict(Node)
for _ in range(N):
    root, left, right = map(str, input().split())
    tree[root] = Node(root=root, left=left, right=right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])