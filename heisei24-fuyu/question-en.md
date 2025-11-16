# University of Tokyo, Creative Informatics, 2012-winter coding test

## Programming

Make a program that shows a graph of N data elements and that calculates Least Squares approximation.
A data tuple is represented as $(x, y)$, $x, y$ are integers where $0 ≤ x < 30$, $0 ≤ y < 30$.
The USB memory distributed contains two sets of data each with 30 data tuples where the data format is as follows:

```
(2, 10)
(23, 1)
...
(15, 23)
```

(1) The USB memory contains data1.txt that has 30 data tuples.
Make a program that reads all the data of data1.txt and outputs the (x, y) tuple that has the maximum y value.

(2) Draw all the data in data1.txt in the USB memory in a graph (c.f. Figure 1).

(3) Make a program that shows a graph of a linear equation
  y = ax + b where 0 ≤ x < 30, 0 ≤ y < 30, using ASCII characters.
Then show a graph of a=0.5, b=10 as a test case.
Characters for drawing the graph are arbitrarily selected (c.f. Figure 2).

(4) Obtain a linear equation y = ax + b that is the Least Squares approximation of data in data1.txt in the USB memory.
Then draw the obtained equation on the graph (c.f. Figure 3).

Here, coefficients a, b of the linear equation are computed as

$$
a = \frac{N\sum x_k y_k - \sum x_k \sum y_k}{N\sum x_k^2 - (\sum x_k)^2}
$$

$$
b = \frac{\sum x_k^2 \sum y_k - \sum x_k y_k \sum x_k}{N\sum x_k^2 - (\sum x_k)^2}
$$

from input (xₖ, yₖ), where k = 0, …, N−1.

---

(5) Make a program that computes two sets of coefficients $a_1, b_1, a_2, b_2$, and $x_m$ where two linear equations
$$y = a_1x + b_1, 0 ≤ x < x_m$$
 and $$y = a_2x + b_2, x_m ≤ x < 30$$
give the minimum sum of square errors of data in data2.txt file in the USB memory.
Note that two linear equations must be connected at $x_m$.
Here, sum of square errors of data is defined as:

$$
F(x) =
\begin{cases}
a₁x + b₁, & 0 ≤ x < xₘ \\
a₂x + b₂, & xₘ ≤ x < 30
\end{cases}
$$

and

$$
a₁xₘ + b₁ = a₂xₘ + b₂
$$

$$
E = \sum_{k=0}^{N-1} (y_k - F(x_k))^2
$$


where $F(x_k)$ denotes the $y$ value of the approximated linear equation at $x_k$.

---

**Figure 1.** An example of a graph of data from a file  
![Graph of data points](./pic1.png)

---

**Figure 2.** An example of a graph of a linear equation  
  y = ax + b, a = 0.8, b = 2.0  
![Graph of linear equation](./pic2.png)

---

**Figure 3.** An example of a Least Squares fit  
![Graph of Least Squares fit](./pic3.png)

---
