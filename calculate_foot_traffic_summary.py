import pandas as pd
import random

# Path to the large dataset generated for June 2024
input_file = r"C:\Users\venka\Desktop\FootTraffic\Walmart_Foot_Traffic_June_2024_Large.csv"

# Load the data into a DataFrame
df = pd.read_csv(input_file)

# Group by ZIP_Code, Chain_Name, POI_Name, and POI_Chain_ID (but don't calculate actual sums)
foot_traffic_summary = df.groupby(['ZIP_Code', 'Chain_Name', 'POI_Name', 'POI_Chain_ID']).size().reset_index(name='Foot_Traffic_Sum')

# Replace the 'Foot_Traffic_Sum' with random values centered around 15,000
foot_traffic_summary['Foot_Traffic_Sum'] = foot_traffic_summary['Foot_Traffic_Sum'].apply(lambda x: random.randint(14000, 16000))

# Save the summary to a new CSV file
output_file = r"C:\Users\venka\Desktop\FootTraffic\Walmart_Foot_Traffic_Summary_Random_June_2024.csv"
foot_traffic_summary.to_csv(output_file, index=False)

# Display the first few rows to verify
print(foot_traffic_summary.head(20))
