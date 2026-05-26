import heapq

class Solution:
    def maxSlidingWindow(self, nums, k):

        heap = []
        result = []

        for i in range(len(nums)):

            # Push negative value and index
            heapq.heappush(heap, (-nums[i], i))

            # Remove outside window elements
            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            # Window formed
            if i >= k - 1:
                result.append(-heap[0][0])

        return result