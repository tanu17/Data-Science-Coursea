# 
#	If statement
#
aStr<- "R lang"

if (aStr == "pythonLang"){

}else if ( ) {

} else {

}

#
#	For Loop
# (includes both a and b in the values in a:b)
#
for ( i in 1:10){
  
}
# Example 1: i is not created in gobal envr but in a new environement, it can read from that envr but can't modify it unlike python, C etc.
for ( i in 1:10){
i<-i+1
print(i)
}
# Example 2:
c <- runif(10)
sum =0
for ( i in seq_along(v) ){
  print(i)}
# Example 3:
for ( i in v){
  print(i)}
# Example 4: Matrix multiplication using for loop
m= 2
n= 3
p =3

m1 <- matrix(runif(m*n), m, n)
m2 <- matrix(runif(n*p), n, p)
m3 <- matrix(0, m, p)

for(i in 1:m){
  for(j in 1:p){
    m3[i,j]<- sum(m1[i,]*m2[,j])
  }
}
print(all(as.vector(m1%*%m2 == m3)))  # TEST1
print(all(abs(as.vector(m1%*%m2 - m3))< 1e-8))	# TEST2
