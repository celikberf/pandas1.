import pandas as pd

#1- Dosya hakkındaki bilgiler
result = pd.read_csv('pandas_demo.csv')

#2- İlk 5 kaydı gösterin
df = pd.read_csv('pandas_demo.csv') 
result = pd.DataFrame.head(df)

#3- İlk 10 kaydı gösterin
result = pd.DataFrame.head(df,10)

#4- Son 5 kaydı gösterin
result = pd.DataFrame.tail(df)

#5- Son 10 kaydı gösterin
result = pd.DataFrame.tail(df,10)

#6- Sadece 1 kolon alın
result = df["en_US Monday"]

#7- Sadece 1 kolonun ilk 5 kaydını alın
result = df['en_US Monday'].head()

#8- İki kolonun da ilk 5 kaydını alın
result = df[["en_US Monday"," August 1"]].head()

#9- İki kolonun son 7 kaydını alın
result = df[["en_US Monday"," August 1"]].tail(7)

#10- iki kolonun 2-5 arası kaydını alın
result = df.iloc[2,2:5]



print(result)
