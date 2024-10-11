from datetime import datetime
import time

# Function to calculate the time difference in seconds
def time_difference(t1, t2):
    # Define the format of the input timestamps
    timestamp_format = "%a %d %b %Y %H:%M:%S %z"
    
    # Convert the timestamps to datetime objects
    dt1 = datetime.strptime(t1, timestamp_format)
    dt2 = datetime.strptime(t2, timestamp_format)
    
    # Calculate the difference in seconds and return the absolute value
    return abs(int((dt1 - dt2).total_seconds()))

# Input the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the two timestamps
    t1 = input().strip()
    t2 = input().strip()
    
    # Print the absolute difference in seconds
    print(time_difference(t1, t2))
