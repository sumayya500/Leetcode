class Solution:
    def lengthOfLastWord(self, s: str) -> int:  # Changed to camelCase
        """
        Returns the length of the last word in the given string `s`.
        A word is defined as a maximal substring consisting of non-space characters only.
        """
        # Step 1: Trim the string to remove leading and trailing spaces
        trimmed_s = s.strip()
        
        # Step 2: Split the string into words using spaces
        words = trimmed_s.split()
        
        # Step 3: Find the last word and return its length
        last_word = words[-1]
        return len(last_word)

# Example usage:
solution = Solution()

# Test cases
print(solution.lengthOfLastWord("Hello World"))               # Output: 5
print(solution.lengthOfLastWord("   fly me   to   the moon  ")) # Output: 4
print(solution.lengthOfLastWord("luffy is still joyboy"))       # Output: 6
