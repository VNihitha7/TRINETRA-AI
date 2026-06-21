import sqlite3
import pandas as pd



conn=sqlite3.connect(

"violations.db"

)


df=pd.read_sql(

"SELECT * FROM violations",

conn

)



repeat=df.groupby(

"plate"

).size()



repeat=repeat.reset_index()



repeat.columns=[

"plate",

"violations"

]



print()


print(

repeat.sort_values(

"violations",

ascending=False

)

)


conn.close()
