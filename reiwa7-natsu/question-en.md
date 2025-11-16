# Programming

Answer the following questions by writing programs. The files needed for answering the questions are found in the USB flash drive. Store the programs in the USB flash drive before the examination ends.

## Problem

In this problem, we represent matrices with *r* rows and *c* columns in various formats. The entry in the *i*-th row and *j*-th column in a matrix is denoted as the *(i, j)* entry; the upper left entry of a matrix is the *(1, 1)* entry, and the entry to the right of it is the *(1, 2)* entry. We say that, for the *(i, j)* entry, the row number is *i* and the column number is *j*. Here, *1 ≤ i ≤ r* and *1 ≤ j ≤ c* hold. For any matrix given in this problem, all entries are integers between −9 and 9, inclusive, no row or column has more than 10 non-zero entries, and the total number of non-zero entries is at most 10⁶.

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
<span class="format-title">Format 1</span>

Format 1 is a number sequence that arranges the entries of a matrix in the row-major order. In the row-major order, the entries in upper rows precede those in lower rows, and entries to the left precede to the right in a row.
For example, the matrix

$$
\begin{pmatrix}
1 & -5 & 0 \\
0 & 3 & 0
\end{pmatrix}
$$

is represented as

$$
1, -5, 0, 0, 3, 0
$$

in Format 1.
</div>


When a number sequence is stored in a file, the concatenated string of elements separated by commas is stored. For example, the file storing a sequence of the four elements, 2,5,−3,0 contains the following string.


$$ 2,5,−3,0 $$


(1). Number sequences representing matrices in Format 1 are stored in files. For each of the following matrices, find the row such that the sum of the entries is the largest, and write down on the answer sheet its row number and the sum of its entries. If there are two or more such rows, answer about one of them.

   (a) The matrix with 6 rows and 4 columns stored in `data1a.txt`.
   
   (b) The matrix with 100 rows and 150 columns stored in `data1b.txt`.

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
<span class="format-title">Format 2</span>

Let $x_{ij}$ be the $(i, j)$ entry of a matrix. We define Format&nbsp;2 as the number sequence where the three integers $i$, $j$, and $x_{ij}$ for all $(i, j)$ such that $x_{ij} \ne 0$ are arranged in the row-major order.  
For example, the matrix

$$
\begin{pmatrix}
1 & -5 & 0 \\
0 & 3 & 0
\end{pmatrix}
$$

is represented as

$$
1, 1, 1, 1, 2, -5, 2, 2, 3
$$

in Format&nbsp;2.
</div>


(2). Number sequences representing matrices in Format 2 are stored in files. For each of the following matrices, find the row such that the sum of the entries is the largest, and write down on the answer sheet its row number and the sum of its entries. If there are two or more such rows, answer about one of them.

   (a) The matrix with 6 rows and 4 columns stored in `data2a.txt`.

   (b) The matrix with 100 rows and 150 columns stored in `data2b.txt`.

   (c) The matrix with 10⁶ rows and 10⁶ columns stored in `data2c.txt`.

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
<span class="format-title">Format 3</span>

Let $n_i$ be the number of consecutive zeros immediately preceding the $i$-th element  
in the sequence of entries of a matrix arranged in the row-major order.  
Let $x_i$ be the value of the $i$-th element.  
We define Format 3 as the number sequence where the two integers $n_i$ and $x_i$  
for all $i$ such that $x_i \ne 0$ are arranged in the ascending order of $i$.  
For example, the matrix

$$
\begin{pmatrix}
1 & -5 & 0 \\
0 & 3 & 0
\end{pmatrix}
$$

is represented as

$$
0, 1, 0, -5, 2, 3
$$

in Format 3.
</div>


(3). Number sequences representing matrices in Format 3 are stored in files. For each of the matrices obtained by **transposing** the following matrices, find the row such that the sum of the entries is the largest, and write down on the answer sheet its row number and the sum of its entries. If there are two or more such rows, answer about one of them.

   (a) The matrix with 4 rows and 6 columns stored in `data3a.txt`.

   (b) The matrix with 100 rows and 150 columns stored in `data3b.txt`.

   (c) The matrix with 10⁶ rows and 10⁶ columns stored in `data3c.txt`.

(4). Number sequences representing matrices in **Format 3** are stored in files.  
For each of the following matrices obtained by applying the **×** operation, find the row such that the sum of the entries is the largest, and write down on the answer sheet its row number and the sum of its entries.  
If there are two or more such rows, answer about one of them.

We define a binary operation **×** that produces a matrix with *r* rows and *n* columns from a matrix *X* with *r* rows and *m* columns and a matrix *Y* with *m* rows and *n* columns.  
The *(i, j)* entry of *X × Y* is defined as

$$
(X × Y)_{ij} = \max_{1 \le k \le m}((X)_{ik}(Y)_{kj}) + \min_{1 \le k \le m}((X)_{ik}(Y)_{kj})
$$

where $(M)_{uv}$ represents the (u, v) entry of matrix *M*, $(X)_{ik}(Y)_{kj}$ represents the product of $(X)_{ik}$ and $(Y)_{kj}$, and  
$\max_{1 \le k \le m} f(k)$ and $\min_{1 \le k \le m} f(k)$ represent the maximum and minimum values of *f(k)* for integers *k* $(1 \le k \le m)$, respectively.

   (a) **A × B**, where A is the matrix with 2 rows and 4 columns stored in `data4a.txt`, and B is the matrix with 4 rows and 3 columns stored in `data4b.txt`.

   (b) **C × D**, where C is the matrix with 10⁶ rows and 10⁶ columns stored in `data4c.txt`, and D is the matrix with 10⁶ rows and 10⁶ columns stored in `data4d.txt`. The number of non-zero entries in each of C and D does not exceed 1000.

   (c) **E × F**, where E is the matrix with 10⁶ rows and 10⁶ columns stored in `data4e.txt`, and F is the matrix with 10⁶ rows and 10⁶ columns stored in `data4f.txt`.


(5). When we choose a rectangular region of *R* rows high and *C* columns wide in a matrix with *r* rows and *c* columns,  
there are $(r - R + 1) × (c - C + 1)$ ways to choose.  
Let us count the number of regions among them where the sum of the entries is 0.  
For example, the matrix

$$
\begin{pmatrix}
0 & -1 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
-4 & 8 & 2 & 0 & 0 & 0
\end{pmatrix}
$$

has eight ways to select a rectangular region of 2 rows high and 3 columns wide,  
and the following four out of them are the regions where the sum of the entries is 0:

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

Number sequences representing matrices in **Format 3** are stored in files.  
For each matrix *r*, *R*, and *C* below, count the number of regions with *R* rows high and *C* columns wide where the sum of the entries is 0,  
and write that number down on the answer sheet.

   (a) The matrix with 8 rows and 6 columns stored in `data5a.txt`. R = 2, C = 3.  
   (b) The matrix with 10⁶ rows and 10⁶ columns stored in `data5b.txt`. R = C = 10.  
   (c) The matrix with 10⁶ rows and 10⁶ columns stored in `data5c.txt`. R = C = 100.
