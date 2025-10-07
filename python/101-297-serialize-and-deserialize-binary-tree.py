# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

    # version without global variable in class 'i'
    # def deserialize(self, data):
    #     nodes = data.split(',')

    #     def dfs(i):
    #         if nodes[i] == 'N':
    #             return (None, i + 1)
            
    #         node = TreeNode(int(nodes[i]))
    #         i += 1
    #         node.left, i = dfs(i)
    #         node.right, i = dfs(i)
    #         return (node, i)

    #     return dfs(0)[0]

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))