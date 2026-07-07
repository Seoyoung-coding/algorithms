class Solution:
    def isValid(self, s: str) -> bool:
        # Creating a stack to keep track of opening parentheses
        stack = []

        # Iterating through each character in the input string
        for c in s:
            # If the character is an opening parenthesis, push it onto the stack
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                # If stack is empty and we have a closing parenthesis, the string is not balanced
                if not stack:
                    return False

                # Pop the top character from the stack
                top = stack.pop()

                # If the character is a closing parenthesis, check whether
                # it corresponds to the most recent opening parenthesis
                if c == ')' and top != '(':
                    return False
                if c == '}' and top != '{':
                    return False
                if c == ']' and top != '[':
                    return False
        # If the stack is empty, all opening parentheses had a corresponding closing match
        return not stack