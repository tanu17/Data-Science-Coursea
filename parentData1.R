library(ggplot2)
library(UsingR)
data(galton)
ggplot(galton, aes(x=parent, y=child))+ geom_point()

