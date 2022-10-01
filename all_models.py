from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics
from io import StringIO
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import multilabel_confusion_matrix,  confusion_matrix, r2_score, accuracy_score, mean_absolute_error, mean_squared_error, f1_score, recall_score
