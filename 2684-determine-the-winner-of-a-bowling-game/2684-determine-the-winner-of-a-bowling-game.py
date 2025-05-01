class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        
        def calculate_score(pins):
            score = 0
            prev = False
            prev_2 = False
            
            for i in range(len(pins)):
                # print(prev, prev_2)
                if prev or prev_2:
                    score += pins[i]*2
                else:
                    score += pins[i]
                    
                prev_2 = prev
                if pins[i] == 10:
                    prev = True
                else:
                    prev = False

            return score
        
        score_player1 = calculate_score(player1)
        score_player2 = calculate_score(player2)

        print(score_player1)
        print(score_player2)

        if score_player1 > score_player2:
            return 1
        elif score_player1 < score_player2:
            return 2
        else:
            return 0