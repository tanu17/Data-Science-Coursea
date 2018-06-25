# Check the speed of lm() in loop
# Karolina Sikorska and Paul Eilers, 2012

# Simulate data
set.seed(2012)
n = 10000
m = 1000
# runif: random values from uniform distribution
S = matrix(2 * runif(n * m), n, m)
y = rnorm(n)
# rnorm: random values from normal distribution 

# Do the computations
t0 = proc.time()[1]
# t0 marks the staring time

beta = rep(0, m)
# initializing beta vector as (0,0,0,0,0...)

for(i in 1:m){
  # generating a linear mode based upon one SNPs having n states. Linear model provides intercept and slope
  mod = lm(y ~ S[,i])
  beta[i] = mod$coeff[2]
}

# Report time
t1 = proc.time()[1] - t0
msip = 1e-06 * n * m / t1
cat(sprintf("Speed: %2.1f Msips\n", msip))
beta
