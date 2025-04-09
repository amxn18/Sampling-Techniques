import pandas as pd
import numpy as np

df = pd.read_csv('dataset.csv')

# Divide data into 5 clusters based on ID
df['cluster'] = df['ID'] % 5

# Randomly choose 1 cluster
chosen_cluster = np.random.choice(df['cluster'].unique())
sample = df[df['cluster'] == chosen_cluster]

print(f"Cluster Sample (Cluster {chosen_cluster}):\n", sample)


# 🎯 Cluster Sampling

#  Description:
#   Divide the population into clusters and randomly select entire clusters.

#  Example:
#   Group employees by ID % 5 → randomly choose one group.

#  Pros:
#    Cost-effective and fast.
#    Useful for geographically spread populations.

#  Cons:
#   High sampling error risk.
#    May not be representative if cluster is biased.

#  Use Case:
#   - When full population list is unavailable.
#   - When surveying regions/campuses/cities.

#  Code:
#   df['cluster'] = df['ID'] % 5
#   df[df['cluster'] == random.choice(unique_clusters)]
