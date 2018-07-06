#options("max.print"=10000)

snp = read.table("C:/Users/User/Desktop/release/snpMat.txt",header = T)
# Map of every patient and their 10643 SNP values
# nrow(snp) = 245
# ncol(snp) = 10643
S = matrix(unlist(snp, use.names=F), ncol = length(snp), byrow=F)

covariate = read.csv("C:/Users/User/Desktop/release/covariates.csv", header=T, sep=",")
y = unlist(covariate[2], use.names=F) 
# y is a vector if disease yes/no\

rawX0 = covariate[3:5]   
# rawX0 is covariates age, height, weight and their values
normalize <- function(v){(v-min(v))/(max(v)-min(v))}
mean_replacer <- function(t) { ifelse(is.na(t), mean(t, na.rm=T) , t) }
# replaces mean where value is NA
X0_list = lapply(rawX0, mean_replacer) 
#apply function in argument on each element
X0 = (matrix(unlist(X0_list), ncol = length(X0_list), byrow=F))
X0 = normalize(X0)
# Add 1 to every row in covariate matrix
X = cbind(1, X0)

n = nrow(S)		#number of individuals
m = ncol(S) 	#number of SNPs
k = ncol(X0)	#number of covariates

t0 = proc.time()[1]		# start time for computation

model = glm( y ~ X-1, family = binomial("logit")) 
p = model$fitted
w = p * (1 - p)
z = log(p / (1 - p)) + (y - p) / (p * (1 - p))
xtw = t(X * w)
U1 = xtw %*% z
U2 = solve(xtw %*% X, U1)
ztr = z  - X %*% U2
U3 = xtw %*% S
U4 = solve(xtw %*% X, U3)
Str = S - X %*% U4
Str2 = colSums(w * Str^2)
b = crossprod(ztr * w, Str)/Str2
err = sqrt(1/ Str2)
pvalue_parallel = 2 * pnorm(-abs(b / err))
pval = as.numeric(as.matrix(pvalue_parallel))


# Regression without additional covaraites
#b1 = rep(0,m)
#err1 = rep(0,m)
#pval1 = rep(0,m)
#for(i in 1:m){
#  mod1 = glm(y ~ S[, i] + X0, family = binomial ("logit"))  
#  b1[i] = summary(mod1)$coef[2, 1]
#  err1[i] = summary(mod1)$coef[2, 2]
#  pval1[i] = summary(mod1)$coef[2, 4]
#}

t1 = proc.time()[1] - t0
msip = 1e-06 * n * m / t1
cat(sprintf("Speed: %2.1f Msips\n", msip))
