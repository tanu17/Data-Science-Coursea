# Semi-parallel computations avoiding scale()
# Karolina Sikorska and Paul Eilers, 2012

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
means = s1/n
# outer refers to outer product of tensors
# outer(A,B) = A * transpose(B)
e = rep(1, n)
Sc = (S -outer(e, means))
b = crossprod(yc, Sc)/colSums(Sc ^ 2)
# Report time
t1 = proc.time()[1] - t0
msip = 1e-06 * n * m / t1
cat(sprintf("Speed: %2.1f Msips\n", msip))
