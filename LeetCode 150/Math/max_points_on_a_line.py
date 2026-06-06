# 149. Max Points on a Line - hard
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''
            Approach:
            Make a function that calculates the slope between two points.
            Since multiple lines may exist, we use a hashmap to count frequencies of slopes.
            We loop each point and compare it with the other points.
              - For every point, we treat that as a starting point, then we calculate the slope between that point and every point after that.

            slope = (y2 - y1)/(x2 - x1)

            O(n^2) time, O(n) space
        '''
        def find_slope(point1, point2):
            x1, y1 = point1
            x2, y2 = point2

            if x2 == x1: # Divide by zero edge case/vertical line
                return inf

            return (y2-y1)/(x2-x1)
        
        frequencies = defaultdict(int)
        res = 1 # Make res be 1 since 1 <= points.length <= 300, so at least 1 point exists
        for i in range(len(points)):
            frequencies.clear()
            for j in range(i+1, len(points)):
                slope = find_slope(points[i], points[j])
                frequencies[slope] += 1
                res = max(res, frequencies[slope] + 1) # Add 1 to include current point (points[i])

        return res
