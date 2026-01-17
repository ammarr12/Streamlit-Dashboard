from Analysis_file import prodct_compar,rvnue_by_hour,Total_Revenue,df,cffe_srvd
from matplotlib import pyplot as plt
import streamlit as st
st.set_page_config(layout="wide")



col1,col2=st.columns((2,4.5), gap="large")

with col2:
    cl1,cl2=st.columns((1,4.5))
    with cl2:
        st.markdown("# Sales Perfromance By Product Type")
    st.bar_chart(prodct_compar,x="Product Category",y="Revenue",width=18,x_label=" ",y_label=" ",color="#BF092F")
    
    cl11,cl12=st.columns((1,4.5))
    with cl12:
        st.markdown("# Revenue Generated per Hour each day")
    
    st.line_chart(rvnue_by_hour,x="Hours",y="Revenue Generated",color="#BF092F")

with col1:
    st.markdown("# Actionable Insights")
    st.metric("Revenue",round(Total_Revenue,2),border=True,width="stretch")
    st.metric("Products Sold",df["product_detail"].count(),border=True,width="stretch")
    st.metric("Coffees served",cffe_srvd,border=True,width="stretch")

    st.markdown("# DataFrame Preview")
    st.dataframe(df)


    




with st.sidebar:
    st.image("logo.png",caption="Company Logo")
    
    st.markdown("### About Company")
    st.markdown("365 Coffee Cafe is a thriving coffee shop chain with three locations spread across New York City. Known for its premium coffee blends, cozy ambiance, and exceptional customer service, the cafe has become a favorite spot for locals and tourists alike. The business serves a wide range of products, including coffee, tea, pastries, sandwiches, and other snacks. With over 100,000 transactions recorded across its locations, the cafe has amassed a wealth of data that can be leveraged to optimize operations, improve customer experience, and drive revenue growth.")