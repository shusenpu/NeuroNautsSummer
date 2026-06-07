"""
Concept taught:
    Membrane voltage is a difference between inside and outside, and a
    voltage change can be read with signs and units.

What the student should notice:
    - Moving from -70 mV to -55 mV is a +15 mV change.
    - The membrane became less negative, so this is depolarization.
    - Moving from -70 mV to -80 mV is a -10 mV change.
    - The membrane became more negative, so this is hyperpolarization.

Runtime:
    No downloads. Uses only NumPy and matplotlib.
    Saves one figure to minibook_v2/figures/generated/.
"""

from pathlib import Path
import os

import numpy as np


# Keep matplotlib from trying to write a cache file in the user's home folder.
BOOK_DIR = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(BOOK_DIR / ".matplotlib_cache"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


FIGURE_DIR = BOOK_DIR / "figures" / "generated"
FIGURE_PATH = FIGURE_DIR / "01_voltage_changes.png"


def make_step_trace(start_mV, end_mV, switch_time_ms=20.0, total_time_ms=50.0):
    """Create a simple voltage trace with one clean voltage change.

    This is not trying to be a realistic neuron model. It is just a clear
    graph for practicing signs, units, and graph reading.
    """
    time_ms = np.linspace(0, total_time_ms, 501)
    voltage_mV = np.where(time_ms < switch_time_ms, start_mV, end_mV)
    return time_ms, voltage_mV


def describe_change(start_mV, end_mV):
    """Return the signed change and a student-friendly name."""
    change_mV = end_mV - start_mV
    if change_mV > 0:
        name = "depolarization"
    elif change_mV < 0:
        name = "hyperpolarization"
    else:
        name = "no voltage change"
    return change_mV, name


def main():
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    examples = [
        (-70, -55, "Depolarization: less negative"),
        (-70, -80, "Hyperpolarization: more negative"),
    ]

    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

    for ax, (start_mV, end_mV, title) in zip(axes, examples):
        time_ms, voltage_mV = make_step_trace(start_mV, end_mV)
        change_mV, name = describe_change(start_mV, end_mV)

        ax.plot(time_ms, voltage_mV, linewidth=3)
        ax.scatter([0, 25], [start_mV, end_mV], s=50, zorder=3)

        # Draw a double-ended marker showing the size of the voltage change.
        ax.annotate(
            "",
            xy=(32, end_mV),
            xytext=(32, start_mV),
            arrowprops={"arrowstyle": "<->", "linewidth": 2},
        )
        ax.text(
            34,
            (start_mV + end_mV) / 2,
            f"change = {change_mV:+.0f} mV",
            va="center",
            fontsize=11,
        )

        ax.set_title(title)
        ax.set_xlabel("Time (ms)")
        ax.set_ylim(-90, -45)
        ax.grid(True, alpha=0.25)
        ax.text(2, start_mV + 2, f"start {start_mV} mV", fontsize=10)
        ax.text(25, end_mV + 2, f"end {end_mV} mV", fontsize=10)
        ax.text(3, -88, name, fontsize=10, color="#334155")

    axes[0].set_ylabel("Membrane potential, V_m (mV)")
    fig.suptitle("Reading voltage changes: sign, size, and direction")
    fig.tight_layout()
    fig.savefig(FIGURE_PATH, dpi=180)
    plt.close(fig)

    print(f"Saved figure: {FIGURE_PATH}")


if __name__ == "__main__":
    main()

