#Import pandas and numpy libraries
import pandas as pd
import numpy as np
#Load the data set
try: 
    df = pd.read_csv('ncr_ride_bookings.csv')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: The file 'ncr_ride_bookings.csv' was not found.")
    exit ()
# Data Cleaning 
# Display first few rows and information about the data
print("\nInitial data info:")
print(df.head())
print(df.info())

# Fill missing values with mean (replacing nulls with the average of the existing values preserves the overall mean of the column, useful for analyses where the average value is a key metric)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# --- Data Analysis ---
# Generate descriptive statistics
print("\nDescriptive statistics:")
print(df.describe())

# Perform a simple analysis (mean of a specific column)
# Replace 'column_name' with the actual column analyzed
try:
    mean_value = df['column_name'].mean()
    print(f"\nThe mean of 'column_name' is: {mean_value}")
except KeyError:
    print("\nError: 'column_name' not found in the DataFrame.")

# Save cleaned data to a new CSV file
df.to_csv('cleaned_uber_data.csv', index=False)
print("\nCleaned data saved to 'cleaned_uber_data.csv'.")

