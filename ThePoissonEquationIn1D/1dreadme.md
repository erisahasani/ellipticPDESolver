First we start with the Poisson equation in one dimension, which is in fact an ODE. We considder the equation $-u''(x)=f(x)$ for $x \in (0,1)$ and $u(0)=u(1)=0$.
The goal here is to use the finite element method to solve the problem.

We will uniformly partition the interval $(0,1)$, each of size $\frac{1}{h}$. The idea for solving problem of this type is to transform the ODE/PDE problem to a matrix equation
of the form $A \xi=b$ where $\xi$ is the unkown and $A$ and $b$ can be determined from the problem.