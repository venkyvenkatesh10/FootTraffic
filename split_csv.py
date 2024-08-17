import pandas as pd

# Load the large CSV file
df = pd.read_csv("Walmart_Foot_Traffic_June_2024_Large.csv")

# Calculate the chunk size to create approximately 5 files
total_rows = len(df)
chunk_size = total_rows // 5  # Divide the total number of rows by 5

# Split into 5 chunks
for i, chunk in enumerate(range(0, total_rows, chunk_size)):
    df_chunk = df.iloc[chunk:chunk + chunk_size]
    df_chunk.to_csv(f"Walmart_Foot_Traffic_June_2024_Part{i+1}.csv", index=False)

print("CSV file has been split into 5 parts successfully.")
