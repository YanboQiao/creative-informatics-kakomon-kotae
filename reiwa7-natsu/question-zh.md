# 2024年8月 东京大学创造情报学 机试
# 编程

请通过编写程序回答下列问题。作答所需的文件都存放在 USB 闪存中，务必在考试结束前把编写好的程序保存回该 USB 闪存。

## 问题

本题会用多种格式表示一个具有 $r$ 行 $c$ 列的矩阵。矩阵中第 $i$ 行第 $j$ 列的元素记为 $(i, j)$ 元素；左上角的元素是 $(1, 1)$，它右边的元素是 $(1, 2)$。对于 $(i, j)$ 元素，其行号为 $i$，列号为 $j$，并且始终满足 $1 \le i \le r$、$1 \le j \le c$。题目给出的任意矩阵，其元素都是 $-9$ 到 $9$ 之间的整数（含端点），任何一行或一列中非零元素都不超过 $10$ 个，总的非零元素数不超过 $10^6$。

<style>
:root{
  --box-bg-light:#f7f7f7;
  --box-fg-light:#222;
  --box-bg-dark:#1e1e1e;
  --box-fg-dark:#f0f0f0;
  --box-border:rgba(140,140,140,.55);
}
.format-box{
  border:1px solid var(--box-border);
  border-radius:6px;
  padding:12px 16px;
  margin:1em 0;
  background:var(--box-bg-light);
  color:var(--box-fg-light);
  line-height:1.55;
}
@media (prefers-color-scheme: dark){
  .format-box{background:var(--box-bg-dark); color:var(--box-fg-dark);}
}
.format-title{
  font-weight:bold;
  display:block;
  margin-bottom:0.4em;
}
</style>
<div class="format-box" markdown="1">
<span class="format-title">格式 1</span>
格式 1 是把矩阵元素按行优先顺序排列而成的数列。在行优先顺序中，上一行的元素一定排在下一行之前，而同一行中更靠左的元素排在更靠右的元素之前。例如，矩阵

$$
\begin{pmatrix}
1 & -5 & 0 \\
0 & 3 & 0
\end{pmatrix}
$$

会表示为

$$
1, -5, 0, 0, 3, 0
$$

的格式 1 表示。
</div>

当一个数列被存入文件时，会以逗号分隔的元素串联为一个字符串后再存储。例如，一个包含四个元素 $2,5,-3,0$ 的数列会对应如下字符串：

$$ 2,5,-3,0 $$

(1). 文件中保存了用格式 1 表示的矩阵数列。对下列每个矩阵，找出元素和最大的那一行，并在答题纸上写出该行的行号与元素和。如果有多行并列最大，可任选其一。

   (a) `data1a.txt` 中存放的 $6$ 行 $4$ 列矩阵。

   (b) `data1b.txt` 中存放的 $100$ 行 $150$ 列矩阵。
<style>
:root{
  --box-bg-light:#f7f7f7;
  --box-fg-light:#222;
  --box-bg-dark:#1e1e1e;
  --box-fg-dark:#f0f0f0;
  --box-border:rgba(140,140,140,.55);
}
.format-box{
  border:1px solid var(--box-border);
  border-radius:6px;
  padding:12px 16px;
  margin:1em 0;
  background:var(--box-bg-light);
  color:var(--box-fg-light);
  line-height:1.55;
}
@media (prefers-color-scheme: dark){
  .format-box{background:var(--box-bg-dark); color:var(--box-fg-dark);}
}
.format-title{
  font-weight:bold;
  display:block;
  margin-bottom:0.4em;
}
</style>

<div class="format-box" markdown="1">
<span class="format-title">格式 2</span>

设矩阵的 $(i, j)$ 元素为 $x_{ij}$。格式 2 被定义为：把所有满足 $x_{ij} \ne 0$ 的 $(i, j)$ 的三个整数 $i, j, x_{ij}$ 按行优先顺序排列得到的数列。  
例如，矩阵

$$
\begin{pmatrix}
1 & -5 & 0 \\
0 & 3 & 0
\end{pmatrix}
$$

会表示为

$$
1, 1, 1, 1, 2, -5, 2, 2, 3
$$

的格式 2 表示。
</div>

(2). 文件中保存了用格式 2 表示的矩阵数列。对下列每个矩阵，找出元素和最大的那一行，并在答题纸上写出该行的行号与元素和。如果有多行并列最大，可任选其一。

   (a) `data2a.txt` 中存放的 $6$ 行 $4$ 列矩阵。

   (b) `data2b.txt` 中存放的 $100$ 行 $150$ 列矩阵。

   (c) `data2c.txt` 中存放的 $10^6$ 行 $10^6$ 列矩阵。

---
<style>
:root{
  --box-bg-light:#f7f7f7;
  --box-fg-light:#222;
  --box-bg-dark:#1e1e1e;
  --box-fg-dark:#f0f0f0;
  --box-border:rgba(140,140,140,.55);
}
.format-box{
  border:1px solid var(--box-border);
  border-radius:6px;
  padding:12px 16px;
  margin:1em 0;
  background:var(--box-bg-light);
  color:var(--box-fg-light);
  line-height:1.55;
}
@media (prefers-color-scheme: dark){
  .format-box{background:var(--box-bg-dark); color:var(--box-fg-dark);}
}
.format-title{
  font-weight:bold;
  display:block;
  margin-bottom:0.4em;
}
</style>

