class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        Understand: 

        Given arr -> asteroids -> integers. 
        indices -> relative position 

        abs val -> size, 
        sign -> direction.  + means right, - means left. 

        speed is same for all. 

        conditions of collision:
        1. if 2 meet -> smaller will explode
        2. if both same -> both will explode. 
        3. asteroids in same direction will never meet. 

        Never meet
        + +  
        - - 
        - + -> opposite direction away from each other. 

        Only asteroids -> + -

        Can size of asteroid be 0 -> ? no

        Match: Stack -> LIFO to get the previous asteroids for collision. 

        Plan:

        we are only concerned about the + - negative collision. 

        explode = False

        for ast in asteroids:
            while curr ast is negative and previous(stack top) is positive:
                stack top size > curr asteroid
                    explode = true
                    break
                stack top size == curr asteroid
                    stack.pop()
                    explode = True
                    break
                
                stack top < curr aster
                    stack.pop
                    explode = False
                
            if not explode:
                stack.append(curr asteroid)
        '''

        # Implement:
        stack = []
        
        for ast in asteroids:
            explode = False # initially the curr asteroid is set to not explode on collision

            # while curr asteroid and previous asteroid are moving towards each other
            while ast < 0 and stack and stack[-1] > 0:

                # get the size of both asteroids
                ast_size = abs(ast)
                prev_size = abs(stack[-1])

                # If prev ast size greater than current, current will explode.
                if prev_size > ast_size:
                    explode = True
                    break

                # If both equal size, then both explode
                elif prev_size == ast_size:
                    explode = True
                    stack.pop()
                    break
                
                # if prev is smaller in size, only it will explode. 
                else:
                    stack.pop()
            
            # if explode is set to False, append it to stack
            if not explode:
                stack.append(ast)
        
        # return remaining asteroids
        return stack

        '''
        Time COmplexity: O(n)
        Space Complexity: O(n)
        '''
        
            




