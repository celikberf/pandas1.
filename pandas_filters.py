import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns = ["Column1","Column2","Column3","Column4","Column5",])

result = df
result = df.columns # kolon bilgileri
result = df.head() # ilk 5 kayıt gelir(satır)
result = df.head(10) # ilk 10 kayıt geldi
result = df.tail() # son 5 kayıt
result = df.tail(10) # son 10 kayıt
result = df["Column1"].head()  # column1 in ilk 5 kaydı
result = df.Column1.head() # bir üsttekiyle aynı
result = df[["Column1","Column2"]].head() #Column1 ve 2 kayıtların ilk 5 kaydı gelcek
result = df[5:15][["Column1","Column2"]].head() # 5-9 arası kayıtları aldık
result = df[5:15][["Column1","Column2"]].tail() # 10-14 arası kayıtları aldık

result = df > 50  # 50den büyükler true false şeklinde gelir
result = df[df > 50] # koşula uymayan kayıtları NaN verir
result = df[df % 2 == 0] # koşula uymayan kayıtları NaN verir
result = df["Column1"] > 50 # sadece column1 için 50den büyükleri getirir
result = df[df["Column1"] > 50][["Column1","Column2"]]
result = df[(df["Column1"] > 50) & (df["Column1"] <= 70)] # 50den büyük ve 70ten küçük
result = df[(df["Column1"] > 50) | (df["Column1"] <= 70)] # 50den büyük veya 70ten küçük
result = df.query("Column1 >= 50 & Column1 %2 == 0")[["Column1","Column2"]]
result = df.query("Column1 >= 50 | Column1 %2 == 0")[["Column1","Column2"]]


print(result)