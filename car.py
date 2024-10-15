from ucimlrepo import fetch_ucirepo, list_available_datasets
import pandas as pd
import matplotlib.pyplot as plt

# fetch dataset
car_evaluation = fetch_ucirepo(id=19)

# data (as pandas dataframes)
X = car_evaluation.data.features
y = car_evaluation.data.targets

# metadata
print(car_evaluation.metadata)

# variable information
print(car_evaluation.variables)

# Check which datasets can be imported
list_available_datasets()

# Import dataset
heart_disease = fetch_ucirepo(id=45)
# Alternatively: fetch_ucirepo(name='Heart Disease')

# Access data
X = heart_disease.data.features
y = heart_disease.data.targets

# Convert features and targets to pandas DataFrames
X_df = pd.DataFrame(X, columns=heart_disease.data.headers[:-1])  # Exclude target column from features
y_df = pd.DataFrame(y, columns=[heart_disease.data.headers[-1]])  # Target column

# Access metadata
print("UCI ID:", heart_disease.metadata.uci_id)
print("Number of instances:", heart_disease.metadata.num_instances)
print("Abstract:", heart_disease.metadata.abstract)

# Access variable info in tabular format
variables_df = pd.DataFrame(heart_disease.variables)
print("\nVariable info:")
print(variables_df)

# Basic statistics on features and targets
print("\nSummary statistics for features:")
print(X_df.describe())

print("\nSummary statistics for target(s):")
print(y_df.describe())


# Calculate summary statistics
summary_stats = X_df.describe()

# Visualize data using histograms
num_features = len(X_df.columns)
num_rows = (num_features + 1) // 2  # Calculate number of rows needed
plt.figure(figsize=(12, 6))
for i, column in enumerate(X_df.columns):
    plt.subplot(num_rows, 2, i+1)  # Adjusting the subplot grid based on the number of features
    plt.hist(X_df[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(column)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Visualize data using boxplots
plt.figure(figsize=(10, 6))
X_df.boxplot()
plt.title('Boxplot of Features')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()