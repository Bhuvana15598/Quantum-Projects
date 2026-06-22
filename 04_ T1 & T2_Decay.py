import qutip as qt
import numpy as np
import matplotlib.pyplot as plt

# T1 decay analytical solution
# Population of excited state = exp(-t/T1)
# have to calculate T2 as well
# This is the exact solution to the Lindblad equation for pure relaxation
# No solver needed — direct physics

T1 = 50    
T2 = 30
t1_color = ['#E24B4A']
t2_color = ['#BA7517']

tlist = np.linspace(0, 100, 500)

T1_value = {
    " T1 = 50 µs":      50,
    
}



T2_value = {
    " T2 = 30 µs":      30,
    
}


plt.figure(figsize=(10, 6))


for (label, T1), col in zip(T1_value.items(), t1_color):
    population = np.exp(-tlist / T1)
    plt.plot(tlist, population, label=f'T1={T1} µs', color=col, linewidth=2.5)
    plt.axvline(x=T1, color=col, linestyle='--', alpha=0.4)

plt.axhline(y=1/np.e, color='gray', linestyle=':', linewidth=1.5,
            label='1/e ≈ 0.368')

for (label, T2), col in zip(T2_value.items(), t2_color):
    coherence = np.exp(-tlist / T2)
    plt.plot(tlist, coherence, label=f'T2={T2} µs', color=col, linewidth=2.5)
    plt.axvline(x=T2, color=col, linestyle='--', alpha=0.4)

    



plt.xlabel("Time (µs)", fontsize=12)
plt.ylabel("Normalized Value", fontsize=12)
plt.title("T1 & T2 Relaxation: Effect of Material Quality on Qubit Lifetime", fontsize=13)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.ylim(-0.05, 1.05)
plt.tight_layout()
plt.savefig("T1 &T2 _decay.png", dpi=150)
plt.show()

print("Plot generated successfully.\n")

print("Physics interpretation:")
print(f" T1 = {50} µs")
print("     Energy relaxation time")
print("     Excited-state population decays as exp(-t/T1)\n")

print(f"  T2 = {30} µs")
print("     Coherence (phase information) decay time")
print("     Coherence decays as exp(-t/T2)\n")

print("At t = T1:")
print(f"  Population = {np.exp(-1):.3f}")

print("\nAt t = T2:")
print(f"  Coherence = {np.exp(-1):.3f}")

print("\nImportant:")
print("  T1 measures loss of energy.")
print("  T2 measures loss of phase information.")
print("  A qubit can retain energy while already losing coherence.")
print("  Quantum computations are usually limited by T2.")
