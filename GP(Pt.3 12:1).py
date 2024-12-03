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

# Calculate and print standard deviation and intrinsic scatter
std_residuals = np.std(residuals)
intrinsic_scatter = np.sqrt(std_residuals**2 - 0.25**2)
print(f"Standard Deviation: {std_residuals:.3f} ft\nIntrinsic Scatter: {intrinsic_scatter:.3f} ft")