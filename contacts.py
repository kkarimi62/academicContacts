import pandas as pd

df=pd.read_csv('academicContacts.csv',comment='#',dtype={'group_code': str})
print(df)
