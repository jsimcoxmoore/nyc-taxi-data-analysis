import pandas as pd

# Load the Parquet file (update the file path if necessary)
df = pd.read_parquet('yellow_tripdata.parquet')

# Calculate the 0.9 percentile for the 'trip_distance' column
percentile_90 = df['trip_distance'].quantile(0.9)

# Filter the DataFrame for trips that exceed the 0.9 percentile in distance traveled
filtered_trips = df[df['trip_distance'] > percentile_90]

# Save the filtered trips to a CSV file
filtered_trips.to_csv('filtered_trips.csv', index=False)

print(f"Filtered {len(filtered_trips)} trips that exceed the 0.9 percentile in distance traveled.")

# Test script: python solution.py
