import requests
import json
import pandas as pd

# Ingest a single Parquet file into Tinybird
def ingest_parquet_file(tinybird_url, token):
    """Function to ingest a single Parquet file into Tinybird"""
    parquet_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"  # Example file for the task

    # Prepare the data for Tinybird
    data = json.dumps({'url': parquet_url})

    # Send request to Tinybird API
    response = requests.post(tinybird_url, params={'name': 'nyc_trip_data', 'token': token}, data=data)

    if response.status_code == 200:
        print(f"Successfully ingested {parquet_url}")
    else:
        print(f"Failed to ingest {parquet_url}. Status code: {response.status_code}")
        print(response.text)

# Clean and filter the data
def clean_data(dataframe):
    """Function to clean and filter the data"""
    # Filter out invalid or extreme trip distances
    cleaned_df = dataframe[(dataframe['trip_distance'] > 0) & (dataframe['trip_distance'] < 100)]
    return cleaned_df

# Calculate the 0.9 percentile for trip distance
def calculate_percentile(dataframe, percentile_value=0.9):
    """Function to calculate the percentile and return trips above that value"""
    threshold = dataframe['trip_distance'].quantile(percentile_value)
    result_df = dataframe[dataframe['trip_distance'] > threshold]
    return result_df

# Export data to a CSV file
def export_to_csv(dataframe, filename='output.csv'):
    """Export the dataframe to a CSV file"""
    dataframe.to_csv(filename, index=False)

# Main function to run the solution
def main():
    # Tinybird configuration
    tinybird_url = 'https://api.us-east.aws.tinybird.co/v0/events'
    token = 'p.eyJ1IjogImI3OTI4OTdiLTFmZWItNDNiOC1hZTA5LTYxNzQ4YzljNGFkMSIsICJpZCI6ICIwMWFhYjZhYS05MDYzLTQ1MDctODlkMS00ZDE2NTcxMjhlYTkiLCAiaG9zdCI6ICJ1cy1lYXN0LWF3cyJ9.zaMfsqeoZJeY3usiYX8WwaUX6NgUGZk81LqD6yQB1-8'

    # Step 1: Ingest one file for the task
    ingest_parquet_file(tinybird_url, token)

    # Step 2: Simulate loading data into a pandas dataframe
    # (In a real scenario, you will fetch the data from Tinybird or a file)
    # Example dataframe (replace with actual data fetching logic)
    data = {'trip_distance': [1, 20, 0, 150, 2, 5]}  # Replace this with actual fetched data
    df = pd.DataFrame(data)

    # Step 3: Clean the data
    cleaned_df = clean_data(df)

    # Step 4: Calculate the 0.9 percentile
    result_df = calculate_percentile(cleaned_df)

    # Step 5: Export results to CSV
    export_to_csv(result_df)

if __name__ == "__main__":
    main()
 
