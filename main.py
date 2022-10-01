from pandas.plotting import scatter_matrix
import plotly.express as px
import time
df = pd.read_csv("world_population.csv")
app = []
columns = []
country = data.get("Country").values
mark = data.get("CCA3").values
rank = data.get("Rank").values
area = data.get("Area (km²)").values
density = data.get("Density (per km²)").values
Growth = data.get("Growth Rate").values
persent = data.get("World Population Percentage").values
year = data.get("2022 Population").values
continent = data.get("Continent").values
for i in data.columns:
  if data.get(i).dtype == np.float64 or data.get(i).dtype == np.int64: 
    columns.append(i)
    app.append(data.get(i))
all_data_year_or_something = []
len_data = []


for j in app:
  len_data.append(len(j))
  for k in j:
    all_data_year_or_something.append(k)
num = 0
num1 = []
for l in len_data:
  num1.append(all_data_year_or_something[num:num+l])
  num+=l
opp = []
cont_ = []
mar_k = []
for o in range(len(num1)):
  if min(num1[o]) > 500:

    
    for p in range(len(num1[o])):
      opp.append(num1[o][p]/1000000)
      cont_.append(country[p])
      mar_k.append(mark[p])
    fig1 = px.choropleth(df,
                      locations=df["Country"],
                      locationmode='country names',
                      color=columns[o],
                      color_continuous_scale=px.colors.sequential.Peach,
                      template='plotly_dark',
                      title = f"{columns[o]}")
    fig1.update_layout(font = dict(size = 17, family="Franklin Gothic"))

    fig1.show()
print("\n\n") 
column = ["Area (km²)", "Density (per km²)", "Growth Rate", "World Population Percentage"]
name = [area, density, Growth, persent]
for i in range(len(name)):
  f = plt.figure()
  f.set_figwidth(100)
  f.set_figheight(30)
  plt.title(column[i], fontsize=50)
  plt.ylabel("Y_asix", fontsize=30)
  plt.xticks(np.arange(len(name[i])), cont_, rotation=90, fontsize=30)
  plt.plot(np.arange(len(name[i])), name[i], marker = 'o', ms = 10, mec = 'blue', mfc = 'r')
  plt.fill_between(np.arange(len(name[i])), name[i], color='#539ecd')
  plt.grid()
  for x,y,y1 in zip(np.arange(len(name[i])),name[i],  mar_k):

      label = f"{y1}"

      plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,20), ha='center')

  plt.show()

li = LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(np.array(persent).reshape(-1, 1), np.array(year).reshape(-1, 1), test_size=0.2 , random_state=1)
li.fit(np.array(persent).reshape(-1, 1), np.array(year).reshape(-1, 1))
plt.scatter(x_train, y_train)
predict = li.predict(x_test)
plt.plot(y_test, predict)
plt.show()
la = LabelEncoder()

continent = la.fit_transform(continent)
country = la.fit_transform(country)
knn = LinearRegression()
x_train, X_validation, y_train, Y_validation = train_test_split(np.array(country).reshape(-1, 1), np.array(continent).reshape(-1, 1), random_state=1)

knn.fit(np.array(x_train).reshape(-1, 1), y_train)
plt.scatter(x_train, y_train)
predict = knn.predict(np.array(X_validation).reshape(-1, 1))
plt.scatter(Y_validation, predict)

