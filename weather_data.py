# -*- coding: utf-8 -*-
"""Weather_Data

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Oamsb3KJPr9YlAkgosCrajz0lSldLYc4
"""

import pandas as pd

df=pd.read_csv("/content/drive/MyDrive/Python/weatherHistory.csv")
df

df.head()

df.shape

df.index

df.columns

df.dtypes

df["Temperature (C)"].unique()

df["Temperature (C)"].nunique()

df.count

df["Summary"].value_counts

df.info()

df.head(3)

df['Wind Speed (km/h)'].unique()

df["Wind Speed (km/h)"].nunique()

df.groupby("Daily Summary").get_group("Partly cloudy throughout the day.")

df[df["Wind Speed (km/h)"]==14.1197]

df.isna().sum()

df.rename(columns={"Temperature (C)":"Temperature"},inplace=True)

df

df.Temperature.mean()

df.Temperature.std()

df["Humidity"].var()

df[df["Summary"]=="Mostly Cloudy"]

df[(df["Temperature"]>9.377778)&(df["Wind Speed (km/h)"]==8.5169	)]

df.rename(columns={"Visibility (km)":"visibility"})

df.groupby("Visibility (km)").mean()

df.groupby("Visibility (km)").max()

df[df["Summary"]=="Rain"]

df[(df["Summary"]=="Foggy")|(df["Humidity"]>0.43)]

df[(df["Precip Type"]=="rain")&(df["Wind Speed (km/h)"]>4.2826)|(df["Visibility (km)"]>14.9569)]