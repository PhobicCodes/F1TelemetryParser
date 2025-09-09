# Basic F1 telemetry parser
from pathlib import Path 
from data_loader import load_lap_times

data_file = Path(__file__).parent.parent / "data" / "sample_laps.csv"
lap_times = load_lap_times(data_file)

lap_times = load_lap_times(data_file)
        
average = sum(lap_times) / len(lap_times)
fastest = min(lap_times)
slowest = max(lap_times)


print(f"Average lap time: {average:.2f} seconds")
print(f"fastest lap time: {fastest:.2f} seconds")
print(f"slowest lap time: {slowest:.2f} seconds")