# 2013 Summer Entrance Examination

### Department of Creative Informatics

### Graduate School of Information Science and Technology

### The University of Tokyo

## Programming

### Table 1: L's instructions

| Instruction | Description                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------- |
| ADD &emsp; $α$&emsp;$β$     | Add $α$ to $β$. The new value of $β$ is $α + β$. $β$ must be a variable name.                                               
| CMP &emsp; $α$&emsp;$β$     | Skip the next instruction if $α$ equals $β$. Otherwise, move to the next instruction.                                       |
| JMP &emsp; $α$&emsp;$β$     | Jump to the instruction $α$ lines below the current one (If $α$ is a negative integer, then jump backward). $β$ is not used.|
| PRN &emsp; $α$&emsp;$β$     | Print $α$ and $β$ and then terminate the execution.                                                                         |
| SET &emsp; $α$&emsp;$β$     | Set $α$ to $β$. $α$ must be a variable name.                                                                                |

$α$ and $β$ are either an integer literal or a variable name.

(1) The USB memory stick contains `prog1.txt`, which is a code written in L. Write a program that reads this L code and prints the first operand of each line. For example, if a line is:

```
SET x 1
```

then the first operand is x and the second is 1. So x is printed.

(2) Explain the behavior of the following L code:

```
SET x 1
SET y 0
ADD x y
ADD 1 x
CMP x 10
JMP -3 0
PRN x y
```

(3) Write a program that reads an L code and executes it. Test your program with `prog2.txt` on the USB memory stick. You do not have to implement the instructions CMP or JMP, which are not used in `prog2.txt`. You can assume that only valid L code is given to your program and the size of the L code is less than 100 lines.

(4) Extend your program written for (3) to support all the instructions in Table 1. Make any words consisting of a to z available as variables in L. For example, `i` and `count` are variables. Test your program with `prog3.txt` on the USB memory stick.

(5) Extend your program written for (4) to support the new instructions SUB (subroutine call) and BAK (go back) in Table 2. Allow nested subroutine calls. Test your program with `prog4.txt` on the USB memory stick.

(6) Extend your program written for (5) to support the new instructions CAL (call) and RET (return) in Table 3. These instructions are used for a function call. Test your program with `prog5.txt` on the USB memory stick. Note that variables after CAL till RET must be treated as local variables. The instructions must allow recursive function calls. A function argument is available through a special variable `in` till RET is executed while a return value of the last function call is available through a special variable `out`.

### Table 2: SUB and BAK

| Instruction    | Description |
| ----------- |----------------------------------------------------------------------------------------------------------------- |
| SUB  $α$&emsp;$β$     | Record a return position and jump to the instruction $α$ lines below the current one (if $α$ is a negative integer, jump backward). $β$ is not used.   |
| BAK $α$&emsp;$β$     | Return to the position recorded by SUB. $α$ and $β$ are not used.|


$α$ and $β$ are either an integer literal or a variable name.

### Table 3: CAL and RET

| Instruction | Description |
| ----------- | ---------------------------------------------------- |
| CAL $α$&emsp;$β$     | Record a return position and jump to the instruction $α$ lines below the current one (if $α$ is a negative integer, jump backward). $β$ is an argument. |
| RET $α$&emsp;$β$     | Return to the position recorded by CAL. $α$ is a return value. $β$ is not used.                                                                       |

$α$ and $β$ are either an integer literal or a variable name.
