import os
import pandas as pd 

data = {"Name": ["Vishal", "Payal", "Aditya"],
        "Age": [29, 30, 32],
        "City": ["Dubai", "India", "Qatar"]
       }

df = pd.DataFrame(data)

data_dir="Data"
os.makedirs(data_dir, exist_ok=True)
file_path = os.path.join(data_dir, "sample_data.csv")

df.to_csv(file_path, index=False)
print(f'CSV file saved to {file_path}')