import numpy as np

a = np.array([1, 2, 3])



for i in a:

    i=i*2

print(a)  # Output will be [1 2 3] because 'i' is a copy of each element, not a reference    