# 📊 Sampling Techniques in Statistics

This repository demonstrates four fundamental **sampling techniques** using a synthetic dataset of 100 individuals.

## 📁 Dataset Columns

- `ID`: Unique identifier for each individual  
- `Income`: Monthly income bracket (Low, Medium, High)  
- `Region`: Region where the individual resides (North, South, East, West)  
- `Age`: Age of the individual  
- `Gender`: Male or Female  

---

## ✅ Sampling Techniques Implemented

### 1️⃣ Simple Random Sampling
**File**: `simple_random_sampling.py`

- Randomly selects `n` individuals from the dataset using `sample()`.
  
**Pros**:
- Easy and unbiased  
- No need for domain knowledge

**Cons**:
- May not represent sub-groups (e.g., all income levels or regions) proportionally  

---

### 2️⃣ Systematic Sampling
**File**: `systematic_sampling.py`

- Selects every `k-th` element from the dataset after a random start.

**Pros**:
- Simple and fast to implement  
- Suitable for large datasets

**Cons**:
- Can introduce bias if there's a hidden pattern in the data  

---

### 3️⃣ Stratified Sampling
**File**: `stratified_sampling.py`

- Divides the dataset into strata based on `Income`, then samples equally from each group.

**Pros**:
- Ensures proper representation of all subgroups  
- Produces more precise estimates with smaller samples

**Cons**:
- Requires well-defined and non-overlapping strata  
- Needs sufficient data per stratum  

---

### 4️⃣ Cluster Sampling
**File**: `cluster_sampling.py`

- Groups data into clusters based on `Region`, randomly selects clusters, and includes all individuals from chosen clusters.

**Pros**:
- Efficient when data is naturally divided (e.g., by geography)  
- Reduces cost when surveying by groups

**Cons**:
- Can lead to higher variability  
- Not ideal if clusters are not diverse internally  

---

## 📂 Folder Structure

