import requests
import json

# Define the base URL pattern for Parquet files
base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/{trip_type}_{year}-{month}.parquet"

# Define the trip types, years, and months to loop through
trip_types = ["yellow_tripdata", "green_tripdata", "fhv_tripdata"]
years = range(2018, 2024)  # Adjust this range for the years you need
months = range(1, 13)  # Loop through all 12 months

# Define the Tinybird Events API endpoint and token
tinybird_url = 'https://api.us-east.aws.tinybird.co/v0/events'
token = 'p.eyJ1IjogImI3OTI4OTdiLTFmZWItNDNiOC1hZTA5LTYxNzQ4YzljNGFkMSIsICJpZCI6ICIwMWFhYjZhYS05MDYzLTQ1MDctODlkMS00ZDE2NTcxMjhlYTkiLCAiaG9zdCI6ICJ1cy1lYXN0LWF3cyJ9.zaMfsqeoZJeY3usiYX8WwaUX6NgUGZk81LqD6yQB1-8'

# Loop through each trip type, year, and month to generate the URLs and ingest them into Tinybird
for trip_type in trip_types:
    for year in years:
        for month in months:
            # Format the month with leading zero
            month_str = str(month).zfill(2)
            # Construct the Parquet file URL
            parquet_url = base_url.format(trip_type=trip_type, year=year, month=month_str)
            
            # Prepare the data payload for Tinybird API
            data = json.dumps({
                'url': parquet_url
            })
            
            # Send the request to Tinybird to ingest the Parquet file
            r = requests.post(tinybird_url, 
                              params={
                                  'name': 'nyc_trip_data',  # Your data source name
                                  'token': token,
                              }, 
                              data=data)
            
            # Check if the ingestion was successful
            if r.status_code == 200:
                print(f"Successfully ingested {parquet_url}")
            else:
                print(f"Failed to ingest {parquet_url}. Status code: {r.status_code}")
                print(r.text)
