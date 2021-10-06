#ELISH PATEL (180110120030)
import numpy as np
import matplotlib.pyplot as plt
import math

def idnetity_function(x):
  return 

def linear_function(x):
  return  

def binary_step(x):
  
def bipolar_step(x):
  
def bell_shaped(x):
  mean = np.mean(x)
  std = np.std(x)
  y_out = 1 / (std * np.sqrt(2 * np.pi)) * np.exp(- (x * mean) ** 2 / (2  std *2))
  return y_out

x = np.linspace(-10, 10)
plt.plot(x, bell_shaped(x))
 plt.axis('tight')
  plot.title('Activation Function :Bell Shaped')
  plt.title("Elish",loc='right',rotation=45)
  plt.show()
