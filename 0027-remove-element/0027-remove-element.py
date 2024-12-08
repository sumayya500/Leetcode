class Solution:
    def removeElement(self, nums, val):
        # Initialize a pointer for valid elements
        j = 0
        
        # Traverse the array
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]  # Place valid element at index j
                j += 1  # Increment j for the next position
        
        # Return the count of elements not equal to val
        return j
