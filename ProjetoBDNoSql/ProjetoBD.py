import pymongo
import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("./dados.csv", encoding='unicode_escape', sep=";")

Inserts = []
for x in range(len(dados)):
    dicionario = {"_id": x+1}
    for coluna in dados:
        dicionario[f"{coluna}"] = str(dados[coluna][x])
    Inserts.append(dicionario)

cliente = pymongo.MongoClient("mongodb://localhost:27017/")

banco = cliente["Eleições-2018"]
coleção = banco["Dados"]

l = coleção.insert_many(Inserts)
print(l.inserted_ids)
print(l)

group = dados.groupby("NM_MUNICIPIO").sum()
z = group["NR_ZONA"]

x = []
y = []
for i in range(len(z)):
    y.append(z[i])

for i in range(len(Inserts)):
    if x.count(Inserts[i]["NM_MUNICIPIO"]) == 0:
        x.append(Inserts[i]["NM_MUNICIPIO"])
x = sorted(x)
print(x)


fig, ax = plt.subplots(figsize=(6,5))
c = ["#1C1C1C", "#6A5ACD", "#4B0082", "#DAA520", "#8B008B", "#008B8B", "#000080", "#DC143C", "#006400", "#FF0000", "#9932CC", "#0000FF", "#008080", "#8B4513", "#00FF00", "#000000", "#708090", "#191970", "#FFD700", "#A020F0", "#800000", "#228B22"]
wedges, texts, autotexts = ax.pie(y, autopct="%.1f%%", colors=c, textprops=dict(color="w"))
ax.legend(wedges, x, title="Municipios", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Gráfico")

plt.show()


