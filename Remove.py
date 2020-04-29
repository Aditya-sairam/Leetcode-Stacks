#Remove all the adjacent elements in a string using stack

class Solution:
    def removeDuplicates(self, S: str) -> str:
        st = ""
        stack = []
        stack.append(S[0])
        for i in range(1,len(S)):
            if len(stack) > 0:
                if stack[-1] != S[i]:
                    stack.append(S[i])
                else:
                    stack.pop()
            else:
                stack.append(S[i])
                
        for i in stack:
            st += i
        
        return st
