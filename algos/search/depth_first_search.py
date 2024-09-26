class BinaryNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_recur(root: BinaryNode) -> None:

    if not root:
        return
    
    print(root.val)

    if not root.right:
        dfs_recur(root.left)
    
    elif not root.left:
        dfs_recur(root.right)
    
    else:
        dfs_recur(root.left)
        dfs_recur(root.right)


def dfs_iter(root: BinaryNode) -> None:

    stack = [root]

    while stack:

        top = stack.pop()

        print(top.val)

        if top.right:
            stack.append(top.right)

        if top.left:
            stack.append(top.left)



if __name__ == "__main__":

    N1 = BinaryNode(1)
    N2 = BinaryNode(5)
    N3 = BinaryNode(10)
    N4 = BinaryNode(2)
    N5 = BinaryNode(3)
    N6 = BinaryNode(15)

    N1.left = N2
    N2.left = N3
    N1.right = N4
    N4.left = N5
    N4.right = N6

    print("Recursive:")
    dfs_recur(N1)
    
    print("\nIterative")
    dfs_iter(N1)