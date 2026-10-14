class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
            
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for bracket in s:
            if bracket in mapping:
                top_element = stack.pop() if stack else '#'
                
                if mapping[bracket] != top_element:
                    return False
            else:
                stack.append(bracket)
        return len(stack) == 0