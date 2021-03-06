import numpy as np

from sklearn import model_selection
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# step 1 is load data
# step 2 is choose a fitting algorithm
# step 3 calculate metrics 
# step 4 predict values

# load training data
trainDataFile = '..\\data\\train.csv'
rawDataId = open(trainDataFile);
dataset = np.loadtxt(rawDataId, delimiter=',', skiprows=1)
X = dataset[:,2:5]
Y = dataset[:,5]

testElementCount = 1000
totalElementCount = Y.size
trainElementCount = totalElements - testElementCount
train_X = X[0:trainElementCount,:]
train_Y = Y[0:trainElementCount]
test_X = X[trainElementCount:,:]
test_Y = Y[trainElementCount:]
rawDataId.close()

# classification models
models = []
#models.append(('LDA', LinearDiscriminantAnalysis()))
#models.append(('KNN', KNeighborsClassifier()))
#models.append(('CART', DecisionTreeClassifier()))
#models.append(('NB', GaussianNB()))
#models.append(('LR', LogisticRegression()))
models.append(('SVM', SVC()))

for name, model in models:
	model.fit(train_X, train_Y)
	test_predicted_Y = model.predict(test_X)
	print(metrics.classification_report(test_Y,test_predicted_Y))
	print(metrics.confusion_matrix(test_Y,test_predicted_Y))



seed = 7
scoring = 'accuracy'

results = []
names = []

for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)

testDataFile = '..\\data\\test.csv'
rawDataId = open(testDataFile)
dataset = np.loadtxt(rawDataId, delimiter=',', skiprows=1)
predict_X = dataset[:,2:5]
rawDataId.close()