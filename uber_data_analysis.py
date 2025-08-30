# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import cleaned data files
import os

# Create data frame
df = pd.read_csv('cleaned_uber_data.csv', index_col=0)
print(df)
print(df.info())

# Test correlation between driver ratings and booking value
print("Available columns:", df.columns.tolist())

#The Pearson correlation between driver ratings and booking value was -0.0002, close to 0, indicating no meaningful relationship.

# Scatter plot between driver ratings and booking value to see if correlation exists between the two

# Use the exact column names as printed above
correlation = df[df.columns[df.columns.str.lower().str.replace(' ', '_') == 'booking_value'][0]].corr(
	df[df.columns[df.columns.str.lower().str.replace(' ', '_') == 'driver_ratings'][0]]
)
print(f"Correlation between Driver Ratings and Booking Value: {correlation}")
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