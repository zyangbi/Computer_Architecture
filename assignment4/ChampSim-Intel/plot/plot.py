import matplotlib.pyplot as plt
import numpy as np

data = {
    'CPU_0_Branch Prediction Accuracy': {
        '400.perlbench': {
            'hashed_perceptron': 99.6977,
            '2bitcorr': 99.4604,
            'hashed_gselect': 99.3878
        },
        '401.bzip2': {
            'hashed_perceptron': 93.6257,
            '2bitcorr': 91.5915,
            'hashed_gselect': 91.786
        },
        '403.gcc': {
            'hashed_perceptron': 99.4345,
            '2bitcorr': 94.1533,
            'hashed_gselect': 93.0185
        },
        '462.libquantum': {
            'hashed_perceptron': 99.9987,
            '2bitcorr': 96.3061,
            'hashed_gselect': 95.9556
        },
        '464.h264ref.gz': {
            'hashed_perceptron': 98.7394,
            '2bitcorr': 94.0272,
            'hashed_gselect': 95.1154
        },
        '471.omnetpp.gz': {
            'hashed_perceptron': 98.6049,
            '2bitcorr': 95.0628,
            'hashed_gselect': 95.2244
        }
    },
    'ROI_Cumulative_IPC': {
        '400.perlbench': {
            'hashed_perceptron': 0.34145,
            '2bitcorr': 0.335436,
            'hashed_gselect': 0.335817
        },
        '401.bzip2': {
            'hashed_perceptron': 0.509095,
            '2bitcorr': 0.485223,
            'hashed_gselect': 0.486841
        },
        '403.gcc': {
            'hashed_perceptron': 0.617657,
            '2bitcorr': 0.479714,
            'hashed_gselect': 0.456031
        },
        '462.libquantum': {
            'hashed_perceptron': 0.201245,
            '2bitcorr': 0.180431,
            'hashed_gselect': 0.177896
        },
        '464.h264ref.gz': {
            'hashed_perceptron': 0.943607,
            '2bitcorr': 0.832741,
            'hashed_gselect': 0.868695
        },
        '471.omnetpp.gz': {
            'hashed_perceptron': 0.150972,
            '2bitcorr': 0.145044,
            'hashed_gselect': 0.144966
        }
    },
    'CPU_0_MPKIPERCENT': {
        '400.perlbench': {
            'hashed_perceptron': 0.645038,
            '2bitcorr': 1.15116,
            'hashed_gselect': 1.30605
        },
        '401.bzip2': {
            'hashed_perceptron': 11.2101,
            '2bitcorr': 14.9033,
            'hashed_gselect': 14.4837
        },
        '403.gcc': {
            'hashed_perceptron': 1.22667,
            '2bitcorr': 12.6828,
            'hashed_gselect': 15.1452
        },
        '462.libquantum': {
            'hashed_perceptron': 0.0023872,
            '2bitcorr': 6.63548,
            'hashed_gselect': 7.26509
        },
        '464.h264ref.gz': {
            'hashed_perceptron': 1.12543,
            '2bitcorr': 5.33099,
            'hashed_gselect': 4.35999
        },
        '471.omnetpp.gz': {
            'hashed_perceptron': 3.3543,
            '2bitcorr': 11.8707,
            'hashed_gselect': 11.4813
        }
    },
    'CPU_0_Average_ROB_Occupancy_at_Mispredict': {
        '400.perlbench': {
            'hashed_perceptron': 127.846,
            '2bitcorr': 119.427,
            'hashed_gselect': 123.16
        },
        '401.bzip2': {
            'hashed_perceptron': 24.549,
            '2bitcorr': 19.1897,
            'hashed_gselect': 20.1444
        },
        '403.gcc': {
            'hashed_perceptron': 94.5748,
            '2bitcorr': 36.8291,
            'hashed_gselect': 29.7873
        },
        '462.libquantum': {
            'hashed_perceptron': 101.958,
            '2bitcorr': 42.5362,
            'hashed_gselect': 37.6239
        },
        '464.h264ref.gz': {
            'hashed_perceptron': 54.2685,
            '2bitcorr': 56.0133,
            'hashed_gselect': 70.6322
        },
        '471.omnetpp.gz': {
            'hashed_perceptron': 70.7929,
            '2bitcorr': 48.5443,
            'hashed_gselect': 49.3917
        }
    }
}

# Extract benchmarks and policies
benchmarks = list(data['ROI_Cumulative_IPC'].keys())
policies = list(data['ROI_Cumulative_IPC'][benchmarks[0]].keys())

# Loop through each metric
for metric, metric_data in data.items():
    # Create subplots
    fig, ax = plt.subplots()

    # Extract x values
    x = np.arange(len(benchmarks))
    width = 0.15

    # Iterate through policies and plot bars for each policy
    for i, policy in enumerate(policies):
        metric_values = [metric_data[benchmark][policy] for benchmark in benchmarks]
        ax.bar(x + i * width, metric_values, width, label=policy)

    # Set axis labels and title
    ax.set_xlabel('Benchmarks')
    ax.set_ylabel(metric)
    ax.set_title(metric)

    # Set x-axis ticks and labels
    ax.set_xticks(x + width * (len(policies) - 1) / 2)
    ax.set_xticklabels(benchmarks, rotation=45, ha='right')

    # Add legend
    ax.legend()

    # Adjust layout to add more space to the right
    plt.tight_layout(rect=[0, 0, 1, 0.9])  # Adjust the last value to control the space on the right

    # Save the plot as an image file
    filename = f"{metric}.png"
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

    print(f"Saved plot for metric '{metric}' as '{filename}'")
