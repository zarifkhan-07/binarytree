class Node:
    def __init__(self,value):
        self.right=None
        self.left=None
        self.value=value

def search(root,key):
    current=root

    while current:
        if root.value == key:
            return True
        
        elif key < current.value:
            current=current.left 
        
        else:
            current=current.right

root=Node(50)
root.left=Node(30)
root.right=Node(70)
root.left.left=Node(20)
root.left.right=Node(40)
root.right.left=Node(65)
root.right.left=Node(80)

key=40

if search(root,key):
    print(f"{key} found.")

else:
    print(f"{key} not found.")
    