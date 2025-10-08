import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
 
# Load the IRIS dataset
 
iris = datasets.load_iris();
X = iris.data
y = iris.target
 
# Create training/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=0.3, stratify=y)
 
# Feature scaling
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
 
# Fit the model with RBF kernel
svc = SVC(kernel='rbf', random_state=1, gamma=0.10, C=10.0)
svc.fit(X_train_std, y_train)
y_pred = svc.predict(X_test_std)
 
# Check the performance
print('Accuracy: %.3f' % accuracy_score(y_test, y_pred))
