# NYC Taxi Data Ingestion and Processing

This Python script automates the ingestion of NYC Yellow Taxi trip data from Parquet files into Tinybird. The current implementation is designed to ingest and process **one Parquet file** for the assessment, as specified. Additionally, the solution is flexible and can be scaled to handle multiple files in the future by modifying the code.

## Problem Overview

The goal is to ingest NYC Taxi trip data, clean it, calculate the 0.9 percentile for trip distances, and export the results into a CSV file. The solution is expected to handle one file for now, but also demonstrates how it could scale to handle multiple files and large datasets.

## Assumptions

1. **Data Scope**:
   - This solution processes one Parquet file (`yellow_tripdata_2024-01.parquet`) as required for the assessment.
   - **Scalability**: In future iterations, the script can be easily modified to loop through trip types (`yellow`, `green`, `fhv`), years, and months to process all available files. This modular design ensures that the solution can scale without significant changes to the core logic.

2. **Data Cleaning**:
   - The `trip_distance` column is cleaned by removing trips with a distance of `0` and trips above `100` miles, which are considered outliers.
   - **Assumptions**: These thresholds (0 and 100 miles) were chosen to remove outliers based on common data issues. These thresholds are adjustable depending on data exploration or specific business rules.

3. **Distance Calculation**:
   - The script calculates the 0.9 percentile based on the cleaned `trip_distance` column. Trips that exceed this threshold are selected for further analysis.
   - This approach assumes that the `trip_distance` column is reliable across all data files.

4. **Output Format**:
   - The output is exported in CSV format, which is sufficient for the assessment. If necessary, the script can be modified to export results in other formats such as JSON or Parquet for better scalability in large datasets.

## How It Works

1. **Ingest Parquet File**:
   - The script ingests one Parquet file (`yellow_tripdata_2024-01.parquet`) into the Tinybird data source using the Events API.
   
2. **Data Cleaning**:
   - The `trip_distance` column is cleaned by removing invalid entries (trips with distance `0` or those exceeding 100 miles).
   
3. **Percentile Calculation**:
   - The script calculates the 0.9 percentile of `trip_distance`, returning all trips above this threshold.
   
4. **Export to CSV**:
   - The results are exported to a CSV file named `output.csv`.

## Edge Cases

1. **Missing Files**:
   - Currently, the script processes one file. If multiple files were to be ingested, the solution would handle missing files by logging errors and continuing to process the remaining files.
   
2. **Schema Changes**:
   - The script assumes that the schema remains consistent across files. If there are changes in the data schema, the cleaning and ingestion logic would need to be updated accordingly.
   
3. **Invalid or Extreme Values**:
   - The data cleaning function filters out invalid `trip_distance` values (such as `0` or extreme values >100 miles). This can be adjusted based on the specific needs of the analysis.

## Scalability Considerations

1. **Ingestion Process**:
   - **Current State**: The script processes a single Parquet file. In the future, the ingestion process can be scaled by looping through trip types, years, and months. Batch processing or parallel processing could be used to ingest multiple files concurrently.
   
2. **Data Storage**:
   - For larger datasets, Parquet format is recommended for storage efficiency. Although CSV is sufficient for the current task, using Parquet would reduce storage size and improve performance when dealing with large volumes of data.

3. **Data Processing**:
   - The 0.9 percentile calculation can be scaled across larger datasets. If the dataset grows significantly, distributed computing frameworks or optimized SQL queries could be used to improve performance.

4. **Error Handling**:
   - Currently, basic error handling is implemented (e.g., logging failed file ingestion). In the future, a more advanced error handling and retry mechanism could be introduced to ensure no data is missed.

## Trade-offs

1. **File Format**:
   - CSV is simple and easy to use for small datasets, but for large datasets, the Parquet format is more efficient in terms of storage and processing. The solution could easily be adapted to export results in Parquet.
   
2. **Error Handling**:
   - The current implementation logs errors and moves on to the next file (if multiple files are processed). For a production-ready system, you might want to add retry mechanisms or more robust error handling.
   
