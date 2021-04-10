import matplotlib.pyplot as plt
import numpy as np
from qctrlvisualizer import get_qctrl_style, plot_controls

from qctrl import Qctrl

plt.style.use(get_qctrl_style())

# Start a session with the API.
qctrl = Qctrl()

control_count = 5
segment_count = 1
shot_count = 1000

max_rabi_rate = 20 * 2 * np.pi  # MHz

controls = []
for k in range(control_count):
    controls.append({"duration": (np.pi / max_rabi_rate)*1000, "values": np.array([1])})

with qctrl.create_graph() as graph:
    with graph:
        variables = qctrl.operations.bounded_optimization_variable(
            count=10,
            lower_bound=0,
            upper_bound=1,
        )







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

cost = 0
for i in range(control_count):
    cost = cost + (p0-0)**2 + (p1-1)**2 + (p2-0)**2
print(cost)




