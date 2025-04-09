import pandas as pd

df = pd.read_csv('dataset.csv')

k = len(df) // 5  # sample size = 5
start = 2  # starting index
indices = [start + i * k for i in range(5)]
sample = df.iloc[indices]

print("Systematic Sample:\n", sample)


#  Systematic Sampling

#  Description:
#   Select every k-th item from a sorted or indexed list after a random start.

#  Example:
#   Start at index 2, pick every 6th record.

#  Pros:
#    Simple and quick.
#    Useful for large datasets.

#  Cons:
#    Can introduce bias if there's a pattern in the data.
#    Not suitable for cyclical trends.

#  Use Case:
#   - When you want a fixed interval sample.
#   - Suitable when population is randomly ordered.

#  Code:
#   start = 2; k = N // sample_size
#   indices = [start + i*k for i in range(sample_size)]
#   df.iloc[indices]
