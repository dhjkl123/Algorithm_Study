import sys

class node():
    def __init__(self,root,left,right):
        self.root = root
        self.left = left
        self.right = right
    
N = int(sys.stdin.readline())

tree = dict()

for _ in range(N):
    root, left, right = sys.stdin.readline().rstrip().split()

    tree[root] = node(root, left, right)

def pre_search(root):
    print(tree[root].root,end='')
    if tree[root].left != '.' : pre_search(tree[root].left)
    if tree[root].right != '.' : pre_search(tree[root].right)

def mid_search(root):
    if tree[root].left != '.' : mid_search(tree[root].left)
    print(tree[root].root,end='')
    if tree[root].right != '.' : mid_search(tree[root].right)

def back_search(root):
    if tree[root].left != '.' : back_search(tree[root].left)
    if tree[root].right != '.' : back_search(tree[root].right)
    print(tree[root].root,end='')
    
pre_search('A')
print()
mid_search('A')
print()
back_search('A')
