In this project we aim to develop a PDE solver, in particular an elliptic PDE solver. We are seaking approximate solutions to problem of the type:
$$Lu=f \quad \text{ in } \Omega$$
$$u = g \quad \text{ on } \partial \Omega$$ 

where $L$ denotes an elliptic operator (we will elaborate below), $\Omega$ is some specified domain, $f$ is some known function given by the user and $g$ contains the specified data for the problem on the boundary of $\Omega$, which we denote by $\partial \Omega$. In other words, $u$ is our unknown function, that we wish to solve for.

In particular for this project, we allow the operator $L$ to will be of the following standard nondivergence form: 
$$Lu = - \sum_{i,j = 1}^n a^{ij}(x)u_{x_i x_j} + \sum_i b^i(x)u_{x_i}+c(x)u$$

So the end goal of this project will be to numerically solve general elliptic problems where $Lu$ is defined as above. As a first step we consider the case where $Lu = -\Delta u$ starting from dimension $2$ and going up over time.

In this project, we will implement the finite element method for solving partial differential equations. In particular, we will use the following book as a reference on the mathematics of the method: *Numerical Solution of Partial Differential Equations by the Finite Element Method* by Claes Johnson.
