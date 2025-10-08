import pandas as pd
import numpy as np

# Define start and end dates
start_date = '2023-04-01'
end_date = '2024-03-31'

# Convert start and end dates to datetime objects
start_dt = pd.to_datetime(start_date)
end_dt = pd.to_datetime(end_date)

# Generate 9993 random dates within the specified range
random_dates = pd.to_datetime(np.random.randint(start_dt.value, end_dt.value, size=9993), unit='ns')

# Create a DataFrame
df = pd.DataFrame({'OrderDate': random_dates})

# Export DataFrame to Excel
excel_file = 'random_order_dates.xlsx'
df.to_excel(excel_file, index=False)

print(f"Excel file '{excel_file}' has been created successfully.")
