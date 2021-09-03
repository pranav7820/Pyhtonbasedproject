'''import numpy as np
x=np.zeros((2,3))
print(x)


import numpy as np
x=np.full((2,3),10)
print(x)


import numpy as np
x=np.arange(2,30,2)
print(x)

import numpy as np
x=np.arange(2,300,5)
print(x)


import numpy as np
x=np.random.randint(100,201,10)
print(x)

import numpy as np
x=np.array([100,201,10])
y=np.array([700,32,120])
z=np.column_stack((x,y))
print(z)

import numpy as np
x=np.array([100,200,300])
y=np.array([300,400,500])
z=np.intersect1d(x,y)
print(z)

import numpy as np
x=np.array([100,200,300])
y=np.array([300,400,500])
z=np.setdiff1d(x,y)
print(z)

import numpy as np
x=np.array([100,200,300])
y=np.array([300,400,500])
z=np.setdiff1d(y,x)
print(z)

import numpy as np
x=np.array([100,200,300])
y=np.array([300,400,500])
z=np.sum([y,x],axis=1)
print(z)'''

import numpy as np
from numpy.core.fromnumeric import mean
x=np.random.randint(1,101,10)
z=np.std(x)
print(z)


import numpy as np
from numpy.core.fromnumeric import mean
x=np.random.randint(1,101,10)
z=np.save("mynumpy",x)
a=np.load("mynumpy.npy")
print(a)
print(z)