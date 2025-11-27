import os
import pandas as pd 

data = {"Name": ["Vishal", "Payal", "Aditya"],
        "Age": [29, 30, 32],
        "City": ["Dubai", "India", "Qatar"]
       }

df = pd.DataFrame(data)

# Adding new row to df for v2
new_row_data_1 = {"Name": "Sheetal", "Age": 45 , "City": "Australia"}
df.loc[len(df)] = new_row_data_1

# Adding new row to df for v3
new_row_data_2 = {"Name": "Mahesh", "Age": 57 , "City": "Delhi"}
df.loc[len(df)] = new_row_data_2

data_dir="Data"
os.makedirs(data_dir, exist_ok=True)
file_path = os.path.join(data_dir, "sample_data.csv")

df.to_csv(file_path, index=False)
print(f'CSV file saved to {file_path}')