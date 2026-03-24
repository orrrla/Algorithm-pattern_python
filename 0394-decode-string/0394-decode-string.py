class Solution:
    def decodeString(self, s: str) -> str:
        cur_str = ''
        cur_num = 0
        num_st = []
        str_st = []

        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 +int(c)
            elif c == '[':
                num_st.append(cur_num)
                str_st.append(cur_str)
                cur_num = 0
                cur_str = ''
            elif c == ']':
                repeat = num_st.pop()
                pre_str = str_st.pop()
                cur_str = pre_str + repeat * cur_str

            else:
                cur_str+=c

        return cur_str