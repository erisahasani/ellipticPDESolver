In this section we are looking at the problem $-\partial_{xx} u - \partial_{yy} u = f(x,y)$ on the domain $\Omega = (a,b)\times(c,d)$ where $a,b$ are user specified numbers. We assume that $u=g$ on the boundary where such data is specified by the user. 

For simplicity, as a first attempt we take $a=c=0$ and $b=d=1$, i.e we consider the problem on the unit square in $\mathbb{R}^2$.

We separate the following two cases: 
$$-\Delta u=f \quad \text{ in } \Omega$$
$$u = 0 \quad \text{ on } \partial \Omega$$ 
and
$$-\Delta u=0 \quad \text{ in } \Omega$$
$$u = g \quad \text{ on } \partial \Omega$$ 

The first case is under the python file FEM2Poisson.py and the second is under the file FEM2DLaplacian.py.

**Some Details on the FEM2Poisson.py File**

Since the problem is now two dimensional, the stifness matrix will be even larger. In particular, it will be of magnitude $M^2 \times M^2$, where $M$ is the number of partitions in each direction specified by the user. To be consistent with the referenced book, we use the same node ennumeration for our triagulated square (see Fig. 1.10 on p. 31 of the book).