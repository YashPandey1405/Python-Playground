# Data Visualization Libraries

## Overview

Data visualization is a crucial aspect of data analysis. Python provides several powerful libraries for visualizing data, including **Matplotlib, Plotly, Seaborn,** and **Bokeh**. Each library has its own strengths and best use cases.

## 1. Matplotlib

### Description:

Matplotlib is a fundamental plotting library in Python that provides static, animated, and interactive visualizations. It is highly customizable and forms the foundation of many other visualization libraries.

### Installation:

```bash
pip install matplotlib
```

### Example:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()
```

### Key Features:

- Static and interactive plots.
- Customizable with extensive styling options.
- Supports bar charts, histograms, scatter plots, and more.

---

## 2. Plotly

### Description:

Plotly is an interactive visualization library that supports 3D plots, real-time streaming, and dashboards. It is great for web-based interactive charts.

### Installation:

```bash
pip install plotly
```

### Example:

```python
import plotly.express as px

data = px.data.iris()
fig = px.scatter(data, x='sepal_width', y='sepal_length', color='species')
fig.show()
```

### Key Features:

- Interactive and web-based plots.
- Supports 3D visualizations and animations.
- Works well with Dash for building dashboards.

---

## 3. Seaborn

### Description:

Seaborn is built on top of Matplotlib and provides a high-level API for drawing attractive and informative statistical graphics.

### Installation:

```bash
pip install seaborn
```

### Example:

```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
sns.boxplot(x='day', y='total_bill', data=df)
plt.show()
```

### Key Features:

- Beautiful and informative statistical plots.
- Built-in themes and color palettes.
- Supports heatmaps, violin plots, and pair plots.

---

## 4. Bokeh

### Description:

Bokeh is a powerful interactive visualization library designed for web-based applications. It supports real-time and large-scale data visualization.

### Installation:

```bash
pip install bokeh
```

### Example:

```python
from bokeh.plotting import figure, show
from bokeh.io import output_file

output_file("line_chart.html")
p = figure(title="Simple Line Chart", x_axis_label='X', y_axis_label='Y')
p.line([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], line_width=2)
show(p)
```

### Key Features:

- Interactive web-based visualizations.
- Supports real-time streaming data.
- Easily integrates with Flask and Django.

---

## Conclusion

Each of these libraries serves different use cases:

- **Matplotlib**: Best for static, highly customizable plots.
- **Plotly**: Great for interactive and web-based visualizations.
- **Seaborn**: Ideal for statistical and aesthetically pleasing plots.
- **Bokeh**: Suitable for interactive and real-time web applications.

Choose the one that fits your project needs!
