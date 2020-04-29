#Baseball score count problem-stacks

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        if len(ops) == 0: return 0; # empty list, exit
        stack = [] # Stack with points
        for x in ops:
            if x == 'C':
                stack.pop() # remove the last
            elif x == 'D':
                stack.append(int(stack[-1])*2) # double points
            elif x == '+':
                stack.append(int(stack[-1])+int(stack[-2])) # two last combined
            else:
                stack.append(int(x)) # just add to stack if no other options
        return sum(stack) # Plain summ of stack
        
