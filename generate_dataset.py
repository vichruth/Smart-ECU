import numpy as np
import csv
def generate_rpm_data(filename, label, duration_sec=60, sample_rate=50, is_anomaly=False):
    t = np.linspace(0, duration_sec, duration_sec * sample_rate)
    rpm = 2000 + 1500 * np.sin(0.5 * t) 
    noise = np.random.normal(0, 50, rpm.shape)
    rpm = rpm + noise
    if is_anomaly:
        num_spikes = int(len(t) * 0.1)
        spike_indices = np.random.choice(len(t), num_spikes, replace=False)
        rpm[spike_indices] += np.random.choice([-800, 800], num_spikes)
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["rpm", "label"]) 
        for value in rpm:
            writer.writerow([int(value), label])
    print(f"Generated {filename} with {len(rpm)} samples.")
generate_rpm_data("normal.csv", label=0, is_anomaly=False)
generate_rpm_data("anomaly.csv", label=1, is_anomaly=True)