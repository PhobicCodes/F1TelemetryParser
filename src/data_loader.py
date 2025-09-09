import csv
from pathlib import Path

def load_lap_times(file_path: Path) -> list[float]:
    lap_times = []
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lap_times.append(float(row["lap_time"]))
    return lap_times