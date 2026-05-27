import pandas as pd

# Load dataset
data = pd.read_csv("../dataset/Bangalore_AQI_Dataset.csv")

# Remove missing values
data = data.dropna()

# Remove duplicate rows
data = data.drop_duplicates()

# Save cleaned dataset
data.to_csv("../dataset/preprocessed-aqi-dataset.csv", index=False)

print("Preprocessing completed.")
