import qutip as qt
import numpy as np
import matplotlib.pyplot as plt

# Parameters
omega=0.3 # Rabi frequency — controls how fast qubit oscillates
T2= 20    # dephasing time — controls how fast oscillation dies
tlist = np.linspace(0,100,1000)

#--- Calculate curves ---

# Ideal Rabi- no decoherence, oscillates forever
# Formula: sin²(omega × t / 2)
rabi_ideal= np.sin(omega* tlist / 2)**2

# Realistic Rabi — oscillation decays due to T2
# Formula: sin²(omega × t / 2) × exp(−t/T2)
rabi_real = np.sin(omega* tlist / 2)**2* np.exp(-tlist/T2)

# Decay envelope — upper boundary of the decay
envelope = np.exp(-tlist / T2)

#--- Plot ---
plt.figure(figsize=(10, 6))

# Plot ideal Rabi curve
plt.plot(tlist, rabi_ideal, label='Ideal', color='Red', linewidth= 2.5)

# Plot realistic Rabi curve  
plt.plot(tlist, rabi_real, label='Real', color='Black', linewidth= 2.5)

# Shaded envelope showing T2 decay boundary
plt.fill_between(tlist, envelope, alpha=0.1, color='Blue', label='T2 decay envelope')

# Labels and formatting
plt.xlabel("Time (µs)", fontsize=12)
plt.ylabel("P|1⟩(t)")
plt.title("Rabi Oscillation")
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.ylim(-0.1, 1.1)
plt.tight_layout()
plt.savefig("rabi_oscillations.png", dpi=150)
plt.show()

# Print physics summary
print("Rabi Oscillations")
print(f"Rabi frequency: {omega} MHz")
print(f"T2 dephasing time: {T2} µs")
print("Trend between Ideal and Real Rabi Oscillation")
