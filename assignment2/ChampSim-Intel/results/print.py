import os

# directories = ['lru', 'lip', 'bip', 'dip']
directories = ['lru', 'dip', 'ptreelru']
files = ['400.perlbench', '401.bzip2', '403.gcc', '462.libquantum', '464.h264ref', '471.omnetpp']

for file in files:
    print(file)
    for directory in directories:
        print(directory)
        file_path = os.path.join(directory, file)

        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                for line in f:
                    # if "ROI_LLCTOTAL_HITRATE" in line:
                    if "ROI_Cumulative_IPC" in line:
                        print(line)
    print()
    print()
