import pandas as pd

# Load the data file
file_path = 'Walmart_Foot_Traffic_Summary_Random_June_2024.csv'
data = pd.read_csv(file_path)

# Sample data for CMA levels (assuming this is predefined)
cma_zipcode_mapping = {
    1: [75201, 75202],
    2: [75203, 75204],
    3: [75205, 75206],
    4: [75207, 75208],
    5: [75209, 75210]
}

# Grouping the data by ZIP_Code and summing the Foot_Traffic_Sum
traffic_by_zip = data.groupby('ZIP_Code')['Foot_Traffic_Sum'].sum().reset_index()

# Adding a CMA level to each ZIP code
def assign_cma(zipcode):
    for cma, zips in cma_zipcode_mapping.items():
        if zipcode in zips:
            return cma
    return None  # Return None if the ZIP code does not belong to any CMA

# Apply the CMA assignment function
traffic_by_zip['CMA'] = traffic_by_zip['ZIP_Code'].apply(assign_cma)

# Group by CMA and sum the foot traffic, then sort by foot traffic in descending order
traffic_by_cma = traffic_by_zip.groupby('CMA')['Foot_Traffic_Sum'].sum().reset_index()
traffic_by_cma_sorted = traffic_by_cma.sort_values(by='Foot_Traffic_Sum', ascending=False).reset_index(drop=True)

# Saving the sorted data to a CSV file
output_file_path = 'traffic_by_cma_sorted.csv'
traffic_by_cma_sorted.to_csv(output_file_path, index=False)

# Display the sorted data
print(traffic_by_cma_sorted)
