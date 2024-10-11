import requests

# Define the base URL pattern for Parquet files
base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/{trip_type}_{year}-{month}.parquet"

# Define the trip types, years, and months to loop through
trip_types = ["yellow_tripdata", "green_tripdata", "fhv_tripdata"]
years = range(2018, 2024)  # Adjust this range for the years you need
months = range(1, 13)  # Loop through all 12 months

# Define the Tinybird API endpoint and token
tinybird_url = "https://api.tinybird.co/v0/datasources?name=nyc_trip_data"
headers = {
    "Authorization": "Bearer p.eyJ1IjogImI3OTI4OTdiLTFmZWItNDNiOC1hZTA5LTYxNzQ4YzljNGFkMSIsICJpZCI6ICIwMWFhYjZhYS05MDYzLTQ1MDctODlkMS00ZDE2NTcxMjhlYTkiLCAiaG9zdCI6ICJ1cy1lYXN0LWF3cyJ9.zaMfsqeoZJeY3usiYX8WwaUX6NgUGZk81LqD6yQB1-8",
    "Content-Type": "application/json"
}

# Loop through each trip type, year, and month to generate the URLs and ingest them into Tinybird
for trip_type in trip_types:
    for year in years:
        for month in months:
            # Format the month with leading zero
            month_str = str(month).zfill(2)
            # Construct the Parquet file URL
            parquet_url = base_url.format(trip_type=trip_type, year=year, month=month_str)
            
            # Prepare the Tinybird API request
            data = {"url": parquet_url}
            
            # Send the request to Tinybird
            response = requests.post(tinybird_url, headers=headers, json=data)
            
            # Check if the ingestion was successful
            if response.status_code == 200:
                print(f"Successfully ingested {parquet_url}")
            else:
                print(f"Failed to ingest {parquet_url}. Status code: {response.status_code}")
