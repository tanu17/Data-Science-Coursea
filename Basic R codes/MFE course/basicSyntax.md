# Data Types:
character:  "Shantanu", "A"
numeric: 4.52344332, pi , 3.52342432...
// R doesnt have long and various other distinction beause it doesnt have restriction on size
integer
logical: TRUE, FALSE
complex: 3+4i

# Assignment operation:   
  str1 <- "MFE"
  f <- 1:42
  num <- 2
  vetory <- (0,0,0)

    The operators <- and = assign into the environment in which they are evaluated. The operator <- can be used anywhere, 
    whereas the operator = is only allowed at the top level (e.g., in the complete expression typed at the command prompt) 
    or as one of the subexpressions in a braced list of expressions.


# Value check/test:
  is.numeric(str1)                    returns FALSE
  is.numeric(1:30)                    returns TRUE
  is.na(as.numeric("Shantanu")        returns TRUE
  
# Convertor:
  as.numeric("321")
  as.character(num)
  
# Date/Time:
  today <- Sys.Date()                 returns "2018-07-05"
  today + 3                           returns "2018-07-08"
  time <- Sys.time()
  class(time)         returns "POSIXct"  =>>POSIX is international standard for measuring time
  
