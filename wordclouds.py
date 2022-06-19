import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter
from wordcloud import WordCloud


data = pd.read_csv("data_chocolate.csv")
data = data.drop(index=1)
data = data.dropna()


big_comps = [row["Company"] for i, row in data.iterrows()]
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


wordcloud = WordCloud(background_color="white", contour_width=0.1,
                      contour_color="black",  max_font_size=150, random_state=42,
                      colormap="Dark2")


#wordclouds for characteristics of the same 4 big and 4 small companies
char = {k: [] for k in list(little5_d.keys())}
for k, v in char.items():
    for i, row in data.iterrows():
        if k == row["Company"]:
            v.append(row["MostMemorableCharacteristics"])
char2 = {k: " ".join(v).replace(",", "") for k, v in char.items()}
for i in range(4):
    wordcloud.generate(text=list(char2.values())[i])
    plt.subplot(2, 2, i + 1)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
plt.show()


char3 = {k: [] for k in list(top5_d.keys())}
for k, v in char3.items():
    for i, row in data.iterrows():
        if k == row["Company"]:
            v.append(row["MostMemorableCharacteristics"])
char4 = {k: " ".join(v).replace(",", "") for k, v in char3.items()}
for i in range(4):
    wordcloud.generate(text=list(char4.values())[i])
    plt.subplot(2, 2, i + 1)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
plt.show()
