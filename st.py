import streamlit as st
import pandas as pd
df = pd.read_csv("top_words.txt")
st.linechart(df)