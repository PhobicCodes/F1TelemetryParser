# Basic F1 telemetry parser

import csv
from pathlib import Path 

data_file = Path(__file__).parent.parent / "data" / "sample_laps.csv"

lap_times = []
with open(data_file, newline = "") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lap_times.append(float(row["lap_time"]))
        
average = sum(lap_times) / len(lap_times)
fastest = min(lap_times)
slowest = max(lap_times)


print(f"Average lap time: {average:.2f} seconds")
print(f"fastest lap time: {fastest:.2f} seconds")
print(f"slowest lap time: {slowest:.2f} seconds")