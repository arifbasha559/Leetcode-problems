class Solution:
    def isValid(self, s: str) -> bool:
        # Early exit for odd-length strings
        if len(s) % 2 != 0:
            return False
            
        stack = []
        # Dictionary to keep track of matching brackets
        mapping = {")": "(", "}": "{", "]": "["}
        
        for bracket in s:
            if bracket in mapping:
                # Pop the top element if stack isn't empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the popped element doesn't match the mapped opening bracket, it's invalid
                if mapping[bracket] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(bracket)
                
        # If the stack is empty at the end, all brackets were matched correctly
        return len(stack) == 0