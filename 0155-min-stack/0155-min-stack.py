class MinStack:
    def __init__(self):
        self.stack = []      # 数据栈
        self.min_stack = []  # 最小值栈

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 如果最小值栈为空，或者 val 小于等于当前最小值，则入最小值栈
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            # 如果弹出的值等于当前最小值，也从最小值栈弹出
            if self.min_stack and val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None