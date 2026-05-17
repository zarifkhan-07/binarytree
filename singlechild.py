class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printklevelsdown(node,k):
    if node is None or k <0:
        return
    if k==0:
        print(node.data)
        return
    printklevelsdown(node.left,k-1)
    printklevelsdown(node.right,k-1)

if __name__=='__main__':
    root=Node(10)
    root.left=Node(20)
    root.right=Node(30)
    root.left.left=Node(40)
    root.left.right=Node(50)
    root.right.right=Node(60)
    root.left.left.left=Node(70)

    k=-1
    print(f"level {k} nodes:")
    printklevelsdown(root,k)
    