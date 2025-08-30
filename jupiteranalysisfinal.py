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
#Install sklearn for logistic regression
%pip install scikit-learn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, RocCurveDisplay


# %% [markdown]
# Encode Categorical Features for Logistic Regression
# 

# %%
#  Load dataset
df = pd.read_csv("cleaned_uber_data.csv")

# we want to predict whether drving a sedan leads to high booking value rides (> $508.29 (the avg))
df['high_value'] = (df['Booking_Value'] > 508.29).astype(int)
# Convert 'Vehicle_Type' to a binary variable: 1 if 'Sedan', else 0
df['is_sedan'] = (df['Vehicle_Type'] == 'Sedan').astype(int)    

X = df[['is_sedan', 'Booking_Value']]
y = df['high_value']

# %% [markdown]
# Train/Test Split

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# %% [markdown]
# Fit Logistic Regression

# %%
# Check class distribution in y_train
print("y_train value counts:\n", y_train.value_counts())

# If only one class is present, model fitting will fail.
if y_train.nunique() < 2:
	raise ValueError("y_train contains only one class. Please check your data split or threshold for 'high_value'.")
else:
	model = LogisticRegression(max_iter=1000)
	model.fit(X_train, y_train)

# %% [markdown]
# Evaluate Performance

# %%
y_pred = model.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ROC Curve
RocCurveDisplay.from_estimator(model, X_test, y_test)
plt.show()

# %% [markdown]
# Print coefficients to see which values contribute to high/low rating

# %%
coeffs = pd.Series(model.coef_[0], index=X.columns)
print(coeffs.sort_values())
#!/usr/bin/env python3  

# %% [markdown]
# Check class balance and cross-validate

# %%
df['is_sedan'].value_counts()
df.groupby('is_sedan')['high_value'].mean()



