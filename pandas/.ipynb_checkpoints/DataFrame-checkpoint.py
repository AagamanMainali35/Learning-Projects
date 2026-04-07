from pandas import Series as sr
import pandas as pd
import json

# creating a Dataframe
data=pd.DataFrame({
    "no":[1,2,3,4],
    "name":['aagaman',None,'sita',None],
    "age":[1,None,3,4],
    "address":['KTM',None,'BRT','JHP']
},index=['employee1','employee2','employee3','employee4'])

#print sinle row
print(data.loc['employee1']) 

# single row selection with specified colums
print(data.loc['employee1',['age','name']]) 

# print multiple rows
print(data.loc[['employee1','employee3']]) 

 # select multiple rows with custom columnm
print(data.loc[['employee1','employee3'],['age','address']])

# range of row sleection
print(data.loc['employee1':'employee3',['age','address']]) 

#Adding new Row:
data['SID']=[1,2,3,4]

# Adding a new column
new_row=pd.DataFrame({
    "no":[5,6],
    "name":['sita2','sita3'],
    "age":[21,18],
    "address":['PKR','KTM'],
    "Number":[903,00],
    "SID":[5,6]
})
#using pandas .concat method
data=pd.concat([data,new_row],ignore_index=True)  # ignore_index dosen't start the index from 0 again and continues the indexing

#Filtering the data frame bassed on the masked Data
eligibleGuys=data[data['age']>18]

#Filtering based on m,ultiple conditions
eligibleAddress=data[(data['name']=='aagaman') & (data['address'=='KTM'])]

print(eligibleGuys)

#converting data to json with indent  NOTE: this just print data just holds this in variable
data.to_json(orient='records',indent=4)


