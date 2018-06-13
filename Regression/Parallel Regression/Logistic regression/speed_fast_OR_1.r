# Check the speed of semi-parallel approach
# for logistic regression when OR = 1
# Karolina Sikorska and Paul Eilers, 2013

# Simulate data
set.seed(2013)
n = 10000
m = 1000
S = matrix(2 * runif(n * m), n, m)
y = rbinom(n, size = 1, prob = c(0.5, 0.5))

t0 = proc.time()[1]
### fit model without SNP and set weights
mod0 = glm(y ~ 1, family = binomial ("logit"))
p = mod0$fitted
w = p * (1 - p)
### Do the computations
z = log(p / (1 - p)) + (y - p) / (p * (1 - p))
zc = z - mean(z)
s1 = colSums(S)
s2 = colSums(S^2)
den1 = s2 - s1^2/n
b = crossprod(zc, S)/ den1
err = sqrt(1/(w[1] * den1))
pval = 2 * pnorm(-abs(b/err))
# Report time
t1 = proc.time()[1] - t0
msip = 1e-06 * n * m / t1
cat(sprintf("Speed: %2.1f Msips\n", msip))


### check the results
b1 = rep(0, m)
err1 = rep(0, m)
pval1 = rep(0, m)
for(i in 1:m){
  mod = glm(y ~ S[,i], family = binomial ("logit"))
  b1[i] = mod$coeff[2]
  err1[i] = summary(mod)$coef[2, 2]
  pval1[i] = summary(mod)$coef[2, 4]
}
