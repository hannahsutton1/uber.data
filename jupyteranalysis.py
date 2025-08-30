# %% [markdown]
# Here, we are going to analyze an Uber dataset to identify correlations between different variables. We will use Python with libraries such as pandas, matplotlib, and numpy for data manipulation and visualization.
# 

# %%
#Install libraries
%pip install pandas matplotlib numpy

# %%

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
# Import cleaned data files
import os

# %%
# Create data frame
df = pd.read_csv('cleaned_uber_data.csv', index_col=0)
print(df)
print(df.info())
print("Available columns:", df.columns.tolist())

# %% [markdown]
#  Test correlation between driver ratings and booking value:
# 

# %%


correlation = df[df.columns[df.columns.str.lower().str.replace(' ', '_') == 'booking_value'][0]].corr(
	df[df.columns[df.columns.str.lower().str.replace(' ', '_') == 'driver_ratings'][0]]
)

print(f"Correlation between Driver Ratings and Booking Value: {correlation}")

#The Pearson correlation between driver ratings and booking value was -0.0002, close to 0, indicating no meaningful relationship.


# %%
# Scatter plot between driver ratings and booking value to test again if correlation exists between the two

# Use the exact column names as printed above
plt.scatter(
    df[df.columns[df.columns.str.lower().str.replace(' ', '_') == 'driver_ratings'][0]],
    df[df.columns[df.columns.str.lower().str.replace(' ', '_') == 'booking_value'][0]],
    alpha=0.5
)
plt.title('Driver Ratings vs Booking Value')
plt.xlabel('Driver Ratings')
plt.ylabel('Booking Value')
plt.grid(True)
plt.show()
#The scatter plot shows no clear pattern, supporting the conclusion of no significant correlation between driver ratings and booking value. 

# %% [markdown]
# Let's see the overall correlations in the dataset.
# 

# %%

# Find the pearson correlations matrix for numeric columns only
corr = df.select_dtypes(include=[np.number]).corr(method='pearson')
corr

# %% [markdown]
# Since the dataset does not contain any strong correlations (all values are close to 0), we can conclude that there are no significant linear relationships between the numeric variables in this Uber dataset. There is no need for linear regression without vaues that strongly correlate.
# 

# %% [markdown]
# **Logistic testing and regression**

# %%



