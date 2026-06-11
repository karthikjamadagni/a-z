#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        # Code here
        i = 0
        n = len(post_exp)
        st = []
        
        while (i < n):
            ch = post_exp[i]
            
            if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') or (ch >= '0' and ch <= '9')):
                st.append(ch)
                
                
            else:
                t1 = st[-1]
                st.pop()
                t2 = st[-1]
                st.pop()
                
                con = ch + t2 + t1
                
                st.append(con)
                
            i += 1
            
        return st[-1]