import pandas as pd
import seaborn as sbn
data = pd.read_csv("iris.csv")
x = data[["sepal-length", "sepal-width", "petal-length", "petal-width"]].values
y = data["class"].values
color =  ["sepal-length", "sepal-width", "petal-length", "petal-width"]
for i in range(len(data.values[:4])):
  plt.scatter(x[:, i], y, label=color[i])
plt.legend()
knn = KNeighborsClassifier(n_neighbors=25)
knn.fit(x, y)
pred = knn.predict(x)
nav = input("Write fit of sepal-length sepal-width petal-length petal-width: \n").split(" ")
all = [float(i) for i in nav]
print(knn.predict(np.array([all]).reshape(1, -1)))
le = LabelEncoder()
yl, predl = le.fit_transform(y), le.fit_transform(pred)
print("R^ score: ", r2_score(yl, predl))
print("Accuracy score: ", accuracy_score(yl, predl))
plt.plot(x, pred, c="red")
plt.show()
conf = confusion_matrix(yl, predl)
ax = sbn.heatmap(conf, annot=True, cmap='Blues')
ax.set_xlabel("True data")
ax.set_ylabel("Predict data")
ax.xaxis.set_ticklabels(["Iris-setosa", "Iris-versicolor", "Iris-virginica"])
ax.yaxis.set_ticklabels(["Iris-setosa", "Iris-versicolor", "Iris-virginica"])
plt.show()
