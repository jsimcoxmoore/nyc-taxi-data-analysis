# NYC Yellow Taxi Trips - 0.9 Percentile Distance Filter

## Overview

This repository contains the solution for the Tinybird Data Engineer technical test, which involves identifying all trips in the NYC Yellow Taxi dataset that exceed the 0.9 percentile in distance traveled. The solution leverages Tinybird’s data querying capabilities while focusing on data engineering best practices, scalability, and reproducibility.

## Files

1. solution.py: The main script that calculates the 0.9 percentile and filters the trips.

2. README.md: Documentation explaining the approach, steps to reproduce the solution, and considerations for production environments.

## Questions and Assumptions

1.	Clarification on Dataset Scope:
 
 •	The instructions mention using “any of the parquet files you can find” from the NYC Yellow Taxi dataset. Should I process all available Parquet files, or is there a preferred subset of files (e.g., specific time periods or trip types) that I should focus on? A clarification will help ensure I process the appropriate data.

2.	Definition of Distance Calculation:

 •	The percentile calculation is based on the trip_distance column, but should any additional filtering (such as outlier removal or handling of extreme values) be performed before calculating the 0.9 percentile? Should the distance be calculated exactly as provided in the raw dataset, or are there any adjustments or data cleaning steps you’d prefer (e.g., handling invalid or extreme trip_distance values)?

3.	Clarification on Code and Output Format:
 
 •	Beyond the code itself, is there a preferred format or structure for the output data (e.g., CSV, JSON, or Parquet)? I assume CSV is sufficient unless otherwise specified. Additionally, are there any specific sections you’d like included in the README, such as error handling, edge cases, or scalability considerations?

## Approach

Step 1: Understanding the Problem

The goal is to filter out all trips in the NYC Yellow Taxi dataset that exceed the 0.9 percentile in distance traveled. To achieve this:

1.	We load the dataset in Parquet format.
2.	We calculate the 0.9 percentile for the trip_distance column.
3.	We filter the dataset to include only those trips where the trip_distance exceeds the computed 90th percentile.

Step 2: Tools Used

•	Tinybird: Used for efficient querying and data handling.
•	Python: General scripting to handle data processing (if applicable).
•	Pandas: For reading and manipulating Parquet data locally.

Step 3: Code Breakdown

The main operations in the code include:

1.	Loading the dataset: We use pandas.read_parquet() to load the Parquet file into a DataFrame.
2.	Calculating the 0.9 percentile: The quantile(0.9) method in Pandas is used to compute the 90th percentile of the trip_distance.
3.	Filtering trips: The DataFrame is filtered to include only those rows where the trip_distance exceeds the calculated 90th percentile.
4.	Saving the results: The filtered trips are saved to a CSV file for further use.

Step 4: Reproducibility

To reproduce the results, follow these steps:

1.	Install Dependencies:
Ensure Python 3.x is installed along with Pandas:

  pip install pandas pyarrow


2.	Run the Script:
Place the dataset parquet file (yellow_tripdata.parquet) in the same directory as solution.py and run the script:

  python solution.py


3.	Output:
The output will be a CSV file (filtered_trips.csv) containing all trips that exceed the 0.9 percentile in distance.

Step 5: Tinybird SQL Alternative

If using Tinybird’s platform directly, the following SQL query will calculate the 0.9 percentile and filter trips:

  WITH threshold AS (
    SELECT PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY trip_distance) AS percentile_90
    FROM yellow_taxi_trips
)
SELECT *
FROM yellow_taxi_trips
WHERE trip_distance > (SELECT percentile_90 FROM threshold);

## Future Improvements

1.	Scalability:
   
•	If the dataset grows in size, switching from in-memory processing (like Pandas) to distributed frameworks (such as Apache Spark or Dask) would allow for more efficient data handling.
•	Incremental processing could be implemented to update the dataset continuously rather than reprocessing all data with each run.

3.	Error Handling:

•	Adding data validation steps to check for missing or corrupt values in the trip_distance column would improve robustness.
•	Implementing basic logging to track data loading, processing, and output would help identify and troubleshoot any issues quickly.

3.	Automation:
   
•	The current solution could be automated using a simple scheduling tool (like cron jobs or Apache Airflow) to run periodically, ensuring that new data is processed as it arrives.

5.	Performance Optimization:
   
•	Optimizing storage by using formats like Parquet would reduce both storage costs and query times for larger datasets.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
