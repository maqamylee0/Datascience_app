import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache
def load_data():
    df=pd.read_csv("data.csv")
    return df

df=load_data()

def main():
    page = st.sidebar.selectbox("Select a Page",["Home Page","Scatter Plot","Line Plot","Line Chart"])
    
    
    if page == "Home page":
        st.header("Home Page")
        st.write("Select Page on the the left")
        st.table(df)
        
    elif page == "Scatter Plot":
        st.header("Scatter Plot")
        visualise_scatter()
        
    elif page == "Line Plot":
        st.header("Line Plot")
        visualise_line()
        
#     elif page == "Line Chart":
#         st.header("Line Chart")
#         line_chart()

def visualise_scatter():
    sns.scatterplot(data=df,x="author",y="likes")
    st.pyplot
    
# def line_chart():
#     sns.line_chart(df[["likes"]])
#     st.pyplot
    
def visualise_line():
    sns.lineplot(x="author",y="likes",data=df)
    st.pyplot
    
if __name__=="__main__":
    main()