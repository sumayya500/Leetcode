class Solution:
    def plusOne(self, digits):
        n = len(digits)
        # Start from the last digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, set it to 0
            digits[i] = 0
        # If all digits were 9, we need to add a leading 1
        return [1] + digits
