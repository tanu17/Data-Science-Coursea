# Data Types:

character:  "Shantanu", "A" <br />
numeric: 4.52344332, pi , 3.52342432...<br />
    R doesnt have long and various other distinction beause it doesnt have restriction on size integer<br />
logical: TRUE, FALSE<br />
complex: 3+4i<br /><br />

# Assignment operation:   
  str1 <- "MFE"<br />
  f <- 1:42<br />
  num <- 2<br />
  vetory <- (0,0,0)<br />

    The operators <- and = assign into the environment in which they are evaluated.
    The operator <- can be used anywhere, whereas the operator = is only allowed at
    the top level (e.g., in the complete expression typed at the command prompt) 
    or as one of the subexpressions in a braced list of expressions.


# Value check/test:
  is.numeric(str1)                    returns FALSE<br />
  is.numeric(1:30)                    returns TRUE<br />
  is.na(as.numeric("Shantanu")        returns TRUE<br />
  
# Convertor:
  as.numeric("321")<br />
  as.character(num)<br />
  
# Date/Time:
  today <- Sys.Date()                 returns "2018-07-05"<br />
  today + 3                           returns "2018-07-08"<br />
  time <- Sys.time()<br />
  class(time)         returns "POSIXct"  =>>POSIX is international standard for measuring time<br />
  
/# : comments<br />
== : comparison<br />

# Sequence <br />
   rep(0,10) 
   seq<- 1:21 <br/>
   replicate(10,0)<br />
   vector(mode="numeric", length="10<br />
   c( 12, someVector,1) <br/>
   rep(10, rnorm(1))<br />
   
# Vector
  1:10 + 1                             returns 2 3 4 5 6 7 8 9 11<br />
  1:10 + 1:3                           returns 2 4 6 5 7 9 10 12 11 //shorter added again and again<br />
  
# Series/ Sequence
  seq(1,10, by= 3)                      returns 1 4 7 10<br />
  
# Matrix
        Matrix and Vectors are homegenous, contains only one data type
   m <- matrix(nrow=2, ncol=3) <br/>
   m[1,3] <- 10<br />
   matrix(2,3,3)<br />
   matrix("f",2,2)<br />
   diag(1,4,4)                              returns identity 4x4 matrix<br />
   dim(m)                                   returns dimension<br />
   cbind(diag(1,3,3), matrix(0,3,3))        returns matrix appended on right or columns<br />
   rbind(diag(1,3,3), matrix(0,3,3))        returns matrix appended on bottom or rows<br />
   
   paste0(c("A","G","T","C"),2))<br/>
   paste(1,2,"f")<br/>
   paste0(1,2,"f)<br/>
   <br/>
   // genrate card sequence<br/>
   cards<- paste0(c("Spade","Clubs,"Hearts","Diamonds"), sort(rep(1:13, 4))), "J", "j"))<br/>
   length(cards)<br/>
   
# List
   x <- list( "shan", 3, FALSE, 3+8i, 4)
   x[[1]]<br/>
<br/>
   lst <- list(a=1, b=2, c=4)             // NAMED LIST
   lst[[2]]<br/>
   lst[["a"]]<br/>
   lst$a<br/>
   x[[1]]<br/>
   
   
