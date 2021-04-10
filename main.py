import matplotlib.pyplot as plt
import numpy as np
from qctrlvisualizer import get_qctrl_style, plot_controls

from qctrl import Qctrl

plt.style.use(get_qctrl_style())

# Start a session with the API.
qctrl = Qctrl()

control_count = 1
segment_count = 1
duration = 30.0
shot_count = 32

max_rabi_rate = 20 * 2 * np.pi  # MHz


controls = []
# for k in range(control_count):
#     # Create a random string of complex numbers for each controls.
#     real_part = np.random.random(size=[segment_count])
#     imag_part = np.random.random(size=[segment_count])
#     values = 0.15 * k * (real_part + 1j * imag_part)

controls.append({"duration": np.pi / max_rabi_rate, "values": np.array([1])})


experiment_results = qctrl.functions.calculate_qchack_measurements(
    controls=controls,
    shot_count=shot_count,
)

measurements = experiment_results.measurements
for k, measurement_counts in enumerate(measurements):
    print(f"control #{k}: {measurement_counts}")


for k, measurement_counts in enumerate(measurements):
    p0 = measurement_counts.count(0) / shot_count
    p1 = measurement_counts.count(1) / shot_count
    p2 = measurement_counts.count(2) / shot_count
    print(f"control #{k}: P(|0>) = {p0:.2f}, P(|1>) = {p1:.2f}, P(|2>) = {p2:.2f}")

