import os

metrics = ["CPU_0_Branch Prediction Accuracy", "ROI_Cumulative_IPC", "CPU_0_MPKIPERCENT", "CPU_0_Average_ROB_Occupancy_at_Mispredict"]
policies = ['perceptron', 'hashed_perceptron', '2bitcorr', 'hashed_gselect']
benchmarks = ['400.perlbench', '401.bzip2', '403.gcc', '462.libquantum', '464.h264ref.gz', '471.omnetpp.gz']

with open('output.txt', 'w') as file:
    for metric in metrics:
        for benchmark in benchmarks:
            file.write(benchmark + '\n')
            for method in policies:
                file.write(method + '\n')
                file_path = os.path.join(method, benchmark)

                if os.path.exists(file_path):
                    with open(file_path, 'r') as f:
                        for line in f:
                            if metric in line:
                                file.write(line + '\n')
            file.write('\n')
            file.write('\n')