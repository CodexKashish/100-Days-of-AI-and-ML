import numpy as np
import os

simulation_state = np.random.uniform(0, 1, (5, 5))

filename = "system_memory.npy"
np.save(filename, simulation_state)

print("--- Data Saved Successfully ---")
print(f"File '{filename}' created in your directory.")

del simulation_state

if os.path.exists(filename):
    restored_state = np.load(filename)
    print("\n--- Data Restored from Disk ---")
    print(restored_state)
    
    os.remove(filename)
    print("\nCleanup complete. Memory is fresh!")
