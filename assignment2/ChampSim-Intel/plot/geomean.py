import numpy as np

# IPC data for different workloads and policies
ipc_data = {
    '400.perlbench': {
        'lru': 0.34145,
        'lip': 0.311882,
        'bip': 0.311902,
        'dip': 0.340729,
        'ptreelru': 0.340589
    },
    '401.bzip2': {
        'lru': 0.509095,
        'lip': 0.524298,
        'bip': 0.531252,
        'dip': 0.513558,
        'ptreelru': 0.516042
    },
    '403.gcc': {
        'lru': 0.617657,
        'lip': 0.51735,
        'bip': 0.610084,
        'dip': 0.623032,
        'ptreelru': 0.614071
    },
    '462.libquantum': {
        'lru': 0.201245,
        'lip': 0.208364,
        'bip': 0.203279,
        'dip': 0.201104,
        'ptreelru': 0.201039
    },
    '464.h264ref': {
        'lru': 0.943607,
        'lip': 0.98222,
        'bip': 0.970752,
        'dip': 0.942724,
        'ptreelru': 0.946241
    },
    '471.omnetpp': {
        'lru': 0.150972,
        'lip': 0.152078,
        'bip': 0.15109,
        'dip': 0.150922,
        'ptreelru': 0.152294
    }
} 

# Define the reference policy (LRU)
reference_policy = 'lru'

# Initialize a dictionary to store IPC speedup values
ipc_speedup = {}

# Calculate IPC speedup for each policy compared to LRU
for workload, policies in ipc_data.items():
    ipc_speedup[workload] = {}
    for policy, ipc_value in policies.items():
        if policy != reference_policy:
            speedup = ipc_data[workload][reference_policy] / ipc_value
            ipc_speedup[workload][policy] = speedup

# Print IPC speedup values
for workload, policies in ipc_speedup.items():
    print(f"Workload: {workload}")
    for policy, speedup in policies.items():
        print(f"{policy} Speedup: {speedup:.4f}")
    print()


# Initialize an empty dictionary to store geometric mean speedup for each workload
geomean_speedup = {}

# Loop through each workload
for workload, policies in ipc_data.items():
    # Initialize an empty list to store speedup values for each policy
    speedup_values = []

    # Calculate speedup for each policy compared to LRU
    for policy, ipc_value in policies.items():
        lru_ipc = ipc_data[workload]['lru']
        speedup = lru_ipc / ipc_value
        speedup_values.append(speedup)

    # Calculate geometric mean speedup for the workload
    geomean = np.prod(speedup_values) ** (1 / len(speedup_values))
    geomean_speedup[workload] = geomean

# Print the geometric mean speedup for each workload
for workload, geomean in geomean_speedup.items():
    print(f"{workload} Geometric Mean Speedup: {geomean:.4f}")