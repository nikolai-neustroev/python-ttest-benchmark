import numpy as np

np.random.seed(0)
a = np.random.randn(1_000_000)
b = np.random.randn(1_000_000)

np.save('data/data_a.npy', a)
np.save('data/data_b.npy', b)
