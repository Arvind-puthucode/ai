import pandas as pd
import numpy as np
from math import *
import matplotlib.pyplot as plt
dataset=[[1,0,0,0],[1,0,1,0],[1,1,0,0],[1,1,1,1]]
df = pd.DataFrame(dataset, columns = ['x0', 'x1','x2','y'])
x=df.iloc[:,:-1]
y=df.iloc[:,-1]
def sigmoid(val):
  return 1/(1+exp(-val))

w=np.array([0.1,0.5,0.5])
epoch=0
wold=np.array([0,0,0])
while(epoch==0 or not(wold==w).all()):
  epoch+=1
  yhat_c=[]
  wold=w.copy()
  for row_no in range(len(x)):
    wtx=np.dot(w,x.iloc[row_no,:])
  #  print(wtx,"wtx")
    yhat=None
    sigmx=sigmoid(wtx)
  #  print('sigmx',sigmx)
    if(sigmoid(wtx)>=0.5):
      yhat=1
    else:
      yhat=0
    yhat_c.append(yhat)
    #print('y are',yhat,y[row_no])
    if(yhat==y[row_no]):
      pass
    else:
   #   print('hi inside')
      w=w+0.1*(y[row_no]-sigmx)*np.array(x.iloc[row_no,:])
    print('w after each updation is',w)
    x1=x.iloc[:,1]
    x2=x.iloc[:,2]
    print(x1,x2)
   # cdict = {1: 'red', 2: 'blue'}
    print('yhat',yhat_c)
  
  #  plt.scatter(x1,x2,c=yhat_c,label=yhat_c)
  #  plt.legend()
  #  plt.plot(range(0,1.0,st),range(0,1,0.1))
print('final weight',w)
print('number of epochs are',epoch)

