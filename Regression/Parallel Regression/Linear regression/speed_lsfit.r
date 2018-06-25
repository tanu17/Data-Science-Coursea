# Check the speed of lsfit() in loop
# Karolina Sikorska and Paul Eilers, 2012

# Least Square is faster than linear modela

# Simulate data
# set.seed() is a PRG used to provide reproducable random data points
set.seed(2012)
n = 10000
m = 1000
S = matrix(2 * runif(n * m), n, m)
y = rnorm(n)

# Do the computations
t0 = proc.time()[1]

beta = rep(0, m)
for (i in 1:m) {
  # only change in code
  mod = lsfit(S[, i], y)
  beta[i] = mod$coeff[2]
}

# Report time
t1 = proc.time()[1] - t0
msip = 1e-06 * n * m / t1
cat(sprintf("Speed: %2.1f Msips\n", msip))
