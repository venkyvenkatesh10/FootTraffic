import random
import pandas as pd
import os

# List of Dallas ZIP codes
zip_codes = [
    "75201", "75202", "75203", "75204", "75205", "75206", "75207", "75208",
    "75209", "75210", "75211", "75212", "75214", "75215", "75216", "75217",
    "75218", "75219", "75220", "75223", "75224", "75225", "75226", "75227",
    "75228", "75229", "75230", "75231", "75232", "75233", "75234", "75235",
    "75236", "75237", "75238", "75240", "75241", "75243", "75244", "75246",
    "75247", "75248", "75249", "75251", "75252", "75253", "75254", "75287"
]

# Define Walmart POI types
walmart_pois = [
    {
        "poi_name": "Walmart Supercenter",
        "poi_base_id": 1000
    },
    {
        "poi_name": "Walmart Neighborhood Market",
        "poi_base_id": 2000
    },
    {
        "poi_name": "Walmart Marketplace",
        "poi_base_id": 3000
    }
]

# Function to generate a list of Walmart stores in the given ZIP codes with unique POI Chain IDs
def list_walmart_stores_by_zip():
    data = []
    for zip_code in zip_codes:
        for poi in walmart_pois:
            # Generate a unique POI Chain ID by adding the base ID to the last digits of the ZIP code
            unique_poi_chain_id = poi["poi_base_id"] + int(zip_code[-3:])
            entry = {
                "ZIP_Code": zip_code,
                "Chain_Name": "Walmart Supercenter",  # Chain Name is always Walmart Supercenter
                "Chain_ID": 1,  # Chain ID is always 1
                "POI_Name": poi["poi_name"],
                "POI_Chain_ID": unique_poi_chain_id
            }
            data.append(entry)
    return pd.DataFrame(data)

# Path to save the file
output_directory = r"C:\Users\venka\Desktop\FootTraffic"
os.makedirs(output_directory, exist_ok=True)

# Generate and save the list of Walmart stores by ZIP code
walmart_df = list_walmart_stores_by_zip()
filename = "Walmart_Stores_List_by_ZIP_Code.csv"
filepath = os.path.join(output_directory, filename)
walmart_df.to_csv(filepath, index=False)

# Display the first few entries to verify
print(walmart_df.head(150))
