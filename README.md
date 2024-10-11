# NYC Taxi Parquet File Ingestion Script

This Python script automates the ingestion of NYC Taxi Parquet files (yellow, green, and FHV trip data) from the NYC TLC cloud storage into Tinybird using the Events API.

## How It Works

The script:
- Loops through multiple **trip types**: `yellow_tripdata`, `green_tripdata`, `fhv_tripdata`.
- Iterates through multiple **years** (2018 to 2024) and **months** (January to December).
- Constructs the Parquet file URL for each month and trip type.
- Sends the Parquet file URL to the Tinybird Events API for ingestion.

## Prerequisites

- Python 3.x
- The `requests` library (install it with `pip install requests`).

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
   cd YOUR-REPO
