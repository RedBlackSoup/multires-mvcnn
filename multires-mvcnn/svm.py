# @Time    : 2021/7/21 3:56 下午
# @Author  : Hurry Hao
# @Site    : 
# @File    : svm.py
# @Software: PyCharm
import pandas as pd
import sklearn.svm as svm


x_train_c = pd.read_csv('feather/CNN-feather.csv').drop(columns='Unnamed: 0')

x_train = x_train_c.to_numpy()
y_train_c = pd.read_csv('feather/CNN-feather-labels.csv').drop(columns='Unnamed: 0')
y_train = y_train_c.to_numpy()

x_test_c = pd.read_csv('feather/testCNN-feather.csv').drop(columns='Unnamed: 0')
x_test = x_test_c.to_numpy()
y_test_c = pd.read_csv('feather/testCNN-feather-labels.csv').drop(columns='Unnamed: 0')
y_test = y_test_c.to_numpy()

# 建立模型
clf = svm.SVC(C=0.5, kernel='linear')
print('training')
clf.fit(x_train, y_train)

train_result = clf.predict(x_train)
precision = clf.score(x_train, y_train)
print('Training precision: ', precision)

# Test on test data
test_result = clf.predict(x_test)

precision = clf.score(x_test, y_test)
print('Test precision: ', precision)

