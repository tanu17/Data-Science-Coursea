# Semi-parallel computations using scale()
# Karolina Sikorska and Paul Eilers, 2012

# Simulate data
set.seed(2012)
n = 10000
m = 1000
S = matrix(2 * runif(n * m), n, m)
y = rnorm(n)

# Do the computations
t0 = proc.time()[1]

# drop of speed as scale is a slower
# function than explicitly calculating slope

yc = y - mean(y)
Sc = scale(S, scale = F)
S2 = colSums(Sc ^ 2 )
b = crossprod(yc, Sc)/S2

# Report time
t1 = proc.time()[1] - t0
msip = 1e-06 * n * m / t1
cat(sprintf("Speed: %2.1f Msips\n", msip))
