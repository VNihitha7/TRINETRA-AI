import sqlite3
import pandas as pd



conn=sqlite3.connect(

"violations.db"

)



df=pd.read_sql(

"SELECT * FROM violations",

conn

)



df["timestamp"]=pd.to_datetime(

df["timestamp"]

)



df["hour"]=df["timestamp"].dt.hour



print()


print(


df.groupby(

"hour"

).size()

)


conn.close()