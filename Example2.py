import requests
from concurrent.futures import ThreadPoolExecutor

def ingest_file(file_url, token):
    """Function to ingest a file into Tinybird."""
    response = requests.post(
        f'https://api.us-east.aws.tinybird.co/v0/datasources?url={file_url}',
        headers={'Authorization': f'Bearer {token}'}
    )
    if response.status_code == 200:
        print(f'Successfully ingested {file_url}')
    else:
        print(f'Failed to ingest {file_url}: {response.status_code}')

# Example usage with parallel processing
years = [2023, 2024]
months = range(1, 13)
token = 'YOUR_TINYBIRD_TOKEN'

# Construct all the file URLs in advance
file_urls = [f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month:02}.parquet'
             for year in years for month in months]

# Use ThreadPoolExecutor to run requests in parallel
with ThreadPoolExecutor() as executor:
    executor.map(lambda url: ingest_file(url, token), file_urls)
