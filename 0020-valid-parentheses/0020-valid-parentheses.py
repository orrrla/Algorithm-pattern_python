class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', ']': '[', '}': '{'}
        st = []
        
        for c in s:
            if c in d:  
                if not st or st.pop() != d[c]:
                    return False
            else: 
                st.append(c)
        
        return not st