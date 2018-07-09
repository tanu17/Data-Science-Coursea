s <-  function(a){sample(1:365, a,replace = TRUE)}
v <- cumsum(c(31,28,31,30,31,30,31,31,30,31,30,31))

for (j in 1:40){
  t=1
  for(i in 1:100){
    s_new=s(j)
    h= hist(s_new,breaks=c(0,v),probability =TRUE)
    c=h$counts
    for (x in c){if (x==0){
      t=0
      break
    }
      }
  }
  if (t==1){
    print(j)
    break
  }
}
