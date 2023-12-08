import numpy as np

# IPC data for different benchmarks and methods
ipc_data = {
    '400.perlbench': {
        'hashed_perceptron': 0.34145,
        '2bitcorr': 0.335436,
        'hashed_gselect': 0.335817,
    },
    '401.bzip2': {
        'hashed_perceptron': 0.509095,
        '2bitcorr': 0.485223,
        'hashed_gselect': 0.486841,
    },
    '403.gcc': {
        'hashed_perceptron': 0.617657,
        '2bitcorr': 0.479714,
        'hashed_gselect': 0.456031,
    },
    '462.libquantum': {
        'hashed_perceptron': 0.201245,
        '2bitcorr': 0.180431,
        'hashed_gselect': 0.177896,
    },
    '464.h264ref.gz': {
        'hashed_perceptron': 0.943607,
        '2bitcorr': 0.832741,
        'hashed_gselect': 0.868695,
    },
    '471.omnetpp.gz': {
        'hashed_perceptron': 0.150972,
        '2bitcorr': 0.145044,
        'hashed_gselect': 0.144966,
    }
}

# Calculate the geometric mean speedup over all benchmarks
geomean_speedup_2bitcorr = 1.0
geomean_speedup_hashed_gselect = 1.0
count = 0

for benchmark in ipc_data:
    perceptron_ipc = ipc_data[benchmark]['hashed_perceptron']
    geomean_speedup_2bitcorr *= ipc_data[benchmark]['2bitcorr'] / perceptron_ipc
    geomean_speedup_hashed_gselect *= ipc_data[benchmark]['hashed_gselect'] / perceptron_ipc
    count += 1

# Calculate the geometric mean
geomean_speedup_2bitcorr = np.power(geomean_speedup_2bitcorr, 1.0 / count)
geomean_speedup_hashed_gselect = np.power(geomean_speedup_hashed_gselect, 1.0 / count)

# Print the geometric mean speedup for 2bitcorr and hashed_gselect
print(f'Geometric Mean Speedup (2bitcorr vs. hashed_perceptron): {geomean_speedup_2bitcorr:.4f}')
print(f'Geometric Mean Speedup (hashed_gselect vs. hashed_perceptron): {geomean_speedup_hashed_gselect:.4f}')
