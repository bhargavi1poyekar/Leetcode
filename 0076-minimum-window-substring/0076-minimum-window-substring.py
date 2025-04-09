class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        '''
        Understand: 

        Given : 2 strings s -> len m and t -> len n
        return -> min win substring -> every char in t (including duplicates) -> is present in the window. 

        if not string -> return empty.

        Answer is unique. 

        Questions:
        can len t > len s -> is possible -> return empty 
        is it case_specific -> ? No 

        Match:
        Sliding window.  

        Plan:

        freq_counter(t) == freq_counter(Window)

        match_count -> should be equal to distinct values of t. -> if yes, then we try to minimize the window. 

        need to return entire substring -> we need to store. min left, min right, and min_length. 
        
        left = 0
        for right in s:
            add s to freq_s of windows. 
            if freq_s[right] == freq_win[right]:
                increment match count

            while match_count ==  distinct t vals:
                update min_length
                decr window. before dec- . check if left is included in match count. if yes, dec match count. 
        
        return the string. 
        '''

        left = 0
        min_length = float('inf')
        min_left = float('inf')
        min_right = float('inf')
        win_freq = Counter()
        t_freq = Counter(t)

        distinct = len(t_freq)
        match = 0

        for right in range(len(s)):
            win_freq[s[right]] += 1
            if win_freq[s[right]] == t_freq[s[right]]:
                match += 1
            
            while match == distinct:
                curr_length = right - left + 1
                if curr_length < min_length:
                    min_length = curr_length
                    min_left = left
                    min_right = right
                
                if win_freq[s[left]] == t_freq[s[left]]:
                    match -= 1
                
                win_freq[s[left]] -= 1
                left += 1
        
        return s[min_left: min_right+1] if min_length != float('inf') else ""