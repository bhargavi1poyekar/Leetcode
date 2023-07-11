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
        ans=[]
        queue=deque([root])
        while queue:
            for _ in range(len(queue)):
                node=queue.popleft()
                if not node:
                    ans.append('Null')
                else:
                    ans.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
       
        return '/'.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree_str=data.split('/')
        if tree_str[0]=='Null':
            return None

        root=TreeNode(int(tree_str[0]))
        stack=[root]
        idx=1
        while stack:
            if tree_str[idx]!='Null':
                stack[0].left=TreeNode(int(tree_str[idx]))
                idx+=1
                stack.append(stack[0].left)
            else:
                stack[0].left=None
                idx+=1
            if tree_str[idx]!='Null':
                stack[0].right=TreeNode(int(tree_str[idx]))
                idx+=1
                stack.append(stack[0].right)
            else:
                stack[0].right=None
                idx+=1
            stack.pop(0)
        
        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))