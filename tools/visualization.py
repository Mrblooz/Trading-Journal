import pandas as pd
import matplotlib.pyplot as plt

# sample data
data = {    
    "Date": pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05"]),
    "Asset":["EUR/USD"] * 5,
    "Entry Price": [1.2000,1.2500,1.2400, 1.1200,1.1900],
    "Exit Price": [1.2500, 1.2600 , 1.2300, 1.2000, 1.1000],
    "Volume":[100000, 120000, 13000, 14000, 15000],
    "Phase":["Undefined"] * 5,
}

# Create Data frame 
df = pd.DataFrame(data)

# Calculate a rolling mean of 'Entry Price' with a window of size 2
rolling_mean = df["Entry Price"].rolling(window=2).mean()

# Detect wyckof phases based on the rolling mean
df.loc[df["Entry Price"] < rolling_mean, "Phase"] = "Accumulation" # If entry price is below rolling mean
df.loc[df["Entry Price"] > rolling_mean, "Phase" ] = "Markup" # If entry price is above rolling mean

# Visualization of the data
