# Back substitution

$A_{0,0}x_0+A_{0,1}x_1...A_{0,2}x_2=A_{0,3}b_0$

$A_{i,i}x_i+A_{i,i+1}x_{i+1}...A_{i,n-1}x_{n-1}=A_{i,n}b_i$

$\sum_{j=i}^nA_{i,j}x_j=A_{i,n}b_i$

$A_{i,i}x_i=-\sum_{j=i+1}^nA_{i,j}x_j+A_{i,n}b_i$

so that

$x_i=(-\sum_{j=i+1}^nA_{i,j}x_j+A_{i,n}b_i)/A_{i,i}$

but $b_i$ is stored as $A_{i,n}$ so our formula is

$x_i=(-\sum_{j=i+1}^nA_{i,j}x_j+A_{i,n}A_{i,n})/A_{i,i}$
