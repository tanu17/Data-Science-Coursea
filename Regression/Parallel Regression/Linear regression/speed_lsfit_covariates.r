# Checking speed of lsfit in loop, model with covariates
# Karolina Sikorska and Paul Eilers, 2012

# Simulate data
set.seed(2012)
n = 10000
m = 1000
k = 10
S = matrix(2*runif(n*m), n, m)
y = rnorm(n)
X0 = matrix(rnorm(n*k), n, k)
X = cbind(1, X0)

# Do the computations
t0 = proc.time()[1]

b = rep(0,m)
for(i in 1:m){
  mod = lsfit(cbind(S[,i], X), y, intercept = F)
  b[i] = mod$coeff[1]
}
# Report time
t1 = proc.time()[1] - t0
msip = 1e-06 * n * m / t1
cat(sprintf("Speed: %2.1f Msips\n", msip))
