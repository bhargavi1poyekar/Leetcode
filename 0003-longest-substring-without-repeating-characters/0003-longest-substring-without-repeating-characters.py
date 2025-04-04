class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        '''
        Understand: substring -> continous section of the string. 
        longest without duplicate chars. 

        can there be empty strs -> return 0
        chars -> numbers -> alphabets ? 

        Match:
        Sliding window -> to find the substring
        Since we want to find longest: we will have variable length sliding window. 
        
        Plan:

        we have hash_index -> to keep track of when we saw the characters last time. 

        then we keep on increasing the window from right till we get a duplicate char -> already present in the hash_index. 

        once we get it. Now we need to decrement the sliding window from left -> we will bring it either till last occ of that char + 1 or if we have already moved on, that is our window no longer contains that char, then we keep left as it is. 

        now, we just check the length, and compare with longest we have encountered so far. 
        '''

        # Implement

        left = 0
        max_length = 0
        hash_index = Counter()

        for right in range(len(s)):
            # if duplicate char
            if s[right] in hash_index:
                left = max(left, hash_index[s[right]])
                # max of left, and last occ + 1

            # Update the hash index with curr index
            hash_index[s[right]] = right + 1

            # Update max_length
            max_length = max(max_length, right - left + 1)
        return max_length

        '''
        Review:
        Eg: s = "pwwkew"
        left = 3
        hash_index = {p:1, w:6, k:4, e:5}
        right = 5
        max_length = 3 -> return 3

        Evaluation:
        Time Complexity: O(n) -> traversing the string
        Space Complexity: O(n) -> for hash
        '''



