library(UsingR);data(galton);library(reshape);long<- melt(galton)
g <- ggplot(long,aes(x=value,fill=variable))
g <- g + geom_histogram(color="black", binwidth=1)
g <- g + facet_grid(. ~ variable)
g
