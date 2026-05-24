class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def search(root,key):
    if root is None or root.value==key:
        return root
    
    if key<root.value:
        return search(root.left,key)
    
    else:
        return search(root.right,key)


root=Node(50)
root.left=Node(30)
root.right=Node(70)
root.left.left=Node(20)
root.left.right=Node(40)
root.right.left=Node(65)
root.right.left=Node(80)

key=60
result=search(root,key)

if result:
    print(f"{key} found in BST.")

else:
    print(f"{key} not found on BST.")