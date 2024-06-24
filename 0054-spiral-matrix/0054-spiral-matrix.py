class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        spiral=[]
        i=0
        j=-1
        m=len(matrix)
        n=len(matrix[0])
        for l in range(len(matrix[0])):
            
            for r in range(n):
                
                if l%2==0:
                    j+=1
                else:
                    j-=1
                # print(f'{i}{j}')
                spiral.append(matrix[i][j])
                
            n-=1
            for k in range(m-1):
                # print(k)
                if l%2==0:
                    i+=1
                else:
                    i-=1
                # print(f'{i}{j}')
                spiral.append(matrix[i][j])
            m-=1
            if n==0 or m==0:
                break
            # print(spiral)
                
        return(spiral)
            