import os
import numpy as np


alpha_s = np.linspace(0.1, 1.0, 5)
li_ratios = np.linspace(0.1, 1.0, 5)

for alpha in alpha_s:
    for l1 in li_ratios:
        print(f"loggingexperiment for alpha: {alpha}, l1_ratio: {l1}")
        os.system(f"python demo.py -a {alpha} -l1 {l1}")