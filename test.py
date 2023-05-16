import numpy as np
import matplotlib.pyplot as plt
import math

"""	high pass filter	"""
R1 = 10
L1 = 3.75e-3
C1 = 75e-6

"""	low pass filter		"""
R2 = 10
L2 = 375e-6
C2 = 7.5e-6

freq  = []
gain  = []
phase = []

"""         loop over all frequencies from 1 to 1M        """
for frequancy in range(1, 1000000, 1):
	w = 2 * np.pi * frequancy 		#calculate the omega frequency
	s = 1j * w				#calculate the imaginary omega

	"""       CALCULATE THE PHASE       """
	h1 = (s * L1) / (R1 + s * L1 + 1 / (s * C1))		#
	h2 = (1 / (s * C2)) / (R2 + s * L2 + 1 / (s * C2))
	H = h1 * h2
	phase_degree = np.angle(H) * 180 / np.pi
	phase.append(phase_degree)
	gain.append(20 * math.log10(abs(H)))
	freq.append(frequancy)


	"""       anther way to calculate the gain        """
	#hw1 = (w * L1 / math.sqrt((R1 ** 2) + ((w * L1) - (1 / (w * C1))) ** 2))
	#hw2 = ((1 / (w * C2)) / math.sqrt(R2 ** 2 + (w * L2 - 1 / (w * C2)) ** 2))


def main():
	# plot the phase response
	fig1, ax1 = plt.subplots(figsize=(25, 12))
	ax1.plot(freq, phase, linestyle='-', color='blue', linewidth=1, rasterized=False)
	ax1.set_xlabel('Frequency (Hz)')
	ax1.set_ylabel('Phase (degrees)')
	ax1.set_title('Phase Response')
	ax1.set_xscale('log') # set log scale for x-axis
	ax1.grid(True)
	ax1.legend(['Phase'])

	# plot the gain response
	fig2, ax2 = plt.subplots(figsize=(25, 12))
	ax2.plot(freq, gain, linestyle='-', color='red', linewidth=1, rasterized=True)
	ax2.set_xlabel('Frequency (Hz)')
	ax2.set_ylabel('Gain (dB)')
	ax2.set_title('Gain Response')
	ax2.set_xscale('log') # set log scale for x-axis
	ax2.grid(True)
	ax2.legend(['Gain'])

	plt.show()


if __name__ == '__main__':
	main()
