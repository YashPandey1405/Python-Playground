# 🔥 Plotly - Interactive Data Visualization Library

## 📌 Introduction

Plotly is a **powerful Python library** for creating **interactive and dynamic visualizations**. It supports a wide range of charts and can be used for **web-based dashboards**.

📦 **Installation:**

```bash
pip install plotly
```

🛠 **Basic Usage:**

```python
import plotly.express as px

# Load example dataset
df = px.data.iris()

# Create a scatter plot
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
fig.show()
```

---

## 📈 Types of Graphs & Their Uses

### 1️⃣ **Scatter Plot** (`px.scatter()`)

✅ Best for **visualizing relationships between two variables**.

```python
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
fig.show()
```

### 2️⃣ **Bar Chart** (`px.bar()`)

✅ Used for **comparing categorical data**.

```python
fig = px.bar(df, x='species', y='sepal_width', color='species')
fig.show()
```

### 3️⃣ **Histogram** (`px.histogram()`)

✅ Used for **distribution analysis**.

```python
fig = px.histogram(df, x='sepal_length', nbins=20, color='species')
fig.show()
```

### 4️⃣ **Box Plot** (`px.box()`)

✅ Used for **outlier detection and distribution insights**.

```python
fig = px.box(df, x='species', y='sepal_width', color='species')
fig.show()
```

### 5️⃣ **Heatmap** (`go.Heatmap()`)

✅ Used for **visualizing correlations**.

```python
import plotly.graph_objects as go
import numpy as np

corr_matrix = df.corr(numeric_only=True)
fig = go.Figure(data=go.Heatmap(z=corr_matrix.values, x=corr_matrix.columns, y=corr_matrix.columns))
fig.show()
```

---

## 🔥 Most Commonly Used Methods

| Method           | Description                                 |
| ---------------- | ------------------------------------------- |
| `px.scatter()`   | Creates a **scatter plot**                  |
| `px.bar()`       | Creates a **bar chart**                     |
| `px.histogram()` | Creates a **histogram**                     |
| `px.box()`       | Creates a **box plot**                      |
| `px.pie()`       | Creates a **pie chart**                     |
| `px.line()`      | Creates a **line plot**                     |
| `px.violin()`    | Creates a **violin plot**                   |
| `px.area()`      | Creates an **area plot**                    |
| `px.treemap()`   | Creates a **tree map**                      |
| `go.Figure()`    | Used for **advanced custom visualizations** |

---

## 🎯 Summary

- **Plotly is used for interactive visualizations**.
- Great for **data science dashboards**.
- **Highly customizable** and supports **web embedding**.
- Supports both **Plotly Express (simple) and Graph Objects (advanced)**.

🚀 **Keep practicing! The more you visualize, the more you understand!**
