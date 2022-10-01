import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, confusion_matrix, accuracy_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder
def my_model_evaluation_journey_r2_score(param_1, param_2):
  name0 = int(input("""
                SEE TABLE 
                1 -- Visualitions
                2 -- matrics
                3 -- train_test_split
                What kind of things do you want:
                """))
  df = pd.read_csv(StringIO(param_1)).values
  df2 = pd.read_csv(StringIO(param_1)).values
  le = LabelEncoder()
  for i in range(len(df[0])):
    df[:, i] = le.fit_transform(df[:, i])
    df2[:, i] = le.fit_transform(df2[:, i])
  all = []
  all2 = []
  for j in range(len(df)):
    all.append(df[j])
    all2.append(df2[j])
  x = np.array(all)
  y = np.array(all2)
  if name0 == 3:
    name_t = input("""
                  Things: x_train, x_test, y_train, y_test
                  What kind things, do you want write
                  """)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    if name_t == "x_train":
      # for i in range(len(x_train)):
      #   x_t1.append([j for j in range(len(x_train[i]))])
      plt.hist(x_train)
      plt.show()
    elif name_t == "x_test":
      plt.hist(x_test)
      plt.show()
    elif name_t == "y_train":
      plt.hist(y_train)
      plt.show()
    elif name_t == "y_test":
      plt.hist(y_test)
      plt.show()
  elif name0 == 1:
      plt.plot(x)
      plt.title("X data")
      plt.xlabel("X_values")
      plt.ylabel("Columns")
      plt.show()
      plt.plot(y)
      plt.title("Y data")
      plt.xlabel("X_values")
      plt.ylabel("Columns")
      plt.show()
      plt.scatter(x, y)
      plt.xlabel("First data")
      plt.ylabel("Second data")
      plt.show()
  else:
      act = []
      act1 = []
      for i in range(len(x)):
        for j in range(len(x[i])):
          act.append(x[i][j])
          act1.append(y[i][j])
      x1 = np.array(act)
      y1 = np.array(act1)
      name = input("What kind of matrics do you want :")
      if name == "r2_score":
        return "r2_score: {}".format(r2_score(x, y))
      elif name == "mean_absolute_error":
        return "mean_absolute_error: {}".format(mean_absolute_error(x, y))
      elif name == "mean_squared_error":
        return "mean_squared_error: {}".format(mean_squared_error(x, y))
      elif name == "confusion_matrix":
        plt.plot(confusion_matrix(x1, y1))
        plt.show()
        return "confusion_matrix: \n{}".format(confusion_matrix(x1, y1))
      elif name == "accuracy_score":
        return "accuracy_score: {}".format(accuracy_score(x1, y1))
      elif name == "recall_score":
        return "recall_score: {}".format(recall_score(x1, y1, average=None))
      elif name == "f1_score":
        return "f1_score: {}".format(f1_score(x1, y1, average=None))
      else:
        return "You type wrong matrics"

print(my_model_evaluation_journey_r2_score("robot_model_name,nbr_pieces_head,nbr_pieces_arms,nbr_pieces_legs,nbr_pieces_body\nda Vinci Surgical System,4377,47000,97969,37320\nKITT,90043,73282,18868,45540\nThe Tachikomas,2114,68111,75162,36340\nToyota violin-playing,63098,85704,78717,57345\nGERTY,81519,26677,65519,43420\nMega Man,27814,9740,12137,26380\nRock \u2018Em Sock \u2018Em Robots,876,67,581,5460\nDoraemon,16788,85783,86233,47200\nAwesom-O,7448,54163,33401,23740\nHK-47,46131,58449,92296,49200\nED-209,77228,10734,54545,35720\nBeer-Fetching Robot,59627,81878,23861,41340\nBishop,96414,66998,4115,41880\nThe Energizer Bunny,68804,14932,37880,30400\nH.E.L.P.eR.,78159,8060,63274,37360\nClank,11578,84323,86292,45540\n", "robot_model_name,nbr_pieces_head,nbr_pieces_arms,nbr_pieces_legs,nbr_pieces_body\nClank,43973,25595,58504,32000\nDaft Punk,96371,61676,31481,47380\nJohnny 5,66511,38385,47953,38200\nThe Robot,58752,89090,51497,49820\nMr. Roboto,94246,12826,78777,45480\nMarvin the Paranoid Android,53874,16704,21492,23000\nLego Mindstorms NXT,483,48426,29257,19540\nRobbie,22657,2013,75082,24920\nAstro Boy,34499,33062,86296,38460\nThe Iron Giant,57496,90149,29823,44360\nOptimus Prime,13205,4869,76120,23540\nRoomba,22875,32377,76437,32920\nDJ Roomba,68704,8287,77907,38720\nCindi Mayweather,17690,41995,68166,309940\nMark Z,85325,88067,64264,59400\nRosie,83044,74974,41489,49860\nCrow T. Robot/Tom Servo,96983,26930,21595,36360\nK-9,35898,69605,83592,47260\nThe Terminator,65268,47748,50964,40980\nThe Maschinenmensch,10278,91180,46682,37020\nASIMO,4955,37023,59065,25260\nGLaDOS,59036,20960,26556,26620\nThe Final Five,83686,87654,71010,50320\nSojourner,56273,199,31862,22080\nData,86581,27309,21246,33780\nR2D2,45064,59797,37373,35540\nBender Bending Rodriguez,61198,51705,13208,31520\nWall-E,66709,19032,72116,39460"))
