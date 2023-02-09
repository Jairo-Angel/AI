import numpy as np 
from matplotlib import pyplot



def funcion(x)->int:
    return np.cos(x)
def plot():
    limites= np.asarray([[-30.0,30.0]])
    x_inputs = np.arange(limites[0,0],limites[0,1],0.1)
    y_inputs = [funcion(x) for x in x_inputs]
    pyplot.plot(x_inputs, y_inputs,'--')
    pyplot.show()  
