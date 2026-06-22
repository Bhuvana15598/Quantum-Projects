import qutip as qt
import numpy as np
import matplotlib.pyplot as plt

# ── PART 1: Basic quantum states ──

# Ground state |0> — qubit is OFF
ground = qt.basis(2, 0)

# Excited state |1> — qubit is ON
excited = qt.basis(2, 1)

# Superposition — qubit is both ON and OFF
superposition = (ground + excited).unit()

print("Ground state |0>:")
print(ground)

print("\nExcited state |1>:")
print(excited)

print("\nSuperposition state:")
print(superposition)

# ── PART 2: Quantum gates (Pauli matrices) ──
# These are the building blocks of quantum device operation

sx = qt.sigmax()   # X gate — flips qubit
sy = qt.sigmay()   # Y gate
sz = qt.sigmaz()   # Z gate — measures qubit

print("\nPauli X (flip gate):")
print(sx)

# Apply X gate to ground state — should give excited state
flipped = sx * ground
print("\nAfter X gate applied to |0>:")
print(flipped)

# ── PART 3: Bloch sphere visualisation ──
b = qt.Bloch()

# Add states to the sphere
b.add_states(ground)      # north pole
b.add_states(excited)     # south pole
b.add_states(superposition)  # equator

b.save('bloch_sphere.png')
b.show()

print("\nBloch sphere saved as bloch_sphere.png")
