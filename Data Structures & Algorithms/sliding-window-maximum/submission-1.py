class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # to store the results
        res = []
    
        # create deque to store max values
        dq = deque()

        # Process first k (or first window) elements of array
        for i in range(0, k):
        
            # For every element, the previous smaller elements 
            # are useless so remove them from dq
            while dq and nums[i] >= nums[dq[-1]]:
            
                # Remove from rear
                dq.pop()

            # Add new element at rear of queue
            dq.append(i)

        # Process rest of the elements, i.e., from arr[k] to arr[n-1]
        for i in range(k, len(nums)):
        
            # The element at the front of the queue is the largest 
            # element of previous window, so store it
            res.append(nums[dq[0]])

            # Remove the elements which are out of this window
            while dq and dq[0] <= i - k:
            
                # Remove from front of queue
                dq.popleft()

            # Remove all elements smaller than the currently being 
            # added element (remove useless elements)
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            # Add current element at the rear of dq
            dq.append(i)

        # store the maximum element of last window
        res.append(nums[dq[0]])

        return res