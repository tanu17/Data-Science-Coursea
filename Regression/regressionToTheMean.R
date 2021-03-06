library(UsingR)
data("father.son")

# normailizing the data
y <- (father.son$sheight- mean(father.son$sheight))/sd(father.son$sheight)
x <- (father.son$fheight- mean(father.son$fheight))/sd(father.son$fheight)
rho <- cor(x,y)

#plotting the data
library(ggplot2)
g = ggplot(data.frame(x=x,y=y),aes(x=x,y=y))
g = g+ geom_point(size=4, colour="black",alpha=0.2)
g = g+ geom_point(size=2, colour="salmon", alpha=0.2)
g = g+ xlim(-4,4) + ylim(-4,4)
g = g+ geom_abline(intercept=0, slope=1)
g = g+ geom_vline(xintercept = 0)
g = g+ geom_hline(yintercept = 0)
g = g+ geom_abline(intercept = 0, slope = rho, size=2)
g = g+ geom_abline(intercept = 0, slope = 1/rho, size=2)
g

# if there was no noise then corelation lines would have lied on either xAxis or yAxis 
# but as there is a dependence, there is some regression to the mean 
