class Solution:
    def isValid(self, s: str) -> bool:
        # Step 1: Define matching pairs
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        # Step 2: Process each character in the string
        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                # Pop from the stack if available, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the top element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # Step 3: If the stack is empty, all brackets were matched
        return not stack
