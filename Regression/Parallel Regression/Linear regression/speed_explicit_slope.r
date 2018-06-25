# Computing slopes explicitly 
# Karolina Sikorska and Paul Eilers, 2012

# faster than lsfir model

# Simulate data
set.seed(2012)
n = 10000
m = 1000
S = matrix(2 * runif(n * m), n, m)
y = rnorm(n)

# Do the computations
t0 = proc.time()[1]

# explicit caculation of slope faster than scale()
beta = rep(0, m)
yc = y - mean(y)
for(i in 1:m){
  sc = S[, i] - mean(S[, i])
  beta[i] = sum(sc * yc)/(sum(sc ^ 2)) 
}
# Report time
t1 = proc.time()[1] - t0
msip = 1e-06 * n * m / t1
cat(sprintf("Speed: %2.1f Msips\n", msip))
