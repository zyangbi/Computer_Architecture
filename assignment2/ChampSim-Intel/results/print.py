import os

metrics = ["ROI_Cumulative_IPC", "ROI_LLCTOTAL_HITRATE", "ROI_LLCLOAD_HITRATE", "ROI_LLCWRITEBACK_HITRATE", "ROI_LLCAVERAGE_MISS_LATENCY"]
policies = ['lru', 'lip', 'bip', 'dip', 'ptreelru']
benchmarks = ['400.perlbench', '401.bzip2', '403.gcc', '462.libquantum', '464.h264ref', '471.omnetpp']

for metric in metrics:
    for benchmark in benchmarks:
        print(benchmark)
        for policy in policies:
            print(policy)
            file_path = os.path.join(policy, benchmark)

            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    for line in f:
                        if metric in line:
                            print(line)
        print()
        print()