import matplotlib.pyplot as py
import seaborn as sb
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import dill as pickle

def get_data_sets():
  df = sb.load_dataset('tips')
  df.replace({ 'sex': {'Male':0 , 'Female':1} , 'smoker' : {'No': 0 , 'Yes': 1}} ,inplace=True)
  days = pd.get_dummies(df['day'],drop_first=True)
  df = pd.concat([df,days],axis=1)
  times = pd.get_dummies(df['time'],drop_first=True)
  df = pd.concat([df,times],axis=1)
  df.drop(['day','time'],inplace=True,axis=1)
  X = df[['sex','smoker','size','Fri','Sat','Sun','Dinner']]
  Y = df[['tip']]
  return train_test_split(X,Y,test_size=0.25,random_state=26)

def train(model, X_train, y_train):
  model.fit(X_train, y_train)
  return True

def test(model, X_test, y_test):
  # y_pred = model.predict(X_test)
  return model.score(X_test, y_test)

def predict(model, sample):
  myvals = np.array(sample).reshape(1,-1)
  print(myvals)
  return model.predict(myvals)[0].tolist()[0]

def create_model():
  return LinearRegression()

def save_model(model,id):
  filename = f'{id}.pk'
  with open('./'+filename, 'wb') as file:
	  return pickle.dump(model, file)


def load_model(id):
  filename = f'{id}.pk'
  with open('./'+filename ,'rb') as f:
    return pickle.load(f)
