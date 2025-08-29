import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import altair as alt
import plotly.express as px

box = st.container(border=True)          
box.markdown('# **:green[Turn-Around-Time]** **:red[Trend]**')

st.markdown('Y2025 Monthly Increase/Decrease Status')
col1, col2 = st.columns(2)

with col1:
    st.text('Line Chart')
    chart_data = pd.read_csv('TAT.csv')
    st.line_chart(chart_data, use_container_width=True)

with col2:
    st.text('Bar Chart')
    chart_data = pd.read_csv('TAT.csv')
    st.bar_chart(chart_data)




