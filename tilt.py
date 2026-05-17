class newNode:
    def __init__(self,data):
        self.val=data
        self.left=self.right=None
def traverse(root, title):
    if (not root):
        return 0
    left=traverse(root.left,title)
    right=traverse(root.right,title)

    tilt[0]+=abs(left-right)

    return left+right+root.val

def tilt(root):
    tilt=[0]
    traverse(root,tilt)
    return tilt[0]

if __name__=='__main__':
    root=None
    root=newNode(4)
    root.left=newNode(5)
    root.right=newNode(6)
    root.left.left=newNode(7)
    root.left.right=newNode(8)
    root.right.right=newNode(9)

    print("Tilt:",tilt(root))