import sys
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def plot_graph(csv_file):
    df = pd.read_csv(csv_file)
    df.head()
    title = df.loc[0, "Anime"]
    # decide what to plot here #Members #Timestamp #Score
    x = df[sys.argv[2]]    
    y = df[sys.argv[3]]
    fig, ax = plt.subplots(figsize=(10,7))
    ax.plot(x,y, marker = 'o')
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Score")
    ax.set_title(title) 
    plt.savefig(title + " - " + datetime.now().strftime('%Y-%m-%d') + '.png')

plot_graph(sys.argv[1])