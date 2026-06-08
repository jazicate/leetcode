# 215. Kth Largest Element in an Array - medium
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
            A straight forward approach would be to sort the array then return the element at index n-k, but that would take O(nlogn) time. A better solution would be to use a min-heap where we keep the heap size of k. We push an element into the heap, and every time the heap gets above k, we would heappop the smallest element. At the end, he first element in the heap should be the kth largest element.

            Intuitively, the min-heap is a list of size k that holds the largest elements, and of course the first element would be the kth largest element of nums.
        '''
        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

    # O(nlogk) tme, O(k) space

    '''
        This is optimal, but if we do quicker sorting algorithm like quickselect, we can get better average runtime performance with O(n), but a worst-case of O(n^2).
    '''