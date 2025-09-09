# Basic F1 telemetry parser

lap_times = [88.3, 87.9, 88.1, 87,5]
average = sum(lap_times) / len(lap_times)
fastest = min(lap_times)
slowest = max(lap_times)

print(f"Average lap time: {average:.2f} seconds")
print(f"fastest lap time: {fastest:.2f} seconds")
print(f"slowest lap time: {slowest:.2f} seconds")