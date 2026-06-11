class Solution:
    def infixtoPostfix(self, s):
        # code here
        i = 0
        st = []
        n = len(s)
        ans = ""
        
        while (i < n):
            if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= '0' and s[i] <= '9'):
                ans += s[i]
                
            elif (s[i] == '('):
                st.append(s[i])
                
            elif (s[i] == ')'):
                while len(st) > 0 and st[-1] != '(':
                    ans += st.pop()
                if len(st) > 0:      # ✅ safety check
                    st.pop()
                    
            else:
                while (
                    len(st) > 0 and
                    (
                        self.priority(s[i]) < self.priority(st[-1]) or
                        (self.priority(s[i]) == self.priority(st[-1]) and s[i] != '^')
                    )
                ):
                    ans = ans + st[-1]
                    st.pop()
                    
                st.append(s[i])
                
            i += 1
            
        while len(st) > 0:
            ans = ans + st[-1]
            st.pop()
                
        return ans
        
    def priority(self, char):
        if char == "^":
            return 3
        elif char == "*" or char == "/":
            return 2
        elif char == "+" or char == "-":
            return 1
        else:
            return -1
