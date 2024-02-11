import matplotlib.pyplot as plt
import control as ct

s = ct.TransferFunction.s

# Define the system (unstable)
G = 1/(s - 5)

# Define a PID controller
# C = Kp + Ki/s + Kd*s/(tau*s + 1)

# Derivative filter time
tau = 0.1

# Gains
Kp = 31.6
Kd = 0.73
Ki = 73

# Transfer function
C = Kp + Ki/s + Kd*s/(tau*s + 1)

# Plot root-locus of C*P
plt.figure()
ct.root_locus(C*G)

# Close loop transfer function setpoint to output
T = ct.feedback(C*G)

# Print transfer functions
print(f"T(s): {T}")

# Find poles
poles = ct.pole(T)
zeros = ct.zero(T)
print(f"Poles of T: {poles}")
print(f"Zeros of T: {zeros}")

# Plot step response
plt.figure()

# Step response - setpoint to output
t, yout = ct.step_response(T, T_num=100)

plt.plot(t, yout)
plt.ylabel("Output")
plt.grid()

plt.show()