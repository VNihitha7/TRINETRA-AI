import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image


st.set_page_config(
    page_title="TRINETRA AI",
    layout="wide"
)


st.markdown("""

<style>

.stApp{
background-color:#0E1117;
color:white;
}

.metric{
padding:20px;
border-radius:15px;
background:#1E1E2F;
}

</style>

""",unsafe_allow_html=True)


st.title("🚦 TRINETRA AI")
st.subheader("AI Powered Traffic Enforcement System")


conn=sqlite3.connect("violations.db")

df=pd.read_sql(

"SELECT * FROM violations",

conn

)


c1,c2,c3,c4=st.columns(4)


c1.metric(

"Violations",

len(df)

)


c2.metric(

"Avg Severity",

round(df["severity"].mean(),1)

)


c3.metric(

"Max Severity",

df["severity"].max()

)


helmet_count=len(df)


c4.metric(

"Helmet Cases",

helmet_count

)



st.divider()


left,right=st.columns([2,1])



with left:


    fig=px.histogram(

        df,

        x="severity",

        nbins=10,

        title="Severity Distribution"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )




with right:


    gauge=go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=df["severity"].mean(),


            gauge={

            'axis':{'range':[0,100]},


            'bar':{'color':'red'}

            }

        )

    )



    st.plotly_chart(

        gauge,

        use_container_width=True

    )



st.divider()



st.subheader(

"Recent Violations"

)



st.dataframe(

df.tail(10),

use_container_width=True

)




st.subheader(

"Evidence"

)


img=Image.open(

"output/final_evidence.jpg"

)



st.image(

img,

width=700

)


conn.close()