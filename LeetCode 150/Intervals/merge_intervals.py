# 56. Merge Intervals - medium
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: # O(nlogn) time, O(1) space
        '''
            given intervals list where each interval is [start, end]
            merge all overlapping intervals
            return a list of the non-overlapping intervals

            Sort intervals first
            Initialize a pointer to track the position of the last merged interval
            Iterate through the intervals starting at index 1
              - if the current interval overlaps with the last merged interval
                -> merge them by updating the end to the max of both
              - else
                - move the write pointer forward
                - copy the current interval to that position
        '''
        if not intervals:
            return []

        intervals.sort()

        write = 0  # Points to the last merged interval
        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[write][1]:
                intervals[write][1] = max(intervals[write][1], intervals[i][1])
            else:
                # Move write pointer forward and overwrite
                write += 1
                intervals[write] = intervals[i]

        return intervals[:write + 1]
