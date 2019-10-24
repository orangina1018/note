import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import datasets

X = np.array([0,0.002,0.004,0.006,0.008,0.010,0.012,0.014,0.016])
Y = np.array([0.01417,0.01511,0.01498,0.01537,0.01598,0.01617,0.01789,0.01717,0.01737])

class Least_squares_method(object):

    def __init__(self, X, Y):
        self.X=X
        self.Y=Y
        #X = [0,0.002,0.004,0.006,0.010,0.012,0.014,0.016]
        #Y = [0.01414,0.01511,0.01498,0.01537,0.1598,0.01617,0.01789,0.01717,0.01737]
        #if len(X)!=len(Y):
            #raise ValueError('The dimensions of X and Y must be equal')
        self.E_X=X.mean()
        self.E_Y=Y.mean()
        self.var_X=X.var()
        self.cov=np.cov(X,Y)[0,1]
    def execute_regression(self):
        self.a=self.cov/self.var_X
        self.b=self.E_Y-self.a*self.E_X
        return self.a, self.b
    def get_R(self):
        self.RSS=0
        self.TSS=0
        for i in range(len(self.X)):
            self.RSS+=(self.Y[i]-self.a*self.X[i]-self.b)**2
            self.TSS+=(self.Y[i]-self.E_Y)**2
        self.R2=1-self.RSS/self.TSS
        return self.R2
    def plot_result(self):
        a, b=self.execute_regression()
        y=a*self.X+b
        R2=self.get_R()

        print(a)
        a = f'{a:.4g}'
        b = f'{b:.4g}'
        R2 = f'{R2:.4g}'
        print(a)
        title1 = "R^2="+ str(R2)
        title2 = "y="+ str(a)+ "x+"+str(b)
        title = title1 + "," + title2
        fig=plt.figure()
        ax=fig.add_subplot(111)
        ax.scatter(self.X, self.Y)
        ax.plot(self.X, y)
        ax.set_title(title)
        plt.xlabel('Cyclodextrin concentration (M)')
        plt.ylabel('Edaravone concentration (M)')
model1=Least_squares_method(X,Y)
model1.plot_result()
plt.show()