<div class="format-box" markdown="1">
<span class="format-title">格式 3</span>

设 $n_i$ 为把矩阵元素按行优先顺序排列后，第 $i$ 个元素前面连续零的个数；设 $x_i$ 为第 $i$ 个元素的取值。格式 3 被定义为：对所有满足 $x_i \ne 0$ 的 $i$，按 $i$ 递增顺序依次写出成对的整数 $n_i$ 与 $x_i$ 所得到的数列。  
例如，矩阵

$$
\begin{pmatrix}
1 & -5 & 0 \\
0 & 3 & 0
\end{pmatrix}
$$

会表示为

$$
0, 1, 0, -5, 2, 3
$$

的格式 3 表示。
</div>

(3). 文件中保存了用格式 3 表示的矩阵数列。对下列矩阵的**转置矩阵**，找出元素和最大的那一行，并在答题纸上写出该行的行号与元素和。如果有多行并列最大，可任选其一。

   (a) `data3a.txt` 中存放的 $4$ 行 $6$ 列矩阵。

   (b) `data3b.txt` 中存放的 $100$ 行 $150$ 列矩阵。

   (c) `data3c.txt` 中存放的 $10^6$ 行 $10^6$ 列矩阵。

(4). 文件中保存了用**格式 3** 表示的矩阵数列。对下列由**×** 运算得到的矩阵，找出元素和最大的那一行，并在答题纸上写出该行的行号与元素和。如果有多行并列最大，可任选其一。

我们定义二元运算 **×**：给定一个 $r \times m$ 的矩阵 $X$ 与一个 $m \times n$ 的矩阵 $Y$，可得到一个 $r \times n$ 的矩阵。$X \times Y$ 的 $(i, j)$ 元素定义为

$$
(X \times Y)_{ij} = \max_{1 \le k \le m}((X)_{ik}(Y)_{kj}) + \min_{1 \le k \le m}((X)_{ik}(Y)_{kj}),
$$

其中 $(M)_{uv}$ 表示矩阵 $M$ 的 $(u, v)$ 元素，$(X)_{ik}(Y)_{kj}$ 是 $(X)_{ik}$ 与 $(Y)_{kj}$ 的乘积，$\max_{1 \le k \le m} f(k)$ 与 $\min_{1 \le k \le m} f(k)$ 分别表示 $1 \le k \le m$ 的整数中 $f(k)$ 的最大值与最小值。

   (a) **A × B**，其中 A 是 `data4a.txt` 中的 $2 \times 4$ 矩阵，B 是 `data4b.txt` 中的 $4 \times 3$ 矩阵。

   (b) **C × D**，其中 C 是 `data4c.txt` 中的 $10^6 \times 10^6$ 矩阵，D 是 `data4d.txt` 中的 $10^6 \times 10^6$ 矩阵。C 与 D 的非零元素个数均不超过 $1000$。

   (c) **E × F**，其中 E 是 `data4e.txt` 中的 $10^6 \times 10^6$ 矩阵，F 是 `data4f.txt` 中的 $10^6 \times 10^6$ 矩阵。

(5). 若在一个 $r$ 行 $c$ 列的矩阵中选择一个高度为 $R$ 行、宽度为 $C$ 列的矩形区域，则共有 $(r - R + 1) \times (c - C + 1)$ 种选法。我们要统计这些区域中，元素和为 $0$ 的区域个数。例如矩阵

$$
\begin{pmatrix}
0 & -1 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
-4 & 8 & 2 & 0 & 0 & 0
\end{pmatrix}
$$

在选择 $2$ 行高、$3$ 列宽的矩形区域时共有 $8$ 种选法，其中下列 $4$ 个区域的元素和为 $0$：

$$
\begin{pmatrix}
0 & -1 & 1 \\
0 & 0 & 0
\end{pmatrix}
,\quad
\begin{pmatrix}
0 & 0 & 0 \\
-4 & 8 & 2
\end{pmatrix}
,\quad
\begin{pmatrix}
-1 & 1 & 0 \\
0 & 0 & 0
\end{pmatrix}
,\quad
\begin{pmatrix}
1 & 0 & 0 \\
8 & 2 & 0
\end{pmatrix}
$$

文件中保存了用**格式 3** 表示的矩阵数列。对于每个给定的矩阵 $r$、$R$ 与 $C$，请统计元素和为 $0$ 的 $R$ 行 $C$ 列矩形区域数量，并将该数量写在答题纸上。

   (a) `data5a.txt` 中的 $8 \times 6$ 矩阵，$R = 2$，$C = 3$。

   (b) `data5b.txt` 中的 $10^6 \times 10^6$ 矩阵，$R = C = 10$。

   (c) `data5c.txt` 中的 $10^6 \times 10^6$ 矩阵，$R = C = 100$。