3. **Performance**:
   - While this solution works efficiently for one file, processing multiple files at once may require optimizations like batch processing, parallelism, or distributed computing to handle a large number of files or a large dataset.

## How to Run

### Prerequisites

- **Python 3.x** should be installed on your system.
- A **Tinybird** account with an **API token** to ingest data.
- Required Python libraries (requests and pandas).

### Step 1: Clone the Repository

1. Open your terminal or command prompt.
2. Run the following command to clone the repository to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/nyc-taxi-data-analysis.git
cd nyc-taxi-data-analysis
```

### Step 2: Install Required Libraries

Run the following command in the terminal to install the required Python libraries:

```bash
pip install requests pandas
```

### Step 3: Configure Tinybird API Token

1. Open the `solution.py` file in your code editor.
2. Find the line that says:

```python
token = 'YOUR_TINYBIRD_TOKEN'
```
3. Replace 'YOUR_TINYBIRD_TOKEN' with the actual API token from your Tinybird account.

### Step 4: Run the Script

Run the following command to execute the script:

```bash
python solution.py
```
Or if you're using Python 3:
```bash
python3 solution.py
```
### Step 5: Check the Output

1. After the script completes, the processed data will be saved as `output.csv` in the project directory.
2. Open `output.csv` to review the results and ensure the correct trips (those over the 0.9 percentile of distance traveled) have been selected.

### Future Improvements

1. **Parallel Processing**:
   - Currently, the script processes one file at a time. To improve performance and handle large datasets efficiently, you can implement parallel processing. By using Python’s `concurrent.futures` or a similar library, you can ingest multiple Parquet files simultaneously, drastically reducing the time required for ingestion, especially when dealing with a full year's worth of taxi data.

2. **Schema Validation**:
   - As the NYC Taxi dataset evolves, schema changes can occur across different files. Adding schema validation ensures that the data structure remains consistent, preventing errors during ingestion or processing. By implementing checks with a library like `PyArrow` or using a data validation framework, you can ensure the integrity of the dataset before ingestion.

3. **Data Quality Checks**:
   - Beyond the basic cleaning of `trip_distance` values, you could implement additional quality checks on other columns. For instance:
     - Validate `pickup` and `dropoff` datetime values to ensure they are logical (i.e., `dropoff` should always be after `pickup`).
     - Check for missing or null values in essential fields and handle them appropriately (e.g., filtering or filling in missing values).
     - Verify that geolocation coordinates (if available) are within reasonable ranges (e.g., latitude between -90 and 90, longitude between -180 and 180).

4. **Error Handling and Retries**:
   - To make the ingestion process more robust, especially when scaling to multiple files, implement more advanced error handling. For example:
     - Catch network-related exceptions during file ingestion and implement retry logic (e.g., using exponential backoff).
     - Log detailed error messages to a log file, allowing for easy debugging if ingestion fails or if a file is corrupted.
     - Track failed file ingestions and attempt to reprocess them at a later time without crashing the entire pipeline.
   
5. **Data Storage Optimization**:
   - Although CSV is sufficient for small datasets, Parquet format is better suited for large datasets due to its columnar storage format, which is more storage-efficient and faster to process. You could add functionality to store processed results in Parquet instead of CSV, improving both performance and storage as the dataset grows.
   
6. **Scalability for Full Dataset**:
   - As the current solution is designed for one file, scaling to handle the entire NYC Taxi dataset across multiple years will require more sophisticated orchestration. Consider automating the ingestion pipeline using workflow management tools like Apache Airflow, allowing the ingestion and processing of multiple files in a structured, scheduled manner.

7. **Improved Data Visualization**:
   - Once the data has been processed, you can integrate data visualization to provide insights directly. This can be achieved using libraries such as `Matplotlib` or `Seaborn`, or even by exporting the cleaned data to a visualization platform like Tableau or Power BI. Adding these insights could help users of the dataset better understand trends, such as how trip distances vary by time of year or across different regions.



