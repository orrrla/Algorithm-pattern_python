class Solution:
    def calculate(self, num1, num2, opt):
        if opt == "/":
            return int(num1 / float(num2))
        elif opt =="*":
            return num1 * num2
        elif opt=="+":
            return num1+num2
        else:
            return num1-num2

    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            try:
                st.append(int(i))
            except:
                num2 = st.pop()
                num1 = st.pop()
                st.append(self.calculate(num1,num2,i))
        return st[0]

    