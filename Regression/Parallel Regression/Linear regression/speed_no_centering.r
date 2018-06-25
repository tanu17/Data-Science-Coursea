0# Semi-parallel computations, no centering
# Karolina Sikorska and Paul Eilers, 2012

# fastest
# uses the fact that E((X-mu)^2) = E(X^2) - n*mu^2
# Simulate data
set.seed(2012)
n = 10000
m = 1000
S = matrix(2 * runif(n * m), n, m)
y = rnorm(n)

# Do the computations
t0 = proc.time()[1]

yc = y - mean(y)
s1 = colSums(S)
s2 = colSums(S ^ 2)
b = crossprod(yc, S)/(s2 - (s1 ^ 2) / n)

# Report time
t1 = proc.time()[1] - t0
msip = 1e-06 * n * m / t1
cat(sprintf("Speed: %2.1f Msips\n", msip))
