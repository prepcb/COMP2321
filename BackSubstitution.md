# Back substitution

Assume we have our Upper diagonal form so that

$$
\left(\begin{array}{ccc} 
1 & 2 & 3\\
0 & 3 & 4\\
0 & 0 & 5\\
\end{array}\right)
\left(\begin{array}{c} 
x_1 \\ 
x_2 \\
x_3
\end{array}\right)
=\left(\begin{array}{c}
6\\
7\\
8\\
\end{array}\right)
$$ 

or more generally

$$
\left(\begin{array}{ccc} 
A_{0,0}&A_{0,1}  & A_{0,2}\\
0 & A_{1,1} & A_{1,2}\\
0 & 0 & A_{2,2}\\
\end{array}\right)
\left(\begin{array}{c} 
x_0 \\ 
x_1 \\
x_2
\end{array}\right)
=\left(\begin{array}{c}
b_0\\
b_1\\
b_2\\
\end{array}\right)
$$

so, for example,

$A_{0,0}x_0+A_{0,1}x_1+A_{0,2}x_2=b_0$



