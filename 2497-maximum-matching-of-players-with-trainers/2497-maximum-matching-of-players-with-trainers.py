class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        p_ptr,t_ptr=0,0

        match_count=0

        players=sorted(players,reverse=True)
        trainers=sorted(trainers,reverse=True)

        while p_ptr<len(players) and t_ptr<len(trainers):
            # print(p_ptr,t_ptr,match_count)
            if players[p_ptr]<=trainers[t_ptr]:
                t_ptr+=1
                match_count+=1
            p_ptr+=1
        
        return match_count
        
