# 📊 Matplotlib - Python's Data Visualization Library

## 📌 Introduction

Matplotlib is a powerful **Python library for data visualization**. It allows users to create a wide range of **static, animated, and interactive plots** with ease. It is widely used in **data science, machine learning, and scientific computing**.

📦 **Installation:**

```bash
pip install matplotlib
```

🛠 **Basic Usage:**

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.show()
```

---

## 📈 Types of Graphs & Their Uses

### 1️⃣ **Line Plot** (`plt.plot()`)

✅ Best for **trend analysis** over time.

```python
plt.plot(x, y, marker='o', linestyle='--', color='b')
```

### 2️⃣ **Bar Plot** (`plt.bar()`)

✅ Used for **comparison of categories**.

```python
plt.bar(['A', 'B', 'C'], [30, 40, 50], color='g')
```

### 3️⃣ **Histogram** (`plt.hist()`)

✅ Used for **distribution analysis**.

```python
import numpy as np
data = np.random.randn(1000)
plt.hist(data, bins=30, color='purple')
```

### 4️⃣ **Scatter Plot** (`plt.scatter()`)

✅ Used for **showing relationships between two variables**.

```python
plt.scatter([1, 2, 3, 4], [10, 20, 25, 30], color='red')
```

### 5️⃣ **Pie Chart** (`plt.pie()`)

✅ Used for **percentage distribution**.

```python
plt.pie([40, 30, 20, 10], labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%')
```

---

## 🔥 Most Commonly Used Methods

| Method          | Description                   |
| --------------- | ----------------------------- |
| `plt.plot()`    | Creates a **line plot**       |
| `plt.bar()`     | Creates a **bar plot**        |
| `plt.hist()`    | Creates a **histogram**       |
| `plt.scatter()` | Creates a **scatter plot**    |
| `plt.pie()`     | Creates a **pie chart**       |
| `plt.xlabel()`  | Labels the **X-axis**         |
| `plt.ylabel()`  | Labels the **Y-axis**         |
| `plt.title()`   | Adds a **title** to the graph |
| `plt.legend()`  | Displays a **legend**         |
| `plt.grid()`    | Adds a **grid** to the plot   |
| `plt.show()`    | Displays the **plot**         |

---

## 🎯 Summary

- **Matplotlib is a versatile plotting library** for Python.
- Supports **multiple chart types** (line, bar, scatter, histogram, etc.).
- Highly **customizable** for labels, legends, and colors.
- Essential for **data visualization** in machine learning and data science.

🚀 **Keep practicing! The more you plot, the more you learn!**
