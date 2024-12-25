import pandas as pd

# Load the dataset
file_path = "studentdata.csv"  # Replace with your file path
df = pd.read_csv(file_path)

# Shuffle the rows
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save back to CSV
df_shuffled.to_csv("data.csv", index=False)
print("Rows have been shuffled and saved to 'shuffled_file.csv'.")