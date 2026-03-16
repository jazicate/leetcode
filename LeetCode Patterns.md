## 1. Hash Map / Hash Set
One of the **most common patterns** in interviews.
### When to use
- Counting frequency
- Checking duplicates
- Finding complements
### Example problems
- Two Sum
- Group Anagrams
- Longest Consecutive Sequence
### Idea
Store values for **O(1) lookup**.
Example:
```
map[value] = index
```

---
## 2. Two Pointers
Two indices move through the array.
### When to use
- Sorted arrays
- Palindrome checks
- Pair problems
### Pattern
```
left = 0  
right = n - 1  
  
while left < right:
```
### Example problems
- Container With Most Water
- 3Sum
- Valid Palindrome

Two-pointer techniques can reduce many problems from **O(n²) to O(n)**.

---
## 3. Sliding Window
Used for **subarray / substring problems**.
### When to use
- Longest substring
- Maximum/minimum window
- Fixed-length subarrays
### Pattern
```
left = 0  
for right in range(n):  
    expand window  
    shrink window if needed
```
### Example problems
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Maximum Average Subarray

Sliding window optimizes brute force by maintaining a moving window over elements.

---
## 4. Fast and Slow Pointers
Also called **Floyd’s algorithm**.
### When to use
- Linked list cycle detection
- Find middle of list
### Pattern
```
slow = head  
fast = head  
  
while fast and fast.next:  
    slow = slow.next  
    fast = fast.next.next
```
### Example problems
- Linked List Cycle
- Middle of Linked List

---
## 5. Binary Search
For **sorted data or search space problems**.
### When to use
- Sorted arrays
- Rotated arrays
- Find boundaries
### Pattern
```
left = 0  
right = n-1  
  
while left <= right:  
    mid = (left + right)//2
```
### Example problems
- Binary Search
- Search in Rotated Sorted Array
- Find Peak Element

---
## 6. Prefix Sum
Precompute cumulative sums.
### When to use
- Range sum queries
- Subarray sums
### Pattern
```
prefix[i] = prefix[i-1] + nums[i]
```
### Example problems
- Subarray Sum Equals K
- Range Sum Query

Prefix sums allow range sums to be computed in **O(1)** time.

---
## 7. Stack / Monotonic Stack
### When to use
- Next greater element
- Histogram problems
- Parentheses matching
### Example problems
- Daily Temperatures
- Largest Rectangle in Histogram
- Valid Parentheses

---
## 8. Heap / Priority Queue
### When to use
- Top K problems
- K largest / smallest
### Pattern
```
import heapq  
heapq.heappush(heap, value)
```
### Example problems
- Kth Largest Element
- Top K Frequent Elements

---
## 9. DFS (Depth First Search)
### When to use
- Trees
- Graph traversal
- Backtracking
### Example problems
- Maximum Depth of Binary Tree
- Number of Islands

DFS explores **one path deeply before backtracking**.

---
## 10. BFS (Breadth First Search)
### When to use
- Shortest path
- Level order traversal
### Pattern
```
queue = deque([start])  
while queue:
```
### Example problems
- Binary Tree Level Order
- Word Ladder

---
## 11. Backtracking
### When to use
- Generate combinations
- Permutations
- Sudoku
### Example problems
- Permutations
- Subsets
- Combination Sum

---
## 12. Dynamic Programming
### When to use
- Overlapping subproblems
- Optimal choices
### Types
- Memoization (top-down)
- Tabulation (bottom-up)
### Example problems
- Climbing Stairs
- Coin Change
- Longest Increasing Subsequence

---
## 13. Union-Find (Disjoint Set)
### When to use
- Connected components
- Graph grouping
### Example problems
- Number of Provinces
- Accounts Merge

---
## 14. Interval Problems
### When to use
- Scheduling
- Overlapping ranges
### Example problems
- Merge Intervals
- Meeting Rooms

---
## 15. Greedy
### When to use
- Local optimum leads to global optimum
### Example problems
- Jump Game
- Gas Station