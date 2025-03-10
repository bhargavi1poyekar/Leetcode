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
        tree_str=[]
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if not node:
                tree_str.append('Null')
            else:
                tree_str.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        
        return '/'.join(tree_str)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data=data.split('/')
        if data[0]=='Null':
            return None

        idx=1
        root=TreeNode(int(data[0]))
        queue=deque([root])
        while queue:
            if data[idx]=='Null':
                queue[0].left=None
                idx+=1
            else:  
                queue[0].left=TreeNode(int(data[idx]))
                queue.append(queue[0].left)
                idx+=1

            if data[idx]=='Null':
                queue[0].right=None
                idx+=1
            else:    
                queue[0].right=TreeNode(int(data[idx]))
                queue.append(queue[0].right)
                idx+=1
            queue.popleft()
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))