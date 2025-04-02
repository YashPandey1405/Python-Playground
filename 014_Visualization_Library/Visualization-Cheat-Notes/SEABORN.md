# 🎨 Seaborn - Statistical Data Visualization Library

## 📌 Introduction

Seaborn is a **Python data visualization library** based on Matplotlib. It provides a high-level interface for drawing **attractive and informative statistical graphics**. It works seamlessly with **Pandas DataFrames**.

📦 **Installation:**

```bash
pip install seaborn
```

🛠 **Basic Usage:**

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
df = sns.load_dataset('penguins')

# Create a scatter plot
sns.scatterplot(x='bill_length_mm', y='bill_depth_mm', hue='species', data=df)
plt.show()
```

---

## 📈 Types of Graphs & Their Uses

### 1️⃣ **Scatter Plot** (`sns.scatterplot()`)

✅ Best for **showing relationships between two numerical variables**.

```python
sns.scatterplot(x='bill_length_mm', y='bill_depth_mm', hue='species', data=df)
```

### 2️⃣ **Bar Plot** (`sns.barplot()`)

✅ Used for **comparing categorical data**.

```python
sns.barplot(x='species', y='body_mass_g', data=df)
```

### 3️⃣ **Histogram (Distribution Plot)** (`sns.histplot()`)

✅ Used for **understanding data distribution**.

```python
sns.histplot(df['bill_length_mm'], bins=30, kde=True)
```

### 4️⃣ **Box Plot** (`sns.boxplot()`)

✅ Used for **detecting outliers and understanding distributions**.

```python
sns.boxplot(x='species', y='bill_length_mm', data=df)
```

### 5️⃣ **Heatmap** (`sns.heatmap()`)

✅ Used for **showing correlation between numerical variables**.

```python
import numpy as np
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
```

---

## 🔥 Most Commonly Used Methods

| Method              | Description                                         |
| ------------------- | --------------------------------------------------- |
| `sns.scatterplot()` | Creates a **scatter plot**                          |
| `sns.barplot()`     | Creates a **bar plot**                              |
| `sns.histplot()`    | Creates a **histogram**                             |
| `sns.boxplot()`     | Creates a **box plot**                              |
| `sns.heatmap()`     | Creates a **heatmap**                               |
| `sns.pairplot()`    | Creates **pairwise scatter plots**                  |
| `sns.violinplot()`  | Creates a **violin plot** for distribution analysis |
| `sns.kdeplot()`     | Creates a **kernel density estimation (KDE) plot**  |
| `sns.regplot()`     | Creates a **regression plot**                       |
| `sns.countplot()`   | Plots **category frequency**                        |

---

## 🎯 Summary

- **Seaborn makes statistical visualization easier**.
- Works well with **Pandas DataFrames**.
- Built-in themes and color palettes for **better aesthetics**.
- Simplifies **complex visualizations like heatmaps and KDE plots**.

🚀 **Keep practicing! The more you visualize, the more you learn!**
