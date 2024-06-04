import os
import requests
import csv

folder_path = "/workspaces/Covid19-postgreSQL-Warehouse/data/raw_data"

url = "https://covid19-lake.s3.us-east-2.amazonaws.com/rearc-covid-19-testing-data/csv/states_daily/states_daily.csv"
response = requests.get(url)

if response.status_code == 200:
    data_lines = response.text.splitlines()

    csv_filename = os.path.join(folder_path, 'states_daily.csv')
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for line in data_lines:
            row = line.split(',')
            writer.writerow(row)

    print(f"Data saved to {csv_filename}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")