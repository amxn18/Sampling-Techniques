import pandas as pd
import random

df = pd.read_csv('dataset.csv')

# Simple Random Sampling (n=5)
sample = df.sample(n=5, random_state=42)

print("Simple Random Sample:\n", sample)


#  Simple Random Sampling

#  Description:
#   Each individual in the population has an equal chance of being selected.

#  Example:
#   Choose 5 employees randomly from the dataset.

#  Pros:
#    Easy to understand and implement.
#    Minimizes selection bias.

#  Cons:
#    May not represent sub-groups well.
#    Requires complete list of population.

#  Use Case:
#   - When population is homogeneous.
#   - When you want unbiased general sampling.

#  Code:
#   df.sample(n=5, random_state=42)
