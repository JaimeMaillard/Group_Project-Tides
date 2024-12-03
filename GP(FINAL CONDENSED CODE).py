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

initial_guess = [5, 2 * np.pi / 12.42, 0, 0]

popt, pcov = curve_fit(tide_model, day, height, p0=initial_guess, sigma=np.full(len(height), 0.25))

A, omega, phi, C = popt
print(f"Fitted Parameters:\nAmplitude (A): {A:.3f}\nFrequency (omega): {omega:.3f}\nPhase (phi): {phi:.3f}\nOffset (C): {C:.3f}")

plt.figure(figsize=(8, 5))
plt.errorbar(day, height, yerr=0.25, fmt='o', label="Data", capsize=3)
plt.plot(np.linspace(min(day), max(day), 1000), tide_model(np.linspace(min(day), max(day), 1000), *popt), 'r-', label="Fitted Model")
plt.xlabel("Day"), plt.ylabel("Height (ft)"), plt.title("Tidal Data with Fitted Oscillatory Model")
plt.legend(), plt.grid(True), plt.tight_layout(), plt.savefig("tide_model_fit.pdf"), plt.show()

residuals = height - tide_model(day, *popt)

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(day, residuals, color="purple", label="Residuals", alpha=0.8)
ax.axhline(0, color="black", linestyle="--", linewidth=1, label="Zero Line")
ax.set_xlabel("Day")
ax.set_ylabel("Residual (ft)")
ax.set_title("Residuals of Tide Data vs. Model")
ax.legend()
ax.grid(visible=True, linestyle=":", alpha=0.7)

fig.tight_layout()
fig.savefig("alternative_residuals_plot.pdf")
plt.show()

plt.hist(residuals, bins=np.linspace(min(residuals), max(residuals), 15), color="orange", edgecolor="black", alpha=0.75)
plt.axvline(np.mean(residuals), color="red", linestyle="--", linewidth=1.5, label="Mean Residual")
plt.xlabel("Residual (ft)"), plt.ylabel("Frequency")
plt.title("Histogram of Residuals"), plt.legend(), plt.grid(alpha=0.7, linestyle=":")
plt.tight_layout()
plt.savefig("short_residuals_histogram.pdf")
plt.show()

std_residuals = np.std(residuals)
intrinsic_scatter = np.sqrt(std_residuals**2 - 0.25**2)
print(f"Standard Deviation: {std_residuals:.3f} ft\nIntrinsic Scatter: {intrinsic_scatter:.3f} ft")