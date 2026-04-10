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

### Statistical Metrics

Let $x_n$ be a series of values, with $N$ as the number of values in the series.

The **mean average**, $\mu$ is defined as

$$
\mu=\frac{\sum_{n=1}^{N}{x_n}}{N}
$$

The **standard deviation** of the same given dataset, $\sigma$ is defined as

$$
\sigma=\sqrt{\frac{\sum_{n=1}^{N}{(x_n-\mu)^2}{}}{N}}
$$

### Probability Density Functions

To compute the probability of a random variable falling within an interval given its history, we'll use _probability density functions_.

$$
P(c \leq X \leq d) = \int_c^df(x)dx
$$

Given that f is continuous or has a finite number of discontinuities, nonnegative, and that $\int_{-\infty}^{\infty}f(x)dx = 1$.

### Normal Distribution

Our dataset naturally satisfies the continuity and non-negativity, but not the last constraint. Because of that, we'll use the **normal distribution**, a.k.a. a bell curve, as our Probability Density Function.

$$
f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}
$$

Using a normal distribution has the assumption that the mean of our dataset is its expected value with equal variance in the negative and positive directions.

## Sources

Returns: https://gregorygundersen.com/blog/2022/02/06/log-returns/