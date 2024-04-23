import pandas

df = pandas.read_excel(r'C:\Users\bluek\OneDrive\Desktop\CS 591\data4.xlsx')

deidentIDData = pandas.DataFrame(df,columns=['DeidentID'])
recIDData = pandas.DataFrame(df,columns=['RecID'])
ParentRDeviceUploadsIDData = pandas.DataFrame(df,columns=['ParentRDeviceUploadsID'])
DeviceDtTmData = pandas.DataFrame(df,columns=['DeviceDtTm'])
RecordTypeData = pandas.DataFrame(df,columns=['RecordType'])
ValueData = pandas.DataFrame(df,columns=['Value'])
UnitsData = pandas.DataFrame(df,columns=['Units'])
SortOrdData = pandas.DataFrame(df,columns=['SortOrd'])
UnusableData = pandas.DataFrame(df,columns=['Unusable'])
UnusableReasonData = pandas.DataFrame(df,columns=['UnusableReason'])



print(deidentIDData)
print(recIDData)
print(AE_DescriptionData)
print(AE_StartDateData)
print(AE_StopDateData)
print(AE_TypeData)
print(AE_SeriousData)
print(AE_IntensityData)
print(AE_RelatedData)
print(AEActionTakenData)
print(AE_OtherWrittenData)
print(AEOutcomeData)