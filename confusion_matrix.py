data = pd.read_csv("https://storage.googleapis.com/qwasar-public/track-ds/iris.csv")
all12 = data
le = LabelEncoder()

for i in range(len(data.iloc[0])):
  data.iloc[:, i] = le.fit_transform(data.iloc[:, i])
all = []
for i in data.values:
  all.append(i)
all1 = []
all2 = []
for i in range(len(all)):
  all1.append(statistics.mean(np.array(all[i])))
  all2.append(statistics.median(np.array(all[i])))
np1 = np.array(all1) 
np2 = np.array(all2)
plt.plot(np1)
plt.show()
plt.plot(np2)
plt.show()
X_train, X_test, y_train, y_test = train_test_split(np1, np2, test_size=0.9, random_state=1)
fig, ax = plt.subplots()

ax.plot(X_train)
ax.plot(y_train)
plt.show()


plt.plot(confusion_matrix(X_train, y_train))
plt.show()
all = []
for i in data.values:
  all.append(i)
plt.plot(np.array(all))
plt.show()
plt.scatter(np1, np2, c=np1)
plt.colorbar()
plt.show()
a = []
b = []
for j in range(len(X_train)):
  a.append(int(X_train[j]))
  b.append(int(y_train[j]))
c, d = np.array(a), np.array(b)
re_s = []
for i in recall_score(c, d, average=None):
  name22 = int(i)
  if i > 0:
    name2 = name22+1-i
    re_s.append(int(i+name2))
  else:
    re_s.append(int(i))
f1_s = []
for i in f1_score(c, d, average=None):
  name11 = int(i)
  if i > 0.0:
    name1 = name11+1-i
    f1_s.append(int(i+name1))
  else:
    f1_s.append(int(i))

print(confusion_matrix(f1_s, re_s))
print("confusion_matrix: -> ", confusion_matrix(c, d))
print("r2_score: -> ", r2_score(c, d))
print("accuracy_score: -> ", accuracy_score(c, d))
print("mean_absolute_error: -> ", mean_absolute_error(c, d))
print("mean_squared_error: -> ", mean_squared_error(c, d))
print("f1_score: -> \n", f1_score(c, d, average=None))
print("recall_score: -> \n", recall_score(c, d, average=None))
