from math import sqrt as rq   #importa a raiz quadrada
import pandas as pd                     #importa a biblioteca pandas para analisar nossos dados

up = pd.read_csv("z1.csv")             #importa as medições com o celular para cima
down = pd.read_csv("z2.csv")         #importa as medições com o celular para baixo
lat1 = pd.read_csv("x1.csv")
lat2 = pd.read_csv("x2.csv")
verlat1 = pd.read_csv("y1.csv")
verlat2 = pd.read_csv("y2.csv")

#bx
print("medias componentes bx")
print(up["Bx"].mean())
print(down["Bx"].mean())
print(lat1["Bx"].mean())
print(lat2["Bx"].mean())
print(verlat1["Bx"].mean())
print(verlat2["Bx"].mean())


#by
print("medias componentes by")
print(up["By"].mean())
print(down["By"].mean())
print(lat1["By"].mean())
print(lat2["By"].mean())
print(verlat1["By"].mean())
print(verlat2["By"].mean())

#by
print("medias componentes bt")
print(up["BT"].mean())
print(down["BT"].mean())
print(lat1["BT"].mean())
print(lat2["BT"].mean())
print(verlat1["BT"].mean())
print(verlat2["BT"].mean())



#de acordo com o paper do relatorio, temos o seguinte:
vertbx = (abs(up["Bx"].mean())+abs(down["Bx"].mean()))/2
lateralbx = (abs(lat1["Bx"].mean()) +      abs(lat2["Bx"].mean()))/2
verlatbx= (abs(verlat1["Bx"].mean())+abs(verlat2["Bx"].mean()))/2
mediabx = (vertbx+verlatbx+lateralbx)/3
vertby = (abs(up["By"].mean())+abs(down["By"].mean()))/2
lateralby = (abs(lat1["By"].mean())+abs(lat2["By"].mean()))/2
verlatby = (abs(verlat1["By"].mean())+abs(verlat2["By"].mean()))/2
mediaby = (vertby+verlatby+lateralby)/3
vertbt = (abs(up["BT"].mean())+abs(down["BT"].mean()))/2
lateralbt = (abs(lat1["BT"].mean())+abs(lat2["BT"].mean()))/2
verlatbt = (abs(verlat1["BT"].mean())+abs(verlat2["BT"].mean()))/2
mediabt = (vertbt+verlatbt+lateralbt)/3

print("******************************")
print(format(vertbx, ".2f"))
print(format(vertby, ".2f"))
print(format(vertbt, ".2f"))
print("******************************")
print(format(lateralbx, ".2f"))
print(format(lateralby, ".2f"))
print(format(lateralbt, ".2f"))
print("******************************")
print(format(verlatbx, ".2f"))
print(format(verlatby, ".2f"))
print(format(verlatbt, ".2f"))
print("******************************")

#e se queremos a componente horizontal media:
horzmd = rq((mediabx**2) + (mediaby**2))

print("a componente horizontal do campo é:", format(horzmd, ".2f"))
print("a componente total do campo é", format(mediabt, ".2f"))
