import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

#new import
from sklearn import tree

music_data = pd.read_csv("../Desktop/Project2/music.csv")

#step2-to clean the data!
#no duplicates, but we have to div it into input(age&gender) and output(genre)
X = music_data.drop(columns = ['genre']) # will creare a new data set but wout the 'genre' column 
# X #to display the new data set
y = music_data['genre']
# y
#making a tuple to train data
#first two are inputs for test&train, last two are outputs
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2) #allocating 80% for training

#NEXT we have to create an algo that presents our model
model = DecisionTreeClassifier() #new instance of the class
model.fit(X_train, y_train) #train it (takes 2 datasets)

# joblib.dump(model, 'music-recommender.joblib')
#Now instead of dumping our model we gonna load it
# joblib.load('music-recommender.joblib')
#asking a prediction
# predictions = model.predict([[21, 1], [22, 0]]) #this method takes 2D array
predictions = model.predict(X_test)
predictions
#measure the accuracy of the model
#before doing so we have to split our data 
#one for training, and the other for testing
score = accuracy_score(y_test, predictions)
score

#new code
# music_data = pd.read_csv('music.csv')
# X = music_data.drop(columns = ['genre'])
# y = music_data['genre']

# model = DecisionTreeClassifier()
# model.fit(X, y)

# tree.export_graphviz(model, out_file = 'music-recommender.dot', 
#                      feature_names = ['age', 'gender'], 
#                      class_names = sorted(y.unique()),
#                      label = 'all', 
#                      rounded = True, 
#                      filled = True) 
