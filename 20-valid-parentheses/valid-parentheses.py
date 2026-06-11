class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for i in range(len(s)):
            if s[i] in ')]}':
                if  not stk:
                    return False
                x=stk.pop()
                if (x=='(' and s[i]==')') or (x=='{' and s[i]=='}') or (x=='[' and s[i]==']'):
                    continue
                else:
                    stk.append(x)
                    stk.append(s[i])
            stk.append(s[i])
        return False if stk else True
        