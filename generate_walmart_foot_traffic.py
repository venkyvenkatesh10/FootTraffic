import random
import pandas as pd
import uuid
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

# Sample first and last names
first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie", "Michael", "Laura", "David", "Sarah"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

# Device makes and models
device_makes_models = {
    "Apple": ["iPhone 12", "iPhone 13", "iPhone SE"],
    "Samsung": ["Galaxy S21", "Galaxy Note 20", "Galaxy A52"],
    "Google": ["Pixel 5", "Pixel 6", "Pixel 4a"],
    "LG": ["LG Velvet", "LG Wing", "LG G8 ThinQ"],
    "Motorola": ["Moto G Power", "Moto G Stylus", "Moto G Play"]
}

# Function to generate random sample data for foot traffic
def generate_sample_data(zip_code, poi, num_samples=100):
    data = []
    for _ in range(num_samples):
        customer_id = str(uuid.uuid4())
        customer_first_name = random.choice(first_names)
        customer_last_name = random.choice(last_names)
        customer_phone_number = f"+1-{random.randint(200, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        device_make = random.choice(list(device_makes_models.keys()))
        device_model = random.choice(device_makes_models[device_make])
        lat = round(random.uniform(32.70, 32.99), 6)
        long = round(random.uniform(-96.99, -96.70), 6)
        upstream_data = round(random.uniform(0.1, 5.0), 2)
        downstream_data = round(random.uniform(0.1, 5.0), 2)
        apps = random.choice(["Facebook", "Instagram", "WhatsApp", "YouTube", "Twitter"])
        category = random.choice(["Social Media", "Streaming", "Gaming", "Shopping", "News"])
        https = random.choice(["Yes", "No"])
        unique_poi_chain_id = poi["poi_base_id"] + int(zip_code[-3:])
        
        entry = {
            "Customer_ID": customer_id,
            "Customer_First_Name": customer_first_name,
            "Customer_Last_Name": customer_last_name,
            "Customer_Phone_Number": customer_phone_number,
            "Device_Make": device_make,
            "Device_Model": device_model,
            "Latitude": lat,
            "Longitude": long,
            "Upstream_Data_GB": upstream_data,
            "Downstream_Data_GB": downstream_data,
            "Apps": apps,
            "Category": category,
            "HTTPS": https,
            "Date": "08/15/2024",
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

# Generate and save sample foot traffic data for each POI in each ZIP code
all_data = []
for zip_code in zip_codes:
    for poi in walmart_pois:
        foot_traffic_df = generate_sample_data(zip_code, poi, num_samples=100)
        all_data.append(foot_traffic_df)

# Combine all data into one DataFrame and save it
combined_df = pd.concat(all_data, ignore_index=True)
filename = "Walmart_Foot_Traffic_Sample_Data.csv"
filepath = os.path.join(output_directory, filename)
combined_df.to_csv(filepath, index=False)

# Display the first few entries to verify
print(combined_df.head(20))
