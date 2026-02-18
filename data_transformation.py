import pandas as pd
import numpy as np
from datetime import datetime

# Load original data
df = pd.read_csv('data/HHS_Unaccompanied_Alien_Children_Program_.csv')

# Clean column names
df.columns = ['Date', 'Apprehended', 'CBP_Custody', 'Transferred_Out', 'HHS_Care', 'Discharged']

# Convert date and remove commas from numbers
df['Date'] = pd.to_datetime(df['Date'])
for col in ['Apprehended', 'CBP_Custody', 'Transferred_Out', 'HHS_Care', 'Discharged']:
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce')

# Remove rows with all NaN values
df = df.dropna(how='all').reset_index(drop=True)

# Sort by date
df = df.sort_values('Date').reset_index(drop=True)

# Calculate efficiency metrics
df['Transfer_Efficiency_Ratio'] = df['Transferred_Out'] / df['CBP_Custody'].replace(0, np.nan)
df['Discharge_Effectiveness'] = df['Discharged'] / df['HHS_Care'].replace(0, np.nan)
df['Pipeline_Throughput'] = (df['Transferred_Out'] + df['Discharged']) / df['Apprehended'].replace(0, np.nan)

# Calculate net changes
df['CBP_Net_Change'] = df['Apprehended'] - df['Transferred_Out']
df['HHS_Net_Change'] = df['Transferred_Out'] - df['Discharged']
df['Total_System_Load'] = df['CBP_Custody'] + df['HHS_Care']

# Calculate bottleneck scores
df['CBP_Bottleneck_Score'] = abs(df['CBP_Net_Change']) / df['Total_System_Load']
df['HHS_Bottleneck_Score'] = abs(df['HHS_Net_Change']) / df['Total_System_Load']

# Calculate discharge stability
df['Discharge_Stability'] = df['Discharged'].rolling(7, min_periods=1).std() / df['Discharged'].rolling(7, min_periods=1).mean()
df['Outcome_Stability_Score'] = 1 - df['Discharge_Stability'].fillna(0)

# Calculate average stay proxy
df['Avg_Stay_Proxy_HHS'] = df['HHS_Care'] / df['Discharged'].replace(0, np.nan)

# Calculate flow balance
df['CBP_Flow_Balance'] = df['Apprehended'] - df['Transferred_Out']
df['HHS_Flow_Balance'] = df['Transferred_Out'] - df['Discharged']

# Extract temporal features
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.strftime('%B')
df['Day_of_Week'] = df['Date'].dt.dayofweek
df['Day_Name'] = df['Date'].dt.strftime('%A')
df['Week'] = df['Date'].dt.isocalendar().week
df['Quarter'] = df['Date'].dt.quarter
df['Is_Weekend'] = (df['Day_of_Week'] >= 5).astype(int)

# Calculate moving averages
for window in [7, 14, 30]:
    df[f'Transfer_Efficiency_MA{window}'] = df['Transfer_Efficiency_Ratio'].rolling(window, min_periods=1).mean()
    df[f'Discharge_Effectiveness_MA{window}'] = df['Discharge_Effectiveness'].rolling(window, min_periods=1).mean()
    df[f'HHS_Care_MA{window}'] = df['HHS_Care'].rolling(window, min_periods=1).mean()

# Save processed data
df.to_csv('data/uac_metrics_processed.csv', index=False)

print(f"✅ Processed {len(df)} records")
print(f"📊 Created {len(df.columns)} features")
print(f"📅 Date range: {df['Date'].min()} to {df['Date'].max()}")
print(f"💾 Saved to: data/uac_metrics_processed.csv")
