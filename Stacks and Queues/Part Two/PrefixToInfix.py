#User function Template for python3

class Solution:
    def preToInfix(self, pre_exp):
        # Code here
        n = len(pre_exp)
        i = n-1
        
        st = []
        
        
        while (i >= 0):
            ch = pre_exp[i]
            if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') or (ch >= '0' and ch <= '0')):
                st.append(ch)
                
            else:
                t1 = st.pop()
                t2 = st.pop()
                
                con = '(' + t1 + ch + t2 + ')'
                
                st.append(con)
                
            i -= 1
            
        return st[-1]