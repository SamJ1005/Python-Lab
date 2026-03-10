#Run this command, and install this package in your terminal to run this code
#pip3 install pandas matplotlib
import pandas as pd
import matplotlib.pyplot as plt

n = int(input("Enter number of values: "))

x = []
y = []

print("Enter X values:")
for i in range(n):
    x.append(int(input()))

print("Enter Y values:")
for i in range(n):
    y.append(int(input()))

# Create DataFrame
data = {"X": x, "Y": y}
df = pd.DataFrame(data)

# Line graph
df.plot(x="X", y="Y", kind="line", title="Line Graph")
plt.show()

# Bar chart
df.plot(x="X", y="Y", kind="bar", title="Bar Chart")
plt.show()

# Histogram
df["Y"].plot(kind="hist", title="Histogram")
plt.show()

# Scatter plot
df.plot(x="X", y="Y", kind="scatter", title="Scatter Plot")
plt.show()