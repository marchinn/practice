import numpy as np

def result(s):
    if sigmoid(s)>=b:
        return True
    else:
        return False

def sigmoid(s):
    return 1/(1+np.exp(-s))
    
class Neuron:
    def __init__(self,w):
        self.w = w

    def y(self,x):
        s=np.dot(self.w,x)
        return result(s)

Xi=np.array([int(i) for i in list(input('please enter input values: '))])
Wi=np.array([int(i) for i in list(input('now enter weight values: '))])
b=float(input('enter threshold value from 0 to 1: '))
n=Neuron(Wi)
print(n.y(Xi))
    