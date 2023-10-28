import matplotlib.pyplot as plt
import numpy as np

data = {
    'ROI_Cumulative_IPC': {
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
    },
    'ROI_LLCTOTAL_HITRATE': {
        '400.perlbench': {
            'lru': 0.613433,
            'lip': 0.165725,
            'bip': 0.198355,
            'dip': 0.610614,
            'ptreelru': 0.604454
        },
        '401.bzip2': {
            'lru': 0.788669,
            'lip': 0.749213,
            'bip': 0.764546,
            'dip': 0.787631,
            'ptreelru': 0.78575
        },
        '403.gcc': {
            'lru': 0.742493,
            'lip': 0.467711,
            'bip': 0.615974,
            'dip': 0.746947,
            'ptreelru': 0.7314
        },
        '462.libquantum': {
            'lru': 0.151136,
            'lip': 0.114359,
            'bip': 0.0955255,
            'dip': 0.122377,
            'ptreelru': 0.148588
        },
        '464.h264ref': {
            'lru': 0.482282,
            'lip': 0.412135,
            'bip': 0.401292,
            'dip': 0.480282,
            'ptreelru': 0.481354
        },
        '471.omnetpp': {
            'lru': 0.358178,
            'lip': 0.129967,
            'bip': 0.139646,
            'dip': 0.356344,
            'ptreelru': 0.356495
        }
    },
    'ROI_LLCLOAD_HITRATE': {
        '400.perlbench': {
            'lru': 0.500961,
            'lip': 0.183682,
            'bip': 0.217515,
            'dip': 0.497246,
            'ptreelru': 0.495886
        },
        '401.bzip2': {
            'lru': 0.791586,
            'lip': 0.793156,
            'bip': 0.800167,
            'dip': 0.793145,
            'ptreelru': 0.789529
        },
        '403.gcc': {
            'lru': 0.830816,
            'lip': 0.598818,
            'bip': 0.807764,
            'dip': 0.840543,
            'ptreelru': 0.820159
        },
        '462.libquantum': {
            'lru': 0.0,
            'lip': 0.0319226,
            'bip': 0.000960282,
            'dip': 5.8452e-06,
            'ptreelru': 0.0
        },
        '464.h264ref': {
            'lru': 0.362626,
            'lip': 0.398517,
            'bip': 0.394639,
            'dip': 0.362729,
            'ptreelru': 0.369114
        },
        '471.omnetpp': {
            'lru': 0.100812,
            'lip': 0.0905747,
            'bip': 0.0880151,
            'dip': 0.10061,
            'ptreelru': 0.107185
        }
    },
    'ROI_LLCWRITEBACK_HITRATE': {
        '400.perlbench': {
            'lru': 0.995833,
            'lip': 0.206797,
            'bip': 0.251513,
            'dip': 0.990066,
            'ptreelru': 0.977639
        },
        '401.bzip2': {
            'lru': 0.986363,
            'lip': 0.708019,
            'bip': 0.754623,
            'dip': 0.979331,
            'ptreelru': 0.969184
        },
        '403.gcc': {
            'lru': 0.979285,
            'lip': 0.365927,
            'bip': 0.421927,
            'dip': 0.972284,
            'ptreelru': 0.96512
        },
        '462.libquantum': {
            'lru': 0.933433,
            'lip': 0.541059,
            'bip': 0.585007,
            'dip': 0.755782,
            'ptreelru': 0.917694
        },
        '464.h264ref': {
            'lru': 0.992218,
            'lip': 0.497649,
            'bip': 0.514718,
            'dip': 0.982534,
            'ptreelru': 0.965247
        },
        '471.omnetpp': {
            'lru': 0.991036,
            'lip': 0.228882,
            'bip': 0.26681,
            'dip': 0.985345,
            'ptreelru': 0.96889
        }
    },
    'ROI_LLCAVERAGE_MISS_LATENCY': {
        '400.perlbench': {
            'lru': 2223.58,
            'lip': 993.623,
            'bip': 1058.74,
            'dip': 2200.12,
            'ptreelru': 2154.96
        },
        '401.bzip2': {
            'lru': 905.592,
            'lip': 682.129,
            'bip': 671.0,
            'dip': 929.162,
            'ptreelru': 831.201
        },
        '403.gcc': {
            'lru': 252.788,
            'lip': 198.907,
            'bip': 176.606,
            'dip': 251.33,
            'ptreelru': 252.272
        },
        '462.libquantum': {
            'lru': 419.059,
            'lip': 384.532,
            'bip': 387.162,
            'dip': 405.605,
            'ptreelru': 418.531
        },
        '464.h264ref': {
            'lru': 1365.6,
            'lip': 768.319,
            'bip': 781.317,
            'dip': 1350.89,
            'ptreelru': 1334.0
        },
        '471.omnetpp': {
            'lru': 475.393,
            'lip': 345.572,
            'bip': 349.945,
            'dip': 474.444,
            'ptreelru': 467.63
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
    ax.set_xticklabels(benchmarks)

    # Add legend
    ax.legend()

    # Save the plot as an image file
    filename = f"{metric}.png"
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

    print(f"Saved plot for metric '{metric}' as '{filename}'")
