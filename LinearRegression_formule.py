import numpy as np
import statistics
import matplotlib.pyplot as plt
import math
from sklearn.metrics import r2_score
import seaborn as sns
import pandas as pd
X = 4 * np.random.rand(100, 1)
y = 10 + 2 * X + np.random.randn(100, 1)
plt.scatter(X, y)
X_1 = X.reshape(1, -1)[0]
Y_1 = y.reshape(1, -1)[0]
def LinearRegressionLineFormule(X, y):
  X_mean = statistics.mean(X_1)
  Y_mean = statistics.mean(Y_1)
  all_x = [i-X_mean for i in X_1]
  all_y = [i-Y_mean for i in Y_1]
  all_xy = sum([all_x[i]*all_y[i] for i in range(len(all_x))])
  sum_squared_error_x = sum([i**2 for i in all_x])
  sum_squared_error_y = sum([i**2 for i in all_y])
  E_sum = math.sqrt(sum_squared_error_x*sum_squared_error_y)
  person_corr_score = all_xy/E_sum
  Sy = math.sqrt((sum_squared_error_y)/(len(Y_1)-1))
  Sx = math.sqrt((sum_squared_error_x)/(len(X_1)-1))
  slope_line = person_corr_score*(Sy/Sx)
  Y_intercept = Y_mean - slope_line*X_mean
  x = X_1.reshape(-1, 1)
  new = np.ones((len(X_1), 1))
  x = np.append(new, x, axis=1)
  predict_dependent_variable = np.dot(x, np.array([Y_intercept, slope_line]))
  plt.plot(X, predict_dependent_variable, color="red")
  plt.grid()
  data = {"Predict":predict_dependent_variable,
          "Y_data":Y_1}
  df = pd.DataFrame(data)
  sns.pairplot(df)
  plt.show()
  R2_score = person_corr_score**2
  R2_score2 = 1-(sum([(Y_1[i]-predict_dependent_variable[i])**2 for i in range(len(predict_dependent_variable))])/sum([(Y_1[i]-Y_mean)**2 for i in range(len(Y_1))]))
  MSE = sum([(Y_1[i]-predict_dependent_variable[i])**2 for i in range(len(predict_dependent_variable))])/len(Y_1)
  print(f'With formule: |{MSE}| <- MSE')
  print(f'With metrics: |{mean_squared_error(Y_1, predict_dependent_variable)}| <-MSE')
  print(f"With person corr score: |{round(R2_score2*100, 2)}%|  <- r2_score")
  print(f"With formule: |{round(R2_score*100, 2)}%|  <- r2_score")
  print(f"With metrics r2_score: |{round(r2_score(Y_1, predict_dependent_variable)*100, 2)}%|  <- r2_score")
# LinearRegressionLineFormule(X_1, Y_1)
def GradientDescentOptimizer(X, y):
  m = 0
  b = 0
  all = []
  learning_rate = 0.1
  iteration = 100
  for i in range(iteration):
    y_pred = b + m*X
    dm = -(2/100)*sum(X*(y-y_pred))
    db = -(2/100)*sum(y-y_pred)
    m = m - learning_rate * dm
    b = b - learning_rate * db
    print(f"Y-intercept: {b} | slope-line: {m} | iteration: {i}")
    all.append(np.append(m, b))
  plt.plot(all)
# GradientDescentOptimizer(X_1, Y_1)
