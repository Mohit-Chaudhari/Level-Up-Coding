# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 30/11/21
# -----------------------------------------------


class TreeNode:

    def __init__(self, x):
        self.data = x
        self.right = None
        self.left = None


class Solution:

    def top_view(self, view):

        print("TOP VIEW: ", end=" ")
        for key in view.keys():
            print(view[key][0].data, end=" ")
        print()

    def bottom_view(self, view):

        print("BOTTOM VIEW: ", end=" ")
        for key in view.keys():
            print(view[key][len(view[key]) - 1].data, end=" ")
        print()

    def left_view(self, view):

        n = len(view)

        print("LEFT VIEW : ", end=" ")
        for i in range(n):
            print(view[i][0], end=" ")
        print()

    def right_view(self, view):

        n = len(view)

        print("RIGHT VIEW : ", end=" ")
        for i in range(n):
            print(view[i][len(view[i]) - 1], end=" ")
        print()

    def driver(self, root):

        if root is None:
            print("Tree not present")
            return

        q = list()
        bfs = list()
        mp = dict()

        q.append((root, 0))

        while q:

            count = len(q)
            level = list()

            while count > 0:

                temp = q.pop(0)
                level.append(temp[0].data)

                if temp[0].left:
                    q.append((temp[0].left, temp[1] - 1))

                if temp[0].right:
                    q.append((temp[0].right, temp[1] + 1))

                if temp[1] in mp.keys():
                    mp[temp[1]].append(temp[0])
                else:
                    mp[temp[1]] = [temp[0]]

                count -= 1
            bfs.append(level)

        self.left_view(bfs)
        self.right_view(bfs)
        self.top_view(mp)
        self.bottom_view(mp)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.right.right.right = TreeNode(9)

    s = Solution()
    s.driver(root)
