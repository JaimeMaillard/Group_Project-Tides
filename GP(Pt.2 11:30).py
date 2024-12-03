#First import all ans use scipy to optimize
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.genfromtxt("ASTR19_F24_group_project_data.txt",
                     dtype=[('day', 'i8'), ('time', 'U6'), ('height', 'f8')])

day = np.array(data['day'])
height = np.array(data['height'])

def tide_model(t, A, omega, phi, C):
    return A * np.sin(omega * t + phi) + C

initial_guess = [5, 2 * np.pi / 12.42, 0, 0]\

popt, pcov = curve_fit(tide_model, day, height, p0=initial_guess, sigma=np.full(len(height), 0.25))

A, omega, phi, C = popt
print(f"Fitted Parameters:\nAmplitude (A): {A:.3f}\nFrequency (omega): {omega:.3f}\nPhase (phi): {phi:.3f}\nOffset (C): {C:.3f}")

plt.figure(figsize=(8, 5))
plt.errorbar(day, height, yerr=0.25, fmt='o', label="Data", capsize=3)
plt.plot(np.linspace(min(day), max(day), 1000), tide_model(np.linspace(min(day), max(day), 1000), *popt), 'r-', label="Fitted Model")
plt.xlabel("Day"), plt.ylabel("Height (ft)"), plt.title("Tidal Data with Fitted Oscillatory Model")
plt.legend(), plt.grid(True), plt.tight_layout(), plt.savefig("tide_model_fit.pdf"), plt.show()