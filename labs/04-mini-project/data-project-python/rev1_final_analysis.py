import pandas
from ggplot import *

data = pandas.read_csv("data1_full.csv")

isCanada = data["country"] == "Canada"
sub_data = data[isCanada]

plot = ggplot(aes(x='year', y ='lifeExp'), data=sub_data) + geom_point() + geom_line()
plot.save("graph.png")