from snippets.trees.BinarySearchTree import BinarySearchTree
from snippets.trees import Utilities
from utilities import nonstd

#nonstdio = nonstd.IO(in_file="bst.in", out_file="bst.out")
nonstdio = nonstd.In(in_file="bst.in")
bst = BinarySearchTree()
temp = input().split()
for key in temp:
    bst.insert(int(key))

bst.delete(3)
bst.delete(4)
bst.insert(456)
bst.delete(456)
bst.delete(9)
bst.delete(16)


def op(value):
    print(value, end=" ")

print("inorder")
Utilities.traverse_inorder(bst.get_root(), operation=op)
print("\npreorder")
Utilities.traverse_preorder(bst.get_root(), op)
print("\nlevel order")
Utilities.traverse_levelorder(bst.get_root(), op)
