import matplotlib.pyplot as plt
from math import sin, pi
from numpy import random, linspace


def f(x):
    return sin(x)


a = 0
b = pi

actual_integral = 2

bign = 10000
dn = bign / 500

n = dn
N = []

error_shown = 0.0025

limit_integrals = []
limit_deltas = []

monte_carlo_integrals = []
monte_carlo_deltas = []

while n <= bign:
    # Integrate using limit definition of definite integral
    dx = (b - a) / n
    sum = 0
    i = a
    while i <= b:
        sum += f(i)
        i += dx
    limit_integral = sum * dx
    limit_integrals.append(limit_integral)
    limit_deltas.append(abs(actual_integral - limit_integral))

    # Integrate using Monte Carlo Method
    randoms = random.uniform(a, b, int(n))
    total = 0
    for random_number in randoms:
        total += f(random_number)
    average = total / n
    monte_carlo_integral = average * (b - a)
    monte_carlo_integrals.append(monte_carlo_integral)
    monte_carlo_deltas.append(abs(actual_integral - monte_carlo_integral))
    # Increment n by dn and repeat
    N.append(n)
    n += dn

fig = plt.figure()

fig.suptitle(
    fontsize=14, t='$\int_0^\pi \sin x \; dx$: Comparison of numerical methods')

integrals = fig.add_subplot(211)

integrals.set_title(
    'Partial sums')
integrals.set_ylim(actual_integral - error_shown,
                   actual_integral + error_shown)

integrals.set_xlabel('Number of iterations')
integrals.set_ylabel('Approximation of integral')

limit_integration = integrals.scatter(
    x=N,
    y=limit_integrals,
    label="Limit definition of definite integral"
)

monte_carlo_integration = integrals.scatter(
    x=N,
    y=monte_carlo_integrals,
    label="Monte Carlo integration"
)

errors = fig.add_subplot(212)
errors.set_title(
    'Difference between partial sums and actual integral')
errors.set_ylim(0, error_shown)
errors.set_xlabel('Number of iterations')
errors.set_ylabel('Error in approximation of integral')
limit_errors = errors.scatter(
    x=N,
    y=limit_deltas,
    label="Limit definition of definite integral"
)

monte_carlo_errors = errors.scatter(
    x=N,
    y=monte_carlo_deltas,
    label="Monte Carlo integration"
)
integrals.legend()
errors.legend()

plt.tight_layout()
fig.subplots_adjust(top=0.875)

plt.savefig('limit-definition-vs-monte-carlo-integration.png')

plt.show()
