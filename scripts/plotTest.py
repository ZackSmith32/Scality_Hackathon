import numpy as np
import random
from matplotlib import pyplot as plt

def hist(data):
	# fixed bin size
	bins = np.arange(0, 50, 1) # fixed bin size

	plt.xlim([min(data)-1, 60])

	plt.hist(data, bins=bins, alpha=0.5)
	plt.title('Random Gaussian data (fixed bin size)')
	plt.xlabel('variable X (bin size = 5)')
	plt.ylabel('count')

	plt.show()