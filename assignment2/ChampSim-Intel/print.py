import os
import csv

metrics = ['ROI_Cumulative_IPC', 'ROI_LLCTOTAL_HITRATE', 'ROI_LLCLOAD_HITRATE', 'ROI_LLCWRITEBACK_HITRATE', 'ROI_LLCAVERAGE_MISS_LATENCY']
policies = ['lru', 'lip', 'bip', 'dip', 'ptreelru']
benchmarks = ['400.perlbench', '401.bzip2', '403.gcc', '462.libquantum', '464.h264ref', '471.omnetpp']

# Create a list to store the data
data = []

for metric in metrics:
    for benchmark in benchmarks:
        benchmark_data = {
            'Metric': metric,
            'Benchmark': benchmark,
            'Values': {}
        }
        for policy in policies:
            policy_data = []

            file_path = os.path.join(policy, benchmark)

            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    for line in f:
                        if metric in line:
                            # Split the line into fields and extract the third field
                            fields = line.split()
                            if len(fields) >= 3:
                                value = fields[2]
                                policy_data.append({policy: value})

            benchmark_data['Values'][policy] = policy_data
        data.append(benchmark_data)

# Create a CSV file to store the results
csv_file_path = 'output.csv'

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Metric', 'Benchmark', 'Values'])

    for entry in data:
        metric = entry['Metric']
        benchmark = entry['Benchmark']
        values = entry['Values']

        csv_writer.writerow([metric, benchmark, values])

print(f'Results saved to {csv_file_path}')
