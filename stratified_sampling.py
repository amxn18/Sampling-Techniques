import pandas as pd

# Load the synthetic dataset
df = pd.read_csv('dataset.csv')
# Stratified sampling based on 'Income' (make sure all groups have at least 2 entries)
sample = df.groupby('Income', group_keys=False).apply(lambda x: x.sample(min(len(x), 2), random_state=42))
print("Stratified Sample:\n", sample)


# 🎯 Stratified Sampling
 
#  Description:
#   Divide population into sub-groups (strata) and take random samples from each.

#  Example:
#   Group by 'Department' and take 2 samples from each.

#  Pros:
#    Ensures representation from all strata.
#    Reduces sampling bias.

#  Cons:
#    Requires prior knowledge of strata.
#    Complex if many strata.

#  Use Case:
#   - When population has distinct subgroups.
#   - Used in surveys, elections, etc.

#  Code:
#   df.groupby('Department').apply(lambda x: x.sample(2))
