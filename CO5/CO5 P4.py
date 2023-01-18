#program 4 cycle 5
#create csv file and import pandas
import pandas as pd
df=pd.read_csv("studentdetails.csv")#,usecols=["Std Name"])
print(df)
#specific_column=df[["address","class"]]
#print("The column is : ")
#print(specific_column)
#print(df.head())
#print(df.tail())

