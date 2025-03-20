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
        serialize_list = []
        while queue:
            node = queue.popleft()
            if node:
                serialize_list.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                serialize_list.append('None')
        
        # print(serialize_list)
        
        return '/'.join(serialize_list)
                
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree_list = data.split('/')
        # print(tree_list)
        if tree_list[0] == 'None':
            return None
        root = TreeNode(int(tree_list[0]))
        queue = deque([root])
        tree_idx = 1

        while queue:
            if tree_list[tree_idx] != 'None':
                node = TreeNode(int(tree_list[tree_idx]))
                queue[0].left = node
                queue.append(node)
            else:
                queue[0].left = None
            tree_idx += 1

            if tree_list[tree_idx] != 'None':
                node = TreeNode(int(tree_list[tree_idx]))
                queue[0].right = node
                queue.append(node)
            else:
                queue[0].right = None
            tree_idx += 1
            queue.popleft()
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))