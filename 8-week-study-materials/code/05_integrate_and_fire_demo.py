"""
Concept taught:
    A very simple integrate-and-fire model shows how voltage can move toward
    threshold, create a spike event, and reset.

What the student should notice:
    - This is not a full biological neuron.
    - The model uses small time steps to update V_m.
    - When V_m reaches threshold, we record a spike and reset V_m.

Runtime:
    No downloads. Uses only NumPy and matplotlib.
    Saves one figure to minibook_v2/figures/generated/.
"""

from pathlib import Path
import os

import numpy as np


BOOK_DIR = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(BOOK_DIR / ".matplotlib_cache"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


FIGURE_DIR = BOOK_DIR / "figures" / "generated"
FIGURE_PATH = FIGURE_DIR / "05_integrate_and_fire_demo.png"


def run_lif_model(input_strength=18.0):
    """Run a simple leaky integrate-and-fire model.

    The update rule says:
        new voltage = old voltage + small change

    The small change has two parts:
        1. leak pulls voltage back toward baseline
        2. input pushes voltage upward toward threshold
    """
    dt_ms = 0.1
    total_ms = 300.0
    time_ms = np.arange(0, total_ms, dt_ms)

    baseline_mV = -70.0
    threshold_mV = -55.0
    reset_mV = -70.0
    tau_ms = 20.0

    voltage_mV = np.full_like(time_ms, baseline_mV, dtype=float)
    spike_times = []

    for i in range(1, len(time_ms)):
        # Leak term: if voltage is above baseline, leak pulls it downward.
        leak = (baseline_mV - voltage_mV[i - 1]) / tau_ms

        # Input term: a constant teaching input that pushes upward.
        drive = input_strength / tau_ms

        # Small update over one time step. This is algebraic stepping,
        # not a calculus derivation for the student.
        voltage_mV[i] = voltage_mV[i - 1] + (leak + drive) * dt_ms

        # Threshold rule: record a spike time and reset the voltage.
        if voltage_mV[i] >= threshold_mV:
            spike_times.append(time_ms[i])
            voltage_mV[i] = reset_mV

    return time_ms, voltage_mV, np.array(spike_times), threshold_mV


def main():
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    time_ms, voltage_mV, spike_times, threshold_mV = run_lif_model()

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(time_ms, voltage_mV, color="#0f766e", linewidth=2.5)
    ax.axhline(threshold_mV, color="#dc2626", linestyle="--", linewidth=2, label="threshold")

    # Mark spike events with vertical lines. The plotted voltage resets, so the
    # lines remind the student where spike events occurred.
    for spike_t in spike_times:
        ax.axvline(spike_t, color="#2563eb", alpha=0.35, linewidth=2)

    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Membrane potential, V_m (mV)")
    ax.set_title("Simple integrate-and-fire model")
    ax.grid(True, alpha=0.25)
    ax.legend()
    ax.text(10, -53, f"spikes recorded: {len(spike_times)}", fontsize=11)
    fig.tight_layout()
    fig.savefig(FIGURE_PATH, dpi=180)
    plt.close(fig)

    print(f"Saved figure: {FIGURE_PATH}")
    print(f"Spike times (ms): {np.round(spike_times, 1).tolist()}")


if __name__ == "__main__":
    main()

