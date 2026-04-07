# Probability Density Functions and Cumulative Density Functions: Using Calculus for Insights into Cryptocurrency Markets

## Mathematical and Financial Preliminaries

### Returns

Because the prices of financial assets are uncertain, we will model them as random variables, making their returns random variables, too. Let $P_0$ and $P_1$ be prices, with $P_1$ being observed after $P_0$ 

The _simple return_ over the time period is

$$
R_s = \frac{P_1-P_0}{P_0} = \frac{P_1}{P_0} - 1
$$

The _log return_ over the time period is

$$
R_l = \ln\left(\frac{P_1}{P_0}\right)
$$

The log return is primarily used due to having a property of additivity. That is, if you have three prices $P_2$, $P_1$, and $P_0$. 

$$
\ln\left(\frac{P_2}{P_0}\right) = \ln\left(\frac{P_1}{P_0}\right) + \ln\left(\frac{P_2}{P_1}\right)
$$

Another property worth considering is their symmetry compared to simple returns. To illustrate this:

$$
\ln(2) + \ln\left(\frac{1}{2}\right) = 0
$$

But with simple returns

$$
x \cdot (1+0.5) \cdot (1 - 0.5) = 0.75x \neq x
$$

Log returns are also a rewrite of $P(t)=P_0e^{kt}$ where $k$ is our log return, modeling growth as a continuous function, which is ideal for the integration techniques we will use when calculating probability.

### Probability Density Functions

To compute the probability of a random variable falling within an interval given its history, we'll use _probability density functions_.

$$
P(c \leq X \leq d) = \int_c^df(x)dx
$$

Given that f is continuous, nonnegative, and that $\int_{-\infty}^{\infty}f(x)dx = 1$

Our dataset naturally satisfies the continuity and non-negativity, but not the last constraint.


## Sources

Returns: https://gregorygundersen.com/blog/2022/02/06/log-returns/