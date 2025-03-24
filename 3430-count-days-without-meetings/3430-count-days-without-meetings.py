class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        if not meetings:
            return days

        # Sort meetings by their start day
        meetings.sort()
        
        # Merge intervals
        merged_meetings = []
        start, end = meetings[0]
        
        for i in range(1, len(meetings)):
            current_start, current_end = meetings[i]
            if current_start <= end + 1:  # Overlapping or contiguous intervals
                end = max(end, current_end)
            else:
                merged_meetings.append((start, end))
                start, end = current_start, current_end
        
        # Append the last interval
        merged_meetings.append((start, end))
        
        # Calculate available days
        available_days = 0
        previous_end = 0
        
        for start, end in merged_meetings:
            # Days between the previous end and the current start are available
            available_days += start - previous_end - 1
            previous_end = end
        
        # Days after the last meeting are available
        available_days += days - previous_end

        return available_days