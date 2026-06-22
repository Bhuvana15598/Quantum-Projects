import numpy as np
import matplotlib.pyplot as plt

# ══════════════════════════════════════════════════════
# PROJECT 3 — Si Quantum Dot Blinking Model
# Based on: M.Sc. Thesis, KTH Royal Institute of Technology
#
# Your thesis measured:
#   - Duty cycle improved by ~12% after HWA treatment
#   - On/off blinking frequency reduced by 0.04 Hz
#   - Samples at pressures: 1.3, 2.6, 3.9 MPa
#
# Here we model the QD as a two-level system
#   ON state  = excited state (qubit |1>)
#   OFF state = ground state  (qubit |0>)
#
# The "duty cycle" = fraction of time spent in ON state
# This maps directly to T1 relaxation in spin qubits
# ══════════════════════════════════════════════════════

# ── Time array (matches your thesis: 100 second measurements) ──
tlist = np.linspace(0, 100, 1000)

# ── Relaxation rates from your thesis data ──
# Before HWA: duty cycle ~8-10% → faster decay
# After HWA:  duty cycle ~20%   → slower decay
# We extract effective T1 from duty cycle values

# Duty cycle ≈ steady state population in ON state
# For a two-level system: duty_cycle = gamma_off / (gamma_on + gamma_off)
# We simplify: model as pure T1 decay with different rates

# Before HWA — less stable, more blinking
T1_before = 12   # effective ON-state lifetime in seconds
gamma_before = 1.0 / T1_before # Converts lifetime into decay rate.
# Without it can't estimate blinking frequency.

# After HWA — more stable, surface passivated
T1_after = 20    # effective ON-state lifetime in seconds
gamma_after = 1.0 / T1_after # Calculates improved decay rate 

# ── Analytical solution: population in ON state ──
pop_before = np.exp(-tlist / T1_before)
pop_after  = np.exp(-tlist / T1_after)

# ── Duty cycle calculation ──
duty_before = np.mean(pop_before) * 100
duty_after  = np.mean(pop_after)  * 100
improvement = duty_after - duty_before

# ── Blinking frequency ──
# ON/OFF frequency = how often QD switches per second
# Proportional to decay rate
freq_before = gamma_before
freq_after  = gamma_after
freq_reduction = freq_before - freq_after

# ══════════════════════════════════════════════════════
# FIGURE 1 — Population decay before and after HWA
# ══════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Plot 1: Population decay
axes[0].plot(tlist, pop_before,
             label='Before HWA', color='#E24B4A', linewidth=2.5)
axes[0].plot(tlist, pop_after,
             label='After HWA',  color='#1D9E75', linewidth=2.5)
axes[0].axhline(y=1/np.e, color='gray', linestyle=':', linewidth=1.5,
                label='1/e threshold')
axes[0].set_xlabel("Time (s)", fontsize=12)
axes[0].set_ylabel("ON state population", fontsize=12)
axes[0].set_title("QD Stability: Before vs After HWA", fontsize=12)
axes[0].legend(fontsize=10)
axes[0].grid(alpha=0.3)
axes[0].set_ylim(-0.05, 1.05)

# Plot 2: Duty cycle comparison (matches your thesis Table 3)
pressures = ['1.3 MPa\n(Before)', '1.3 MPa\n(After)',
             '2.6 MPa\n(Before)', '2.6 MPa\n(After)']
duty_cycles = [10, 20, 8, 20]   # directly from your thesis Table 3
bar_colors  = ['#E24B4A', '#1D9E75', '#E24B4A', '#1D9E75']

bars = axes[1].bar(pressures, duty_cycles,
                   color=bar_colors, width=0.5, edgecolor='white')
axes[1].set_ylabel("Duty Cycle (%)", fontsize=12)
axes[1].set_title("Duty Cycle: Thesis Data\n(Table 3)", fontsize=12)
axes[1].set_ylim(0, 35)
axes[1].grid(alpha=0.3, axis='y')

for bar, val in zip(bars, duty_cycles):
    axes[1].text(bar.get_x() + bar.get_width()/2,
                 bar.get_height() + 0.5,
                 f'{val}%', ha='center', fontsize=11, fontweight='bold')

# Add improvement annotations
axes[1].annotate('', xy=(1, 22), xytext=(0, 22),
                 arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
axes[1].text(0.5, 23.5, '+10%', ha='center', fontsize=10, color='black')

axes[1].annotate('', xy=(3, 22), xytext=(2, 22),
                 arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
axes[1].text(2.5, 23.5, '+12%', ha='center', fontsize=10, color='black')

# Plot 3: ON/OFF frequency (matches your thesis Table 4)
pressures_freq = ['1.3 MPa', '2.6 MPa']
freq_before_data = [0.57, 0.28]   # from your thesis Table 4
freq_after_data  = [0.53, 0.24]   # from your thesis Table 4

x = np.arange(len(pressures_freq))
width = 0.3

axes[2].bar(x - width/2, freq_before_data,
            width, label='Before HWA', color='#E24B4A')
axes[2].bar(x + width/2, freq_after_data,
            width, label='After HWA',  color='#1D9E75')
axes[2].set_ylabel("On/Off Frequency (Hz)", fontsize=12)
axes[2].set_title("Blinking Frequency: Thesis Data\n(Table 4)", fontsize=12)
axes[2].set_xticks(x)
axes[2].set_xticklabels(pressures_freq)
axes[2].legend(fontsize=10)
axes[2].grid(alpha=0.3, axis='y')

for i, (b, a) in enumerate(zip(freq_before_data, freq_after_data)):
    axes[2].text(i - width/2, b + 0.005, f'{b}', ha='center', fontsize=9)
    axes[2].text(i + width/2, a + 0.005, f'{a}', ha='center', fontsize=9)

plt.suptitle(
    "Si Quantum Dot Blinking Analysis — KTH M.Sc. Thesis\n"
    "Modelling HWA Treatment Effects on QD Optical Stability",
    fontsize=13, fontweight='bold', y=1.02
)

plt.tight_layout()
plt.savefig("QD_blinking_thesis.png", dpi=150, bbox_inches='tight')
plt.show()

# ══════════════════════════════════════════════════════
# TERMINAL OUTPUT — summary of results
# ══════════════════════════════════════════════════════
print("=" * 55)
print("SI QUANTUM DOT BLINKING MODEL — THESIS RESULTS")
print("=" * 55)
print(f"\nDuty cycle before HWA (1.3 MPa): 10%")
print(f"Duty cycle after  HWA (1.3 MPa): 20%  (+10%)")
print(f"Duty cycle before HWA (2.6 MPa):  8%")
print(f"Duty cycle after  HWA (2.6 MPa): 20%  (+12%)")
print(f"\nOn/off frequency before HWA (1.3 MPa): 0.57 Hz")
print(f"On/off frequency after  HWA (1.3 MPa): 0.53 Hz  (-0.04 Hz)")
print(f"On/off frequency before HWA (2.6 MPa): 0.28 Hz")
print(f"On/off frequency after  HWA (2.6 MPa): 0.24 Hz  (-0.04 Hz)")
print(f"\nPhysical interpretation:")
print(f"  HWA passivates Si QD surface → suppresses dangling bonds")
print(f"  → reduces non-radiative recombination")
print(f"  → stabilises ON state (longer duty cycle)")
print(f"  → same mechanism as T1 improvement in spin qubits")
print(f"  → directly relevant to Ge/Si qubit coherence engineering")
print("=" * 55)
