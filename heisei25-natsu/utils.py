from __future__ import annotations

from pathlib import Path

def read_from_file(path: str) -> list[tuple[str, str, str]]:
    contents = Path(path).read_text(encoding="utf-8").replace("\r", "").strip()

    if not contents:
        return []
    lines: list[str] = [line.strip() for line in contents.split("\n")]
    commands: list[tuple[str, str, str]] = []
    for line in lines:
        parts = line.split(" ")
        if len(parts) != 3:
            raise ValueError("invalid command format")
        cmd, arg1, arg2 = parts
        commands.append((cmd, arg1, arg2))
    return commands

class LMachine_simple:
    """
    L 语言解释器（只允许变量 x 和 y）:
    - 变量: 只有 x, y 两个，初值为 0
    - 指令: SET, ADD, CMP, JMP, PRN, SUB, BAK
    - 每条指令的形式固定为三段: op α β
    """

    def __init__(self, program: list[tuple[str, str, str]]) -> None:
        self.program: list[tuple[str, str, str]] = program
        self.ptr: int = 0       # 程序计数器 (0-based 行号)
        self.x: int = 0
        self.y: int = 0
        self.call_stack: list[int] = []  # SUB/BAK 使用的返回地址栈

    # --------- 读取程序 ---------

    @staticmethod
    def read_from_file(path: str) -> list[tuple[str, str, str]]:
        """
        从文件中读取 L 程序，每行拆成 (op, α, β)
        """
        contents = Path(path).read_text(encoding="utf-8").replace("\r", "").strip()
        if not contents:
            return []

        program: list[tuple[str, str, str]] = []
        for raw_line in contents.split("\n"):
            line = raw_line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 3:
                raise ValueError(f"invalid command format: {raw_line!r}")
            op, a, b = parts
            program.append((op, a, b))

        return program

    @classmethod
    def from_file(cls, path: str) -> LMachine_simple:
        return cls(cls.read_from_file(path))

    # --------- 辅助函数 ---------

    def _get_value(self, token: str) -> int:
        """
        把 α / β 解析成整数:
        - 'x' → 当前 self.x
        - 'y' → 当前 self.y
        - 其它 → 按整数常量解析（支持负号）
        """
        if token == "x":
            return self.x
        if token == "y":
            return self.y
        # 字面量整数
        try:
            return int(token)
        except ValueError:
            raise ValueError(f"illegal operand: {token!r}; only x, y or int literal are allowed")

    def _set_var(self, var: str, value: int) -> None:
        """
        只能给 x / y 赋值
        """
        if var == "x":
            self.x = value
        elif var == "y":
            self.y = value
        else:
            raise ValueError(f"illegal variable: {var!r}; only 'x' and 'y' exist")

    def _check_jump(self, target: int) -> None:
        if target < 0 or target >= len(self.program):
            raise ValueError(f"jump target {target} out of range")

    # --------- 指令实现 ---------

    def op_SET(self, a: str, b: str) -> None:
        """
        SET α β : 把 β 的值赋给变量 α
        α 必须是 x 或 y
        """
        value = self._get_value(b)
        self._set_var(a, value)
        self.ptr += 1

    def op_ADD(self, a: str, b: str) -> None:
        """
        ADD α β : β := β + α, β 必须是 x 或 y
        α 可以是常量，或 x / y
        """
        add_val = self._get_value(a)
        if b == "x":
            self.x += add_val
        elif b == "y":
            self.y += add_val
        else:
            raise ValueError(f"ADD: β must be 'x' or 'y', got {b!r}")
        self.ptr += 1

    def op_CMP(self, a: str, b: str) -> None:
        """
        CMP α β :
        - 若 α == β，则跳过下一条指令 (ptr += 2)
        - 否则正常执行下一条 (ptr += 1)
        α / β 都可以是常量或 x / y
        """
        va = self._get_value(a)
        vb = self._get_value(b)
        if va == vb:
            self.ptr += 2
        else:
            self.ptr += 1

    def op_JMP(self, a: str, b: str) -> None:
        """
        JMP α β : 无视 β，跳到当前行 + α
        α 可以是常量或 x / y
        """
        offset = self._get_value(a)
        new_ptr = self.ptr + offset
        self._check_jump(new_ptr)
        self.ptr = new_ptr

    def op_PRN(self, a: str, b: str) -> None:
        """
        PRN α β : 打印 α 和 β 的值，然后结束程序
        """
        va = self._get_value(a)
        vb = self._get_value(b)
        print(va, vb)
        self.ptr = len(self.program)  # 让 run() 结束

    def op_SUB(self, a: str, b: str) -> None:
        """
        SUB α β :
        - 记录返回地址 (下一条指令的位置)
        - 再按 α 的值进行相对跳转
        β 被保留但不使用（为了保持三元格式）
        """
        offset = self._get_value(a)
        ret = self.ptr + 1
        new_ptr = self.ptr + offset
        self._check_jump(new_ptr)
        self.call_stack.append(ret)
        self.ptr = new_ptr

    def op_BAK(self, a: str, b: str) -> None:
        """
        BAK α β :
        - 从栈中弹出返回地址
        - 跳回该地址继续执行
        α / β 都不使用
        """
        if not self.call_stack:
            raise ValueError("BAK called with empty call stack")
        self.ptr = self.call_stack.pop()

    # --------- 执行循环 ---------

    def step(self) -> None:
        """
        执行当前 ptr 指向的一条指令
        """
        if not (0 <= self.ptr < len(self.program)):
            # 超出范围就让 run() 结束
            self.ptr = len(self.program)
            return

        op, a, b = self.program[self.ptr]

        if op == "SET":
            self.op_SET(a, b)
        elif op == "ADD":
            self.op_ADD(a, b)
        elif op == "CMP":
            self.op_CMP(a, b)
        elif op == "JMP":
            self.op_JMP(a, b)
        elif op == "PRN":
            self.op_PRN(a, b)
        elif op == "SUB":
            self.op_SUB(a, b)
        elif op == "BAK":
            self.op_BAK(a, b)
        else:
            raise ValueError(f"unknown instruction {op!r} at line {self.ptr}")

    def run(self) -> None:
        """
        从当前 ptr 执行到结束（PRN 或 ptr 越界）
        """
        while 0 <= self.ptr < len(self.program):
            self.step()


