import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import csv
import random
import pandas as pd
df = pd.read_csv("MathScore.csv")
data = df["Math_score"].tolist()
fig = ff.create_distplot([data], ["Math Score"], show_hist = False)
fig.show()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("Population Mean:", mean)
print("Standard Deviation:", std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean 
mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("Sampling Distribution Mean:", mean)
fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0,20], mode = "lines", name = "mean"))
fig.show()