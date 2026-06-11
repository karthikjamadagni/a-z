#User function Template for python3

class Solution:
    def postToInfix(self, postfix):
        # Code here
        i = 0
        st = []
        
        n = len(postfix)
        
        while (i < n):
            if ((postfix[i] >= 'a' and postfix[i] <= 'z') or (postfix[i] >= 'A' and postfix[i] <= 'Z') or (postfix[i] >= '0' and postfix[i] <= '9')):
                st.append(postfix[i])
                
            else:
                t1 = st[-1]
                st.pop()
                t2 = st[-1]
                st.pop()
                
                con = '(' + t2 + postfix[i] + t1 + ')'
                
                st.append(con)
                
            i += 1
        return st[-1]