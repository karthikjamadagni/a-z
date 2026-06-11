class Solution:
    
    def priority(self, ch):
        if ch == "^":
            return 3
        elif ch == "*" or ch == '/':
            return 2
        elif ch == '+' or ch == '-':
            return 1
        else:
            return -1
            
    def infixToPrefix(self, s):
        # reverse the string and swap brackets
        rs = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                rs += ')'
            elif s[i] == ')':
                rs += '('
            else:
                rs += s[i]
            
        i = 0
        st = []
        n = len(rs)
        ans = ""
        
        while i < n:
            if (rs[i] >= 'a' and rs[i] <= 'z') or (rs[i] >= 'A' and rs[i] <= 'Z') or (rs[i] >= '0' and rs[i] <= '9'):
                ans += rs[i]
                
            elif rs[i] == '(':
                st.append(rs[i])
                
            elif rs[i] == ')':
                while st and st[-1] != '(':
                    ans += st.pop()
                if st:
                    st.pop()
                
            else:
                while st and (
                    self.priority(rs[i]) < self.priority(st[-1]) or
                    (self.priority(rs[i]) == self.priority(st[-1]) and rs[i] == '^')
                ):
                    ans += st.pop()
                    
                st.append(rs[i])
                
            i += 1
                
        while st:
            ans += st.pop()
            
        # reverse postfix to get prefix
        prefix = ""
        for i in range(len(ans) - 1, -1, -1):
            prefix += ans[i]
            
        return prefix
