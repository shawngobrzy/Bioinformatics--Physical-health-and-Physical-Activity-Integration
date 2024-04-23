import pandas

df = pandas.read_excel(r'C:\Users\bluek\OneDrive\Desktop\CS 591\data2.xlsx')

deidentIDData = pandas.DataFrame(df,columns=['DeidentID'])
recIDData = pandas.DataFrame(df,columns=['RecID'])
AE_DescriptionData = pandas.DataFrame(df,columns=['AE_Description'])
AE_StartDateData = pandas.DataFrame(df,columns=['AE_StartDate'])
AE_StopDateData = pandas.DataFrame(df,columns=['AE_StopDate'])
AE_TypeData = pandas.DataFrame(df,columns=['AE_Type'])
AE_SeriousData = pandas.DataFrame(df,columns=['AE_Serious'])
AE_IntensityData = pandas.DataFrame(df,columns=['AE_Intensity'])
AE_RelatedData = pandas.DataFrame(df,columns=['AE_Related'])
AEActionTakenData = pandas.DataFrame(df,columns=['AEActionTaken'])
AE_OtherWrittenData = pandas.DataFrame(df,columns=['AE_OtherWritten'])
AEOutcomeData = pandas.DataFrame(df,columns=['AEOutcome'])



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


