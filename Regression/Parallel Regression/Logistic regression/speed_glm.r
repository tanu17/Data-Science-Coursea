# Check the speed of glm() in loop
# Karolina Sikorska and Paul Eilers, 2013

# Simulate data
set.seed(2013)
#seed used to reproduce the random results
n = 10000
m = 1000
S = matrix(2 * runif(n * m), n, m)
y = rbinom(n, size = 1, prob = c(0.5, 0.5))

# Do the computations
t0 = proc.time()[1]

beta = rep(0, m)
for(i in 1:m){
  mod = glm(y ~ S[,i], family = binomial ("logit"))
  beta[i] = mod$coeff[2]
}
# Report time
t1 = proc.time()[1] - t0
msip = 1e-06 * n * m / t1
cat(sprintf("Speed: %2.1f Msips\n", msip))
