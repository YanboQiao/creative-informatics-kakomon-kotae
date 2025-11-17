from pathlib import Path


def valid_var_name(var: str) -> bool:
    return var.isalpha() and var.islower()

class LMachine:
    def __init__(self, program: list[tuple[str, str, str]]) -> None:
        self.program: list[tuple[str, str, str]] = program
        self.varlist: dict[str, int] = {}      # 当前帧
        self.call_stack: list[int] = []        # SUB/BAK
        self.func_stack: list[int] = []        # CAL/RET 返回地址
        self.var_stack: list[dict[str, int]] = []  # 变量帧栈（局部作用域）
        self.ptr: int = 0
        self._ops = {
            "SET": self.op_SET,
            "ADD": self.op_ADD,
            "CMP": self.op_CMP,
            "JMP": self.op_JMP,
            "PRN": self.op_PRN,
            "SUB": self.op_SUB,
            "BAK": self.op_BAK,
            "CAL": self.op_CAL,
            "RET": self.op_RET,
        }

    @classmethod
    def read_from_file(cls, path: str):
        contents = Path(path).read_text(encoding="utf-8").replace("\r", "").strip()
        program: list[tuple[str, str, str]] = []
        if contents:
            for raw_line in contents.split("\n"):
                line = raw_line.strip()
                if not line:
                    continue
                parts = line.split()
                if len(parts) != 3:
                    raise ValueError(f"invalid command format: {raw_line!r}")
                op, a, b = parts
                program.append((op, a, b))
        return cls(program)
    
    def _get_value(self, token: str) -> int:
        if token in self.varlist:
            return self.varlist[token]
        if token.lstrip("+-").isdigit():
            return int(token)
        else: 
            raise ValueError(f"This variable {token} has not been declared yet.")
    
    def _set_var(self, var: str, value: int, *, internal: bool = False) -> None:
        if not internal and var in {"in", "out"}:
            raise ValueError("in and out shouldn't be variable name")
        self.varlist[var] = value
    
    def _check_jump(self, target: int) -> None:
        if target < 0 or target >= len(self.program):
            raise ValueError(f"jump {target} out of range")
        
    # 指令实现
    def op_SET(self, a: str, b: str) -> None:
        self._set_var(a, self._get_value(b))
        self.ptr += 1

    def op_ADD(self, a: str, b: str) -> None:
        # β 必须是变量名（题面约束）
        if not valid_var_name(b):
            raise ValueError(f"ADD target {b!r} must be a variable name [a-z]+")
        # 若 β 尚未被赋值，_get_value(b) 会抛出异常；与题面假设“给定有效程序”一致
        result = self._get_value(a) + self._get_value(b)
        self._set_var(b, result)
        self.ptr += 1
    
    def op_CMP(self, a: str, b: str) -> None:
        if self._get_value(a) == self._get_value(b):
            self.ptr += 2
        else:
            self.ptr += 1
    
    def op_JMP(self, a: str, b: str) -> None:
        offset = self._get_value(a)
        target = self.ptr + offset
        self._check_jump(target)
        self.ptr = target
    
    def op_PRN(self, a: str, b: str) -> None:
        print(self._get_value(a), self._get_value(b))
        self.ptr = len(self.program)

    def op_SUB(self, a: str, b: str) -> None:
        offset = self._get_value(a)
        target = self.ptr + offset
        self._check_jump(target)
        self.call_stack.append(self.ptr + 1)
        self.ptr = target
    
    def op_BAK(self, a, b) -> None:
        if not self.call_stack:
            raise ValueError(f"line {self.ptr} BAK with empty call stack")
        self.ptr = self.call_stack.pop()

    def op_CAL(self, a: str, b: str) -> None:
        # 计算目标位置并检查范围
        offset = self._get_value(a)
        target = self.ptr + offset
        self._check_jump(target)

        # 在切换帧前先求出实参的值
        arg_value = self._get_value(b)

        # 记录返回地址与变量帧；创建新的局部帧并设置 in=实参
        self.func_stack.append(self.ptr + 1)
        self.var_stack.append(self.varlist)
        self.varlist = {}
        self._set_var("in", arg_value, internal=True)

        # 跳转到函数入口
        self.ptr = target

    def op_RET(self, a: str, b: str) -> None:
        if not self.func_stack or not self.var_stack:
            raise ValueError(f"line {self.ptr} RET with empty function stack")
        # 取返回值（在当前局部帧求值）
        ret_val = self._get_value(a)

        # 恢复调用者帧并写入 out
        return_addr = self.func_stack.pop()
        caller_frame = self.var_stack.pop()
        self.varlist = caller_frame
        self._set_var("out", ret_val, internal=True)

        # 回到调用点之后
        self.ptr = return_addr

    def run(self) -> None:
        while 0 <= self.ptr < len(self.program):
            op, a, b = self.program[self.ptr]
            fn = self._ops.get(op)
            if fn is None:
                raise ValueError("not a legal op code")
            fn(a, b)
