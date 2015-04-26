import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame(np.arange(10*10).reshape(10,10))
fig, ax = plt.subplots()
ax = sns.heatmap(data,linewidths=0.0)
fig.savefig('stackoverflow_lines.pdf')
