?plot
x <- rnorm(1000)
y <- rnorm(1000)

# for line graph and pint graph
plot(X,Y, type="p")
plot(X,Y, type="l")
hist(distribution)

# different "dots"
plot(X,Y, pch=1/2/3/4)

# overlap two data sets in same graph and then plot something
par(new=T)
plot(distri2)

# restricting data window
par(mfcol= c(2,1))
par(mfrow= c(4,5))
