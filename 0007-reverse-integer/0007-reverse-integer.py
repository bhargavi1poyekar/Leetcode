class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=1
        if(x<0):
            sign=-1
            x=abs(x)
        
        x_rev=int(str(x)[::-1])
        
        if x_rev*sign>=-2147483648 and x_rev*sign<2147483648 :
            return x_rev*sign
        else:
            return 0
        
        
        
        
        