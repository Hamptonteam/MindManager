# predicting grade is on a reg scale bc we are predicting on a scale

from sklearn import linear_model
import pandas
import sklearn
import numpy
import pickle

"""student_data = pandas.read_csv("student-mat.csv", sep=";")

# shorten entry fields
student_data = student_data[["failures", "absences", "G1", "G2", "G3"]]

x = numpy.array(student_data.drop(["G3"], 1))
y = numpy.array(student_data["G3"])

xTrain, xTest, yTrain, yTest = sklearn.model_selection.train_test_split(x,y,test_size=0.1)

reg = linear_model.LinearRegression()
reg.fit(xTrain, yTrain)
score = reg.score(xTest, yTest)

high_score = 0
for i in range(1000):
    xTrain, xTest, yTrain, yTest = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
    reg = linear_model.LinearRegression()
    reg.fit(xTrain, yTrain)
    score = reg.score(xTest, yTest)
    if score > high_score:
        high_score = score
        with open("reg_algo.pickle", "wb") as f:
            pickle.dump(reg,f)
        print(score)"""

# takes trained model
reg = pickle.load(open("reg_algo.pickle", "rb"))
# format of prediction using this model
# failures, absences, past grade 1, past grade 2
print(reg.predict([[1, 0, 19, 19]]))

