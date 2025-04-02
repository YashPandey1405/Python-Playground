# 🎨 Bokeh - Interactive Visualization Library

## 📌 Introduction

Bokeh is a **Python library for creating interactive and web-ready visualizations**. It allows users to create **dynamic, scalable** plots that can be embedded in **web applications**.

📦 **Installation:**

```bash
pip install bokeh
```

🛠 **Basic Usage:**

```python
from bokeh.plotting import figure, show
from bokeh.io import output_file

# Create output file
output_file("bokeh_plot.html")

# Create figure
p = figure(title="Simple Line Plot", x_axis_label='X', y_axis_label='Y')
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)

# Show plot
show(p)
```

---

## 📈 Types of Graphs & Their Uses

### 1️⃣ **Line Plot** (`figure().line()`)

✅ Best for **trend visualization**.

```python
p.line(x=[1, 2, 3, 4], y=[10, 20, 25, 30], line_width=2, color='blue')
```

### 2️⃣ **Bar Chart** (`figure().vbar()`)

✅ Used for **category-wise comparisons**.

```python
p.vbar(x=['A', 'B', 'C'], top=[10, 20, 15], width=0.5, color='green')
```

### 3️⃣ **Scatter Plot** (`figure().circle()`)

✅ Used for **showing relationships between variables**.

```python
p.circle(x=[1, 2, 3, 4], y=[10, 20, 25, 30], size=10, color='red')
```

### 4️⃣ **Histogram** (`figure().quad()`)

✅ Used for **distribution analysis**.

```python
import numpy as np
hist, edges = np.histogram([1, 2, 2, 3, 3, 3, 4, 5, 6], bins=5)
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], color='purple')
```

### 5️⃣ **Heatmap** (`figure().rect()`)

✅ Used for **correlation visualization**.

```python
import pandas as pd
import seaborn as sns

# Sample correlation matrix
data = pd.DataFrame(np.random.rand(5,5), columns=list('ABCDE'))
corr = data.corr()

p.rect(x=corr.columns, y=corr.index, width=0.9, height=0.9, color='blue')
```

---

## 🔥 Most Commonly Used Methods

| Method          | Description                                     |
| --------------- | ----------------------------------------------- |
| `figure()`      | Creates a **new figure** for plotting           |
| `.line()`       | Creates a **line plot**                         |
| `.vbar()`       | Creates a **bar chart**                         |
| `.circle()`     | Creates a **scatter plot**                      |
| `.quad()`       | Creates a **histogram**                         |
| `.rect()`       | Creates a **heatmap** visualization             |
| `show()`        | Displays the **plot**                           |
| `output_file()` | Saves the plot as an **HTML file**              |
| `gridplot()`    | Arranges multiple plots in a **grid layout**    |
| `hovertool()`   | Adds **hover effects** for interactive elements |

---

## 🎯 Summary

- **Bokeh is used for interactive & web-based visualizations**.
- Supports **various charts**, including bar, scatter, line, and heatmaps.
- **Works well with Pandas & NumPy**.
- **Great for dashboards and real-time analytics**.

🚀 **Keep practicing! The more you visualize, the better your insights!**
