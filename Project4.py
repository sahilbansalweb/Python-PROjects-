"""
|---------------------------------------------<  MINI PROJECT => 4  >--------------------------------------------------\
|------------------------------------<  Generating a sine vs cosine curve  >-------------------------------------------\
"""
from matplotlib import pyplot as plt
import numpy

x = numpy.arange(-2*numpy.pi, 2*numpy.pi, 0.001)
y=numpy.sin(x)
z=numpy.cos(x)
plt.plot(x,y,x,z)
plt.show()
