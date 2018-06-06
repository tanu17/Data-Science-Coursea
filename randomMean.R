randomMean <- function(){
  x <- rnorm(100)
  mean(x)
}

secondF <- function(x){
  x+ rnorm(length(x))
}