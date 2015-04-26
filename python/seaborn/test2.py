import matplotlib
matplotlib.use("agg")
    
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(context="paper", font="monospace")
import seaborn as sns
#sns.set()

flights_long = sns.load_dataset("flights")
flights = flights_long.pivot("month", "year", "passengers")
flights = flights.reindex(flights_long.iloc[:12].month)

f, ax = plt.subplots()

sns.heatmap(flights, annot=True, fmt="d")

f.savefig("test2.pdf")

