# Programming

Let  
$$
R_0 : 0 \le x \le 10,\quad 0 \le y \le 10
$$

Consider all the integer-coordinate points $(x, y)$ contained in $R_0$.  
Define $A(d, R_0)$ as the number of points $(x, y)$ in $R_0$ that satisfy  
$$
x^2 + y^2 \le d^2.
$$  
Then $A(1, R_0)$ is 121 as shown in Figure 1.

![Figure 1](pic1.png)

## (1)
Write a program that computes $A(d, R_0)$ for a given floating-point number $d$.

## (2)
A point $(x, y)$ in the region $R_1$ satisfies the following inequality:
$$
R_1 : (x - 5)^2 + (y - 5)^2 \le 5^2.
$$

Write a program that computes this expression:
$$
\frac{A(d, R_1)}{A(d, R_0)} \times \frac{1}{4}
$$
for a given floating-point number $d$.

## (3)
The Koch snowflake (Figure 2) can be constructed by starting with an equilateral triangle, then recursively altering each line segment as follows:

1. divide the line segment into three segments of equal length  
2. draw an equilateral triangle that has the middle segment from step 1 as its base and points outward  
3. remove the line segment that is the base of the triangle from step 2  

(from Wikipedia, http://en.wikipedia.org/wiki/Koch_snowflake)

The region $K_n$ is the inside of the shape obtained from the triangle with vertices $(0,0)$, $(10,0)$, $(5,5\sqrt{3})$ and after $n$ iterations of the steps shown above.  
The boundary of the shape is included in $K_n$.

Write a program that prints the area of $K_2$.  
The answer must be a floating-point number.

![Figure 2](pic2.png)

## (4)
Write a program that computes the area of $K_n$ for a given positive integer $n$.  
The answer must be a floating-point number.

## (5)
Write a program that computes $A(d, K_2)$ for a given floating-point number $d$.

## (6)
Write a program that computes $A(d, K_n)$ for a given floating-point number $d$ and a positive integer $n$.
