class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def printsinglechildnote(root):
    if root is None:
        return
    result=[]

    def traverse(node):
        if node is None:
            return
        
        if (node.left is not None and node.right is None) or \
           (node.left is None and node.right is not None):
             result.append(node.data)

        traverse(node.left)
        traverse(node.right)
    traverse(root)

    if len(result) == 0:
        print(-1)
    else:
        print("Node with exactly one child")
        for x in result:
            print(x, end="")

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

printsinglechildnote(root)