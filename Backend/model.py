import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

#loading the data
df=pd.read_csv("iris.csv")
df2=df.copy()
print(df.head())




#selscting the independent val
X=df[["Sepal_Length","Sepal_Width","Petal_Length","Petal_Width"]]
y=df["Class"]

#splitting the val
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=10)


# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test= sc.transform(x_test)

# Instantiate the model
classifier = RandomForestClassifier()

# Fit the model
classifier.fit(X_train, y_train)

# Make pickle file of our model
pickle.dump(classifier, open("model.pkl", "wb"))