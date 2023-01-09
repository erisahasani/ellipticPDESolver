Our next goal is to move on to the more general case of the Poisson equation in dimension two, where we now also add some lower order terms. Namely, we consider the following problem

$$-\Delta u + b \cdot \nabla u + cu=f \quad \text{ in } \Omega$$
and $u=g$ on $\partial \Omega$. Here, $b \in \mathbb{R}^2$ and $c \in \mathbb{R}$. 

We are still using the finite element method to get a numerical solution, however, we need to derive a new stiffness matrix that incorperates the new components of the equation. 

This file corresponds to the FEM2DElliptic.py