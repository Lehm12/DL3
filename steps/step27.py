import numpy as np
from dezero import *
from dezero.utils import *
import math

class Sin(Function):
    def forward(self, x):
        y = np.sin(x)
        return y

    def backward(self, gy):
        x = self.inputs[0].data
        gx = gy * np.cos(x)
        return gx

def sin(x):
    return Sin()(x)

def my_sin(x, threshoed= 0.0001):
    y = 0
    for i in range(100000):
        c = (-1) ** i / math.factorial(2*i+1)
        t = c * x ** (2*i+1)
        y = y + t
        if abs(t.data) < threshoed:
            break
    return y

x = Variable(np.array(np.pi/4))
y = my_sin(x)
y.backward()

x2 = Variable(np.array(np.pi/4))
y2 = sin(x2)
y2.backward()

print(y.data)
print(x.grad)
print(y2.data)
print(x2.grad)

x.name = 'x'
y.name = 'y'
plot_dot_graph(y, verbose=False, to_file='../graph/my_sin.png')