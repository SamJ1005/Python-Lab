import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {
    "x": [1, 2, 3, 4, 5],
    "y": [5, 7, 6, 8, 9]
}

df = pd.DataFrame(data)

# Line graph
df.plot(x="x", y="y", kind="line", title="Line Graph")
plt.show()

# Bar chart
df.plot(x="x", y="y", kind="bar", title="Bar Chart")
plt.show()

# Histogram
df["y"].plot(kind="hist", title="Histogram")
plt.show()

# Scatter plot
df.plot(x="x", y="y", kind="scatter", title="Scatter Plot")
plt.show()