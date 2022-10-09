import pandas as pd
class Dataset_and_summarize_and_predict:
  def __init__(self, data, test_size, random_state):
    self.data = pd.read_csv(data)
    self.test_size = test_size
    self.random_state = random_state
  def show_data(self):
    df = self.data
    return df.head(10)
  def decribe_data(self):
    df = self.data
    return df.decribe()
  def visualization_data(self):
    df = self.data
    plt.plot(df)
  def train1_test(self):
    df = self.data
    X, Y = df.iloc[:, :4].values, df.iloc[:, 4:].values
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = self.test_size, random_state=self.random_state)
    return [X_train, X_test, Y_train, Y_test]
  def fit_data_and_predict(self):
    dctree = DecisionTreeClassifier()
    dctree.fit(Dataset_and_summarize_and_predict.train1_test(self)[0], Dataset_and_summarize_and_predict.train1_test(self)[2])
    pred = dctree.predict(Dataset_and_summarize_and_predict.train1_test(self)[1])
    return pred
  def LabelEncoder_pred_and_Y_test(self):
    le = LabelEncoder()
    predict = le.fit_transform(Dataset_and_summarize_and_predict.fit_data_and_predict(self))
    Y_test = le.fit_transform(Dataset_and_summarize_and_predict.train1_test(self)[3])
    return [predict, Y_test]
  def find_your_prediction(self, your_pred):
    dctree = DecisionTreeClassifier()
    dctree.fit(Dataset_and_summarize_and_predict.train1_test(self)[0], Dataset_and_summarize_and_predict.train1_test(self)[2])
    pred = dctree.predict(np.array(your_pred).reshape(1, -1))
    return f"Your predict: {pred}"
  def r2_score_accurancy_and_MSE(self):
    all_score = []
    num, num1 = Dataset_and_summarize_and_predict.LabelEncoder_pred_and_Y_test(self)[1], Dataset_and_summarize_and_predict.LabelEncoder_pred_and_Y_test(self)[0] 
    n, n1 = Dataset_and_summarize_and_predict.fit_data_and_predict(self), Dataset_and_summarize_and_predict.train1_test(self)[3]
    for i in range(len(Dataset_and_summarize_and_predict.fit_data_and_predict(self))):
      all_score.append(n[i] == np.array(n1).reshape(1, -1)[0][i])
    name = [i for i in np.array(all_score).reshape(1, -1)[0]]
    name2 = []
    name1 = sorted(set(name))
    for i in range(len(name1)):
      score = name.count(name1[i])
      name2.append(score)
    for i, j in zip(name1, name2):
      print(i, j)
    true_score = [name2[1]*100/sum(name2), name2[0]*100/sum(name2)]
    print(f"Accurancy: {round(true_score[0], 1)}%\nMSE: {round(true_score[1], 1)}%")
    print(f"R^ score: {round(r2_score(num, num1)*100, 1)}%")
all = Dataset_and_summarize_and_predict("https://storage.googleapis.com/qwasar-public/track-ds/iris.csv", 0.3, 10)
all.r2_score_accurancy_and_MSE()
print(all.find_your_prediction([2.3, 2.4, 1.4 , 3.4]))
