import streamlit as st
import pandas as pd 


st.title(" Sales Data analysis")

data=({
  "Products":["Computer","Chear","Acide","Rich_seed","NS_bottel"],
  "category":["Eletonic","Furniture","Camical","Agriculture","Medical"],
  "sales":[1200,3500,9000,5609,67890]
})
df=pd.DataFrame(data)
selected_df=st.sidebar._selectbox(
  "select Category",
  ["All"]+list(df["category"].unique())
)
if selected_df=="All":
  filtered_df=df
else:
  filtered_df=df[df['category']==selected_df]


st.write("Filter table")
st.dataframe(filtered_df)
st.write("sales line chate")
st.line_chart(filtered_df["sales"])