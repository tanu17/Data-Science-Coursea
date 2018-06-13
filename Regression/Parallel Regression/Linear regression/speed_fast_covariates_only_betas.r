# Semi-parallel computations for model with covariates
# (only estimates)
# Karolina Sikorska and Paul Eilers, 2012

# Simulate data
set.seed(2012)
n = 10000
m = 1000
k = 15
S = matrix(2*runif(n*m), n, m)
y = rnorm(n)
X0 = matrix(rnorm(n*k), n, k)
X = cbind(1, X0)

# Do the computations
t0 = proc.time()[1]

U1 = crossprod(X, y)
U2 = solve(crossprod(X), U1)
ytr = y - X %*% U2
U3 = crossprod(X, S)
U4 = solve(crossprod(X), U3)
Str = S - X %*% U4
b = as.vector(crossprod(ytr, Str) / colSums(Str ^ 2))

# Report time
t1 = proc.time()[1] - t0
msip = 1e-06 * n * m / t1
cat(sprintf("Speed: %2.1f Msips\n", msip))

