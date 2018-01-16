import pandas
from ggplot import *

data = pandas.read_csv("data1_full.csv")

isCanada = data["country"] == "Canada"
isYear1982andLater = data["year"] >= 1982
sub_data = data[isCanada & isYear1982andLater]

plot = ggplot(aes(x='year', y ='lifeExp'), data=sub_data) + geom_point() + geom_line()
plot.save("graph.png")