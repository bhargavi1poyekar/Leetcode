# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        tree = []

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    tree.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    tree.append('None')
        
        return '/'.join(tree)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree = data.split('/')
        if tree[0] == 'None':
            return None
        
        root = TreeNode(int(tree[0]))
        queue = deque([root])
        idx = 1

        while queue:
            if tree[idx] != 'None':
                node = TreeNode(int(tree[idx]))
                queue[0].left = node
                queue.append(node)
            else:
                queue[0].left = None
            
            idx += 1

            if tree[idx] != 'None':
                node = TreeNode(int(tree[idx]))
                queue[0].right = node
                queue.append(node)
            else:
                queue[0].right = None
            
            idx += 1
            queue.popleft()
        
        return root


        


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))