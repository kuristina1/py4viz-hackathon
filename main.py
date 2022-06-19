import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter
import plotly.express as px
import plotly.graph_objects as go


data = pd.read_csv("data_chocolate.csv")
data = data.drop(index=1)
data = data.dropna()

# OVERVIEW PART

#number of companies in each country (we have 60 countries)
big_comps = [row["Company"] for i, row in data.iterrows()]
num_comp = [row["CompanyLocation"] for i, row in data.iterrows()]
num_comp2 = list(set(num_comp))
d_comp = {country: [] for country in num_comp2}
for k, v in d_comp.items():
    for i, row in data.iterrows():
        if k == row["CompanyLocation"]:
            v.append(row["Company"])
d_comp2 = {k: len(set(v)) for k, v in d_comp.items()}
d_comp_sort = dict(sorted(d_comp2.items(), key=lambda item: item[1]))
d = {"Country" : list(d_comp_sort.keys())[-9:], "numofcomp" : list(d_comp_sort.values())[-9:]}
d2 = pd.DataFrame(d)
fig = px.bar(d2, x='Country', y='numofcomp',
             hover_data=['numofcomp'], color='numofcomp',
             labels={'numofcomp':'Top 10 manufacturers'}, height=400)
#fig.show()
#fig.write_image("top10manufacturers.pdf")


# rating change over the years for the 4 biggest and 4 smallest companies all over the world
big_comps2 = dict(sorted(dict(Counter(big_comps)).items(), key=lambda item: item[1]))
little5 = [k for k, v in big_comps2.items() if int(v) > 10 and int(v) < 25][:4]
top5 = list(big_comps2.keys())[-4:]

little5_d = {i: [] for i in little5}
top5_d = {i: [] for i in top5}
for k, v in little5_d.items():
    dictio1 = {}
    for i, row in data.iterrows():
        if k == row["Company"]:
            dictio1[row["ReviewDate"]] = row["Rating"]
            v.append(dictio1)

for k, v in top5_d.items():
    dictio2 = {}
    for i, row in data.iterrows():
        if k == row["Company"]:
            dictio2[row["ReviewDate"]] = row["Rating"]
            v.append(dictio2)

#smallest 4
plt.figure(figsize=(18, 15))
plt.subplot(2, 2, 1)
plt.plot([int(i) for i in list(little5_d["Madre"][0].keys())],
         list(little5_d["Madre"][0].values()), marker="o")
plt.xlabel("Years")
plt.ylabel("Rating")
plt.title("Madre")

plt.subplot(2, 2, 2)
plt.plot([int(i) for i in list(little5_d["Altus aka Cao Artisan"][0].keys())],
         list(little5_d["Altus aka Cao Artisan"][0].values()), marker="o")
plt.xlabel("Years")
plt.ylabel("Rating")
plt.title("Altus aka Cao Artisan")

plt.subplot(2, 2, 3)
plt.plot([int(i) for i in list(little5_d["Brasstown aka It's Chocolate"][0].keys())],
         list(little5_d["Brasstown aka It's Chocolate"][0].values()), marker="o")
plt.xlabel("Years")
plt.ylabel("Rating")
plt.title("Brasstown aka It's Chocolate")

plt.subplot(2, 2, 4)
plt.plot([int(i) for i in list(little5_d["French Broad"][0].keys())],
         list(little5_d["French Broad"][0].values()), marker="o")
plt.xlabel("Years")
plt.ylabel("Rating")
plt.title("French Broad")
#plt.show()

#biggest 4
plt.figure(figsize=(18, 15))
plt.subplot(2, 2, 1)
plt.plot([int(i) for i in list(top5_d["Arete"][0].keys())],
         list(top5_d["Arete"][0].values()), marker="o", color="red")
plt.xlabel("Years")
plt.ylabel("Rating")
plt.title("Arete")

plt.subplot(2, 2, 2)
plt.plot([int(i) for i in list(top5_d["Fresco"][0].keys())],
         list(top5_d["Fresco"][0].values()), marker="o", color="red")
plt.xlabel("Years")
plt.ylabel("Rating")
plt.title("Fresco")

plt.subplot(2, 2, 3)
plt.plot([int(i) for i in list(top5_d["Bonnat"][0].keys())],
         list(top5_d["Bonnat"][0].values()), marker="o", color="red")
plt.xlabel("Years")
plt.ylabel("Rating")
plt.title("Bonnat")

plt.subplot(2, 2, 4)
plt.plot([int(i) for i in list(top5_d["Soma"][0].keys())],
         list(top5_d["Soma"][0].values()), marker="o", color="red")
plt.xlabel("Years")
plt.ylabel("Rating")
plt.title("Soma")
#plt.show()


#Bean dealers (how many bars are made of beans from a given country)
num_deal = [row["Broad BeanOrigin"] for i, row in data.iterrows()]
num_deal2 = dict(Counter(num_deal).most_common(10))
num_deal_sort = dict(sorted(num_deal2.items(), key=lambda item: item[1]))
fig2 = go.Figure(go.Bar(
            x=list(num_deal_sort.values()),
            y=list(num_deal_sort.keys()),
            orientation='h'))

#fig2.show()
#fig2.write_image("top10dealers.pdf")


#how many different bars a country has
bars = dict(sorted({k: len(v) for k, v in d_comp.items()}.items(), key=lambda item: item[1]))
bars2 = {"Country" : list(bars.keys())[-9:], "numofbars" : list(bars.values())[-9:]}
bars_df = pd.DataFrame(bars2)
fig3 = px.bar(bars_df, x='Country', y='numofbars',
             hover_data=['numofbars'], color='numofbars',
             labels={'numofbars':'Top 10 countries by variety of chocolate bars'}, height=400)
#fig3.show()
#fig3.write_image("top10bars.pdf")


