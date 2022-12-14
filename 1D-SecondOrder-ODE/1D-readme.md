First we start with the Poisson equation in one dimension, which it is in fact an ODE. We considder the equation $-u''(x)=f(x)$ for $x \in (0,1)$ and $u(0)=u(1)=0$.
The goal here is to use the finite element method to solve the problem.

We will uniformly partition the interval $(0,1)$, each of size $h :=\frac{1}{M+1}$, where $M$ is the number of partitions specified by the user. The idea for solving problem of this type is to transform the ODE/PDE problem to a matrix equation of the form $A \xi=b$ where $\xi$ is the unkown and $A$ and $b$ can be determined from the problem. To see the mathematical details of how to set up the variational problem and obtain the matrix $A$, see chapters $1.1-1.2$ of the reference book for this project. 

Once that case is covered, we next move to the more generalized case of the form $-u''(x)+bu'(x) + cu(x)=f(x)$ while still maintaining zero boundary conditions and $b,c \in \mathbb{R}$ are known parameters specified by the user. Notice that for $b=c=0$, we recover the standard Poission equation in dimension one. This now is a second order non-homogeneuous ODE with constant coefficients. The file *FEM1D.py* is now updated to handle this more general problem.

<!-- Note to self: in the future write up the details on how to get the stiffness matrix for the more generalized problem that's not covered in the book -->