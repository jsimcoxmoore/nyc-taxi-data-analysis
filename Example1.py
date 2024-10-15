import requests

# Define the base URL
base_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_'

# Define the range of years and months
years = [2023, 2024]
months = range(1, 13)

# Loop through each year and month, ingesting each file
for year in years:
    for month in months:
        file_url = f'{base_url}{year}-{month:02}.parquet'
        response = requests.post(
            f'https://api.us-east.aws.tinybird.co/v0/datasources?url={file_url}',
            headers={'Authorization': 'Bearer YOUR_TINYBIRD_TOKEN'}
        )
        if response.status_code == 200:
            print(f'Successfully ingested {file_url}')
        else:
            print(f'Failed to ingest {file_url}: {response.status_code}')

