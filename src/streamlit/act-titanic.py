import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

st.title('Esto es un título!')
st.header('Esto es un header!')
st.markdown('*italick')

df=pd.read_csv("train.csv")
st.dataframe(df)

dffirstclass = df[df['Pclass']==1]
dffirstclass

dfsecondclass = df[df['Pclass']==2]
dfsecondclass

dfthirdclass = df[df['Pclass']==3]
dfthirdclass
