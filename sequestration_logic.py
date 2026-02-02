import matplotlib.pyplot as plt
import numpy as np

# Simulation parameters: 24-hour window (Safety is about speed of clearance)
time = np.linspace(0, 24, 100) 

# Logic: In a Tumor Cell, the "Lock 2" is inactive.
# The viral RNA remains stable and begins translation/replication.
tumor_cell_rna = np.exp(0.15 * time) 

# Logic: In a Healthy Cell, the "3rd Lock" (Foreign Fragment) triggers sequestration.
# This leads to exponential degradation by cellular nucleases (RNases).
healthy_cell_rna = 1.0 * np.exp(-0.4 * time) 

plt.figure(figsize=(10, 6))
plt.plot(time, tumor_cell_rna, 'g-', linewidth=2, label='Tumor Cell: Viral RNA Stability')
plt.plot(time, healthy_cell_rna, 'r--', linewidth=2, label='Healthy Cell: Rapid Sequestration & Decay')

# Threshold for "Safety": Below 0.1, the virus is considered clinically inactive.
plt.axhline(y=0.1, color='gray', linestyle=':', label='Safety Clearance Threshold')

plt.title('Lock 2: RNA Sequestration Efficiency Simulation', fontsize=14)
plt.xlabel('Time (Hours Post-Entry)', fontsize=12)
plt.ylabel('Relative RNA Concentration', fontsize=12)
plt.yscale('log') # Log scale is standard for showing rapid degradation
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.legend()

# Save the result
plt.savefig('sequestration_results.png')
print("Safety simulation complete. Graph saved as sequestration_results.png")
