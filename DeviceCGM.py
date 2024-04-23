import pandas
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt




df = pandas.read_excel(r'C:\Users\bluek\OneDrive\Desktop\CS 591\data1.xlsx')

deidentIDData = pandas.DataFrame(df,columns=['DeidentID'])
recIDData = pandas.DataFrame(df,columns=['RecID'])
parentRDeviceUploadsIDData = pandas.DataFrame(df,columns=['ParentRDeviceUploadsID'])
deviceDtTmData = pandas.DataFrame(df,columns=['DeviceDtTm'])
recordTypeData = pandas.DataFrame(df,columns=['RecordType'])
valuesData = pandas.DataFrame(df, columns=['Value'])
unitsData = pandas.DataFrame(df,columns=['Units'])
sortOrdData = pandas.DataFrame(df,columns=['SortOrd'])
unusableData = pandas.DataFrame(df,columns=['Unusable'])
unusableReasonData = pandas.DataFrame(df,columns=['UnusableReason'])

print(deidentIDData)
print(recIDData)
print(parentRDeviceUploadsIDData)
print(deviceDtTmData)
print(recordTypeData)
print(valuesData)
print(unitsData)
print(sortOrdData)
print(unusableData)
print(unusableReasonData)

def preprocess_DeviceDtTmData(df):
    # Check if 'DeviceDtTm' column exists in the DataFrame
    if 'DeviceDtTm' not in df.columns:
        raise ValueError("DataFrame does not contain 'DeviceDtTm' column.")

    # Calculate the number of rows in the DataFrame
    num_rows = len(df)

    # Initialize lists to store preprocessed data
    middle_times = []

    # Iterate over the 'DeviceDtTm' column in steps of 3
    for i in range(1, num_rows, 3):
        # Get three consecutive times
        middleTime = df.iloc[i:i+1]['DeviceDtTm']

        # Append the middle time to the list
        middle_times.append(middleTime)

    # Create a new DataFrame with all of the middle times
    preprocessed_df = pd.DataFrame({'Averaged_Dates': middle_times})

    return preprocessed_df

# Assuming df is your original DataFrame
preprocessed_df = preprocess_DeviceDtTmData(df)

# Print the preprocessed DataFrame
print(preprocessed_df)

def preprocessedValues(df):
    valueDataColumns = df['Value']
    preprocessedValueData = []

    # Average the first two values separately
    preprocessedValueData.append((valueDataColumns.iloc[0] + valueDataColumns.iloc[1]) / 2)
    preprocessedValueData.append((valueDataColumns.iloc[2] + valueDataColumns.iloc[3]) / 2)

    # Calculate the average for every three values in between
    for i in range(4, len(valueDataColumns) - 2, 3):
        average = (valueDataColumns.iloc[i] + valueDataColumns.iloc[i+1] + valueDataColumns.iloc[i+2]) / 3
        preprocessedValueData.append(average)

    # Average the last two values separately
    preprocessedValueData.append((valueDataColumns.iloc[-4] + valueDataColumns.iloc[-3]) / 2)
    preprocessedValueData.append((valueDataColumns.iloc[-2] + valueDataColumns.iloc[-1]) / 2)

    # Create a new DataFrame with the preprocessed values
    preprocessed_df = pd.DataFrame(preprocessedValueData, columns=['Value'])
    return preprocessed_df

# Assuming df is the DataFrame containing the 'Values' column
preprocessed_values_df = preprocessedValues(df)
print(preprocessed_values_df)


df["DeviceDtTm"].plot(kind = 'hist')

df["Value"].plot(kind = 'hist')



df['DeviceDtTm'] = pd.to_datetime(df['DeviceDtTm'])

df['Day'] = df['DeviceDtTm'].dt.day

plt.figure(figsize=(10, 6))
df.boxplot(column='Value', by='Day')
plt.title('Boxplot of Values by Day')
plt.xlabel('Day')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.tight_layout()

df.plot(kind = 'scatter', x = 'Value', y = 'DeviceDtTm')
plt.show()


