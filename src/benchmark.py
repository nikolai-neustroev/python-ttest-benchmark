import time
import csv
from tqdm import tqdm

import numpy as np
from scipy import stats

a = np.load('data/data_a.npy')
b = np.load('data/data_b.npy')

runtimes = []

for _ in tqdm(range(10000), desc="Running t-tests"):
    start_time = time.perf_counter()
    t_stat, p_value = stats.ttest_ind(a, b, equal_var=False)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    runtimes.append(elapsed_time)

print(f"Python t-statistic: {t_stat:.4f}, p-value: {p_value:.4f}")
print(f"Python last execution time: {elapsed_time:.6f} seconds")

with open('python_runtimes.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['runtime'])
    for runtime in runtimes:
        writer.writerow([runtime])
