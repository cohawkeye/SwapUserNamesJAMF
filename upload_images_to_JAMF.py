import os
import pandas as pd

# Step 1: Read both CSV files
old_data = pd.read_csv('old_data.csv')
new_data = pd.read_csv('new_data.csv')

# Step 2: Merge DataFrames on 'email' to get correspondence between 'old_id' and 'new_id'
merged_data = pd.merge(old_data, new_data, on='email', how='inner')

# Step 3: List files in the 'images' folder
image_files = os.listdir('images')

# Step 4: Rename files based on the mapping
for index, row in merged_data.iterrows():
    old_id = row['old_id']
    new_id = row['new_id']
    old_file_name = str(old_id) + '.png'
    new_file_name = str(new_id) + '.png'
    
    if old_file_name in image_files:
        os.rename(os.path.join('images', old_file_name), os.path.join('images', new_file_name))
        print(f"Renamed {old_file_name} to {new_file_name}")
    else:
        print(f"File {old_file_name} not found in 'images' folder.")
