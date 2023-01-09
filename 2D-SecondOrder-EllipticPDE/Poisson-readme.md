In this section we are looking at the problem $-\partial_{xx} u - \partial_{yy} u = f(x,y)$ on the domain $\Omega = (a,b)\times(c,d)$ where $a,b$ are user specified numbers. We assume that $u=g$ on the boundary where such data is specified by the user. 

For simplicity, as a first attempt we take $a=c=0$ and $b=d=1$, i.e we consider the problem on the unit square in $\mathbb{R}^2$.

We're looking at the problem: 
$$-\Delta u=f \quad \text{ in } \Omega$$
$$u = g \quad \text{ on } \partial \Omega$$ 



Since the problem is now two dimensional, the stiffness matrix will be even larger. In particular, it will be of magnitude $M^2 \times M^2$, where $M$ is the number of partitions in each direction specified by the user. To be consistent with the referenced book, we use the same node enumeration for our triagulated square (see Fig. 1.10 on p. 31 of the book), namely starting from the bottom left, moving to the right then up and repeat.

First, we save the function $g$ defined on the boundary as an $M+2$ by $M+2$ matrix, that has the boundary data on the first and last columns and rows of the matrix and is zero in the interior. For graphing purposes, this is intuitive since we can think of such matrix being the $z$ component of the 3D plot sitting above the $x,y$ grid. Once we get a numerical solution which will be of size $M \times M$, we will save that in the interior of the matrix $g$ described above. 

A finite element method is to find $u_h \in V_h$ such that 
$$\int_{\Omega} \nabla u_h \cdot \nabla \phi = \int_{\Omega} f \phi$$ 
for all $\phi \in V_h$ with $u_h(x) = g(x)$ for all $x \in \partial \Omega$, where $V_h$ consists of piecewise linear functions (for more details on the space $V_h$ see 1.2-1.4 of the referenced book). In this implementation, the way we deal with the boundary data $g$ is to simply to set our unknown $u_h$ to take such values on the boundary and eventually move them to the right hand side of the problem $A \xi =b $. For more details, see the implementation on the file FEM2DPoisson.py. We see that regardless of the values of $g$, the stifness matrix remains the same. 

#
## Future Goals
The next goal is to add also lower order terms to our equation, namely consider the more general problem
$$-\Delta u + b \cdot \nabla u + c u=f \quad \text{ in } \Omega$$
and $u = g$ on $\partial \Omega$. Where $b \in \mathbb{R}^2$ and $c \in \mathbb{R}$ constants specified by the user.