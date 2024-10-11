## Setup

- project uses jupyter notebook
- create an environment
- install pandas 

## Features

- **Idle Time Adjustment**: Each session (FDR) has its end time reduced by 10 minutes to exclude idle time. If this adjusted end time becomes earlier than the start time, the original end time is kept.
- **Total Volume Calculation**: The script calculates the total data volume for each call by summing up the upload and download data volumes across all FDRs for a given user and domain.
- **Total Duration Calculation**: The total duration of a call is calculated as the time between the earliest start time and the latest (adjusted) end time.
- **Bit Rate Calculation**: The bit rate is computed as the total data volume divided by the total time (in kilobits per second).
- **Call Classification**: Calls with a bit rate of 200 kbps or less are classified as **Audio** calls, while those with a higher bit rate are classified as **Video** calls.

## Data Input

The input data is a CSV file containing the following columns:
- `starttime`: The start time of the session (FDR) in the format `YYYY-MM-DDHH:MM:SS`.
- `endtime`: The end time of the session (FDR).
- `msisdn`: The user identifier (phone number or similar).
- `ulvolume`: The upload volume of the session in bytes.
- `dlvolume`: The download volume of the session in bytes.
- `domain`: The domain or application type for the session.

### Results:
- The results are saved to voip_call_output.csv

### Example:

```csv
starttime,endtime,msisdn,ulvolume,dlvolume,domain
2021-04-0212:23:10,2021-04-0212:24:48,1,10819,9960,app1
2021-04-0212:28:56,2021-04-0212:33:12,1,16067,10663,app1

