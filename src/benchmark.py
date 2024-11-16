import time

import numpy as np
from scipy import stats

a = np.load('data/data_a.npy')
b = np.load('data/data_b.npy')

start_time = time.perf_counter()
t_stat, p_value = stats.ttest_ind(a, b, equal_var=False)
end_time = time.perf_counter()

elapsed_time = end_time - start_time

print(f"Python t-statistic: {t_stat:.4f}, p-value: {p_value:.4f}")
print(f"Python execution time: {elapsed_time:.6f} seconds")
