#find between sepal-length and petal-length with LinearReggresion of module
#And some predict data also find r^ score 
def find_linear_regrassion(data):
  df = pd.read_csv(data)
  X = df[["sepal-length"]]
  Y = df[["petal-length"]]
  plt.scatter(X, Y)
  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=1)
  X_train = np.array(X_train).reshape(-1, 1)
  Y_test = np.array(X_test).reshape(-1, 1)
  lin = LinearRegression()
  lin.fit(X_train, Y_train)
  c = lin.intercept_
  m = lin.coef_
  Y_pred_train = m*X_test+c 
  plt.plot(Y_test, Y_pred_train, color="red")
  print(r2_score(Y_test, Y_pred_train))

find_linear_regrassion("https://storage.googleapis.com/qwasar-public/track-ds/iris.csv")
