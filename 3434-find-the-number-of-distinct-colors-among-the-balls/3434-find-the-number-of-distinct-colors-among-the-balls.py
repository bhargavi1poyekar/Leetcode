class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = Counter()
        color_count = {}
        result = []

        for ball, color in queries:
            
            if ball_color[ball] != 0:
                prev_color = ball_color[ball]
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    del color_count[prev_color]
            
            ball_color[ball] = color
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1
            
            result.append(len(color_count))

        return result
                


