"""
Concept taught:
    EPSPs and IPSPs are small graded voltage changes. They can add together
    before the trigger zone reaches threshold.

What the student should notice:
    - EPSPs move V_m upward, toward threshold.
    - IPSPs can reduce or oppose that upward movement.
    - The combined trace matters more than any one input alone.

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
FIGURE_PATH = FIGURE_DIR / "03_threshold_summation_demo.png"


def psp(time_ms, start_ms, amplitude_mV, tau_ms=12.0):
    """Make a simple postsynaptic potential shape.

    This is a teaching curve: it rises instantly and fades gradually.
    Positive amplitude makes an EPSP. Negative amplitude makes an IPSP.
    """
    effect = np.zeros_like(time_ms)
    after_start = time_ms >= start_ms
    effect[after_start] = amplitude_mV * np.exp(-(time_ms[after_start] - start_ms) / tau_ms)
    return effect


def main():
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    time_ms = np.linspace(0, 100, 1001)
    rest_mV = -70.0
    threshold_mV = -55.0

    # Three inputs: two excitatory, one inhibitory.
    epsp_1 = psp(time_ms, start_ms=15, amplitude_mV=6)
    epsp_2 = psp(time_ms, start_ms=30, amplitude_mV=7)
    ipsp_1 = psp(time_ms, start_ms=42, amplitude_mV=-5)
    epsp_3 = psp(time_ms, start_ms=55, amplitude_mV=8)

    combined_mV = rest_mV + epsp_1 + epsp_2 + ipsp_1 + epsp_3

    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.plot(time_ms, combined_mV, color="#0f766e", linewidth=3, label="combined V_m")
    ax.plot(time_ms, rest_mV + epsp_1, color="#2563eb", alpha=0.35, label="single inputs")
    ax.plot(time_ms, rest_mV + epsp_2, color="#2563eb", alpha=0.35)
    ax.plot(time_ms, rest_mV + ipsp_1, color="#ea580c", alpha=0.45)
    ax.plot(time_ms, rest_mV + epsp_3, color="#2563eb", alpha=0.35)
    ax.axhline(rest_mV, color="#64748b", linestyle=":", linewidth=2, label="rest")
    ax.axhline(threshold_mV, color="#dc2626", linestyle="--", linewidth=2, label="threshold")

    ax.text(16, -62, "EPSP", color="#2563eb")
    ax.text(43, -76, "IPSP", color="#ea580c")
    ax.text(72, threshold_mV + 1.5, "threshold", color="#dc2626")

    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Membrane potential, V_m (mV)")
    ax.set_title("Small synaptic inputs sum before threshold")
    ax.set_ylim(-82, -50)
    ax.grid(True, alpha=0.25)
    ax.legend(loc="lower right")
    fig.tight_layout()
    fig.savefig(FIGURE_PATH, dpi=180)
    plt.close(fig)

    print(f"Saved figure: {FIGURE_PATH}")


if __name__ == "__main__":
    main()

