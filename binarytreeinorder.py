from binarytree import build

class Node:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.val=key
    
def print_inorder(root):
    if root:
        print_inorder(root.left)

        print(root.val, end="")

        print_inorder(root.right)
    

if __name__ == '__main__':
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)

tree_list=[1,2,3,4,5]
visual_tree=build(tree_list)
print("\nBinary tree visualization")
print(visual_tree)
print("Inorder traversal of binary tree is:")
print_inorder(root)
print()
