class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            # Get the current bits, defaulting to 0 if index is out of range
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            # Calculate the sum and carry
            total = bit_a + bit_b + carry
            current_bit = total % 2
            carry = total // 2

            # Append the current bit to the result
            result.append(str(current_bit))

            # Move to the next bits
            i -= 1
            j -= 1

        # Reverse the result to get the correct order
        return ''.join(result[::-1])
