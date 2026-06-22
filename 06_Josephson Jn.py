import numpy as np
import matplotlib.pyplot as plt

# Parameters
Ic = 1.0
Ej = 1.0
phi = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# ── Calculate ──

# Current-phase relationship
# Formula: I = Ic × sin(φ)
current = I = Ic * np.sin(phi)

# Energy-phase relationship  
# Formula: E = Ej × (1 - cos(φ))
energy = Ej * (1 - np.cos(phi))

# ── Plot ──
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Plot 1: Current vs Phase
axes[0].plot(phi, current, phi, current, color='#E24B4A', linewidth=2.5)
axes[0].axhline(y=0, color='gray', linestyle='--', alpha=0.5)
axes[0].axvline(x=0, color='gray', linestyle='--', alpha=0.5)
axes[0].set_xlabel("Phase φ (radians)", fontsize=12)
axes[0].set_ylabel("Current I (µA)", fontsize=12)
axes[0].set_title("Current-Phase Relationship")
axes[0].grid(alpha=0.3)

# Plot 2: Energy vs Phase
axes[1].plot(phi, energy, phi, energy, color='#1D9E75', linewidth=2.5)
axes[1].set_xlabel("Phase φ (radians)", fontsize=12)
axes[1].set_ylabel("Energy E (GHz)", fontsize=12)
axes[1].set_title("Energy Landscape")
axes[1].grid(alpha=0.3)

# Plot 3: Energy levels inside potential well
# Focus on one period: -π to π
phi_well = np.linspace(-np.pi, np.pi, 500)
energy_well = Ej * (1 - np.cos(phi_well))

axes[2].plot(phi_well, energy_well, color='#1F4E79', linewidth=2.5)

# Add energy levels — equally spaced for harmonic, unequally for anharmonic
# For Josephson junction they are slightly unequal — anharmonicity
energy_levels = [0.2, 0.55, 0.85]   # approximate normalised levels
level_colors  = ['#1D9E75', '#BA7517', '#E24B4A']
level_labels  = ['|0⟩ ground state', '|1⟩ first excited', '|2⟩ second excited']

for level, color, label in zip(energy_levels, level_colors, level_labels):
    # find where energy curve crosses this level
    idx = np.argmin(np.abs(energy_well - level * Ej * 2))
    phi_cross = phi_well[idx]
    axes[2].axhline(y=level * Ej * 2,
                    xmin=(phi_cross + np.pi) / (2*np.pi),
                    xmax=1 - (phi_cross + np.pi) / (2*np.pi),
                    color=color, linewidth=2, label=label)

axes[2].set_xlabel("Phase φ", fontsize=12)
axes[2].set_ylabel("Energy", fontsize=12)
axes[2].set_title("Energy Levels — Anharmonic Spectrum")
axes[2].legend(fontsize=10)
axes[2].grid(alpha=0.3)

plt.suptitle(
    "Josephson Junction — Current, Energy and Qubit Levels",
    fontsize=14, fontweight='bold'
)
plt.tight_layout()
plt.savefig("josephson_junction.png", dpi=150, bbox_inches='tight')
plt.show()

# Print physics summary
print("Josephson Junction Model")
print(f"Critical current Ic = {Ic} µA")
print(f"Josephson energy Ej = {Ej} GHz")
print("\nPhysics:")
print("  I = Ic × sin(φ)  — current-phase relationship")
print("  E = Ej × (1 - cos(φ))  — energy-phase relationship")
print("  Anharmonic energy levels → only |0⟩ and |1⟩ addressable → qubit")
print("  This is the operating principle of transmon qubits")
print("  Used in IBM, Google and all major superconducting quantum computers")
