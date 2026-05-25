class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key,end="")
        inorder(root.right)

def insert(node,key):
    if node is None:
        return Node(key)
    
    if key<node.key:
        node.left=insert(node.left,key)
    
    else:
        node.right=insert(node.right,key)
    
    return node

def minValNode(node):
    current=node

    while (current.left is not None):
        current=current.left
    return current

def deleteNode(root,key):
    if root is None:
        return root
    
    if key<root.key:
        root.left=deleteNode(root.left,key)

    elif(key>root.key):
        root.right=deleteNode(root.right,key)
    
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        
        elif root.left is None:
            temp=root.right
            root=None
            return temp
        
        temp=minValNode(root.right)
        root.key=temp.key
        root.right=deleteNode(root.key,temp.key)

        return root

root=None
root=insert(root,50)
root=insert(root,30)
root=insert(root,20)
root=insert(root,40)
root=insert(root,70)
root=insert(root,60)
root=insert(root,80)

print("Inorder traversel of the gven tree")
inorder(root)

print("\nDelet 20")
root=deleteNode(root,20)

print("Inorder travarsal of the modified tree.")
inorder(root)
