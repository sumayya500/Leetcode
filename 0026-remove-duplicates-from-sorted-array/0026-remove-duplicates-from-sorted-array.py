class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        # Initialize a pointer for the last unique element
        j = 0
        
        # Traverse the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:  # Found a new unique element
                j += 1             # Move the pointer
                nums[j] = nums[i]  # Update the position with the new unique element
        
        # Return the number of unique elements
        return j + 1
