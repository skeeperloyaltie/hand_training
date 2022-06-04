# apply three classifiers and compare performances
# hand gesture application 
# hand gesture recognition app 
import csv
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd


def read_csv(filename):
    with open(filename, 'r') as f:
        reader = pd.read_csv(f)
    return reader

def get_data(data):
    return data.head()

def divide_data(data):
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    # train_test_split = int(len(data) * 0.8)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    return X_train, X_test, y_train, y_test

def classifier(divide_data):
    class1 = LogisticRegression()
    X_train = divide_data[0]
    y_train = divide_data[1]
    X_test = divide_data[2]
    y_test = divide_data[3]
    return class1.fit(X_train, X_test)



def main():
    data = read_csv('sign.csv')
    classification = divide_data(data)
    classify1 = classifier(classification)
    print(classify1)
    
    # knn neighbors
    
    knn_model = KNeighborsClassifier(n_neighbors=5)
    # SVC_model 
    SVC_model = SVC(kernel='linear', C=1.0)
    
    print(knn_model)
if __name__ == '__main__':
    main()
    

