import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('titanic.csv')

df_pro=df[['Survived','Age','Sex']]

df_pro['Age'].fillna(df_pro['Age'].median(), inplace=True)

num_personas=len(df)
personas_sobrevivientes=df_pro['Survived'].sum()

df_pro['Sex'].unique()

df_pro_mujeres=df_pro[df_pro['Sex']=='female']
num_mujeres=len(df_pro_mujeres)
plt.hist(df_pro_mujeres['Survived'], density=True)

