# Check the speed of semi-parallel approach
# for logistic regression with covariates
# Karolina Sikorska and Paul Eilers, 2013

set.seed(2013)
n = 10000
m = 1000
k = 1
S = matrix(2 * runif(n * m), n, m)
X0 = matrix(rnorm(n * k), n, k)
X = cbind(1, X0)
y = rbinom(n, size = 1, prob = c(0.5, 0.5))

# Do the computations
t0 = proc.time()[1]
 
mod0 = glm( y ~ X, family = binomial("logit"))
p = mod0$fitted
w = p * (1 - p)
z = log(p / (1 - p)) + (y - p) / (p * (1 - p))

# computing z*
xtw = t(X * w)
U1 = xtw %*% z
U2 = solve(xtw %*% X, U1)
ztr = z  - X %*% U2

# computing s*
U3 = xtw %*% S
U4 = solve(xtw %*% X, U3)
Str = S - X %*% U4

Str2 = colSums(w * Str^2)
b = crossprod(ztr * w, Str)/Str2
err = sqrt(1/ Str2)
pval = 2 * pnorm(-abs(b / err))

# Report time
t1 = proc.time()[1] - t0
msip = 1e-06 * n * m / t1
cat(sprintf("Speed: %2.1f Msips\n", msip))
###check results

t2 = proc.time()[1]
b1 = NULL
err1 = NULL
pval1 = NULL
for(i in 1:m){
  mod1 = glm(y ~ S[, i] + X0, family = binomial ("logit"))
  b1[i] = summary(mod1)$coef[2, 1]
  err1[i] = summary(mod1)$coef[2, 2]
  pval1[i] = summary(mod1)$coef[2, 4]
}

t3 = proc.time()[1] - t2
msip1 = 1e-06 * n * m / t3
cat(sprintf("Speed: %2.1f Msips\n", msip1))
