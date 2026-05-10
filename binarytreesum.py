class Node():
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    
    def sum_tree_recursive(root):
        if root is None:
            return 0
        return sum_tree_recursive(root.left)+sum_tree_recursive(root.right)+root.key

if __name__ == '__main__':
    root=Node(1)
    root.left(2)
    root.right(3)
    root.left.left(4)
    root.left.right(5)
    root.right.left(6)
    root.right.left(7)

    total_sum=sum_tree_recursive(root)
    print(f"Sum of all the nodes are:"{total_sum})