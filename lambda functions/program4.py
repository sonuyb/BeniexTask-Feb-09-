from datetime import datetime
extract_info = lambda dt: (dt.year, dt.month, dt.day, dt.strftime("%H:%M:%S"))
current_datetime = datetime.now()
result = extract_info(current_datetime)
print(result)
print("Year:", result[0])
print("Month:", result[1])
print("Date:", result[2])
print("Time:", result[3])
