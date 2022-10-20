#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python37-32\python.exe
from sklearn import*
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv("spcc_mini2.csv")
#data = np.array(data)

#X = data[1:, 1:-1]
#y = data[1:, -1]
#y = y.astype('int')
#X = X.astype('int')
# print(X,y)
X_train, X_test, y_train, y_test = train_test_split(data[['sem-1','sem-2','sem-3','sem-4','sem-5']],data['Group'], test_size=0.20, random_state=0)
log_reg = LogisticRegression()


log_reg.fit(X_train, y_train)

#inputt=[int(x) for x in "45 32 60".split(' ')]
#final=[np.array(inputt)]

#b = log_reg.predict_proba(final)


pickle.dump(log_reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))


