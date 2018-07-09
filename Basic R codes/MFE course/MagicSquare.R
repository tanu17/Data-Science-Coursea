while(TRUE){
  m<- matrix(sample(1:9), 3, 3)
  t=1
  for(i in 1:3){
    for(j in 1:3){
      if (sum(m[i,])!=sum(m[j,]) | sum(m[i,])!=sum(m[,j]) | sum(m[,i])!=sum(m[,j])){
        t=0
      }
    }
  }
  if (t==1){
    print(m)
    break
  }
}


#     [,1] [,2] [,3]
#[1,]    8    3    4
#[2,]    1    5    9
#[3,]    6    7    2
