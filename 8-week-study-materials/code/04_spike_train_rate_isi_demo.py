"""
Concept taught:
    Spike trains can be described by firing rate and interspike intervals.

What the student should notice:
    - Firing rate counts spikes per second.
    - ISI means the time between neighboring spikes.
    - Two trials can have similar spike counts but different timing.

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
FIGURE_PATH = FIGURE_DIR / "04_spike_train_rate_isi_demo.png"


def firing_rate_hz(spike_times_ms, window_ms):
    """Return spike count per second."""
    seconds = window_ms / 1000.0
    return len(spike_times_ms) / seconds


def main():
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    window_ms = 100.0
    trial_1 = np.array([10, 24, 38, 53, 67])
    trial_2 = np.array([8, 29, 37, 58, 66])

    isi_1 = np.diff(trial_1)
    isi_2 = np.diff(trial_2)

    rate_1 = firing_rate_hz(trial_1, window_ms)
    rate_2 = firing_rate_hz(trial_2, window_ms)

    fig, (ax_raster, ax_hist) = plt.subplots(
        2, 1, figsize=(8, 5), gridspec_kw={"height_ratios": [1, 1.2]}
    )

    # Raster plot: each vertical mark means "a spike happened here."
    for y, spikes, color, label in [
        (2, trial_1, "#0f766e", f"trial 1: {rate_1:.0f} Hz"),
        (1, trial_2, "#ea580c", f"trial 2: {rate_2:.0f} Hz"),
    ]:
        ax_raster.vlines(spikes, y - 0.35, y + 0.35, color=color, linewidth=3)
        ax_raster.text(104, y, label, va="center")

    ax_raster.set_xlim(0, 130)
    ax_raster.set_ylim(0.4, 2.6)
    ax_raster.set_yticks([1, 2])
    ax_raster.set_yticklabels(["Trial 2", "Trial 1"])
    ax_raster.set_xlabel("Time (ms)")
    ax_raster.set_title("Spike rasters: same count can hide timing differences")
    ax_raster.grid(True, axis="x", alpha=0.25)

    bins = np.arange(0, 36, 5)
    ax_hist.hist(isi_1, bins=bins, alpha=0.7, label="trial 1 ISIs", color="#0f766e")
    ax_hist.hist(isi_2, bins=bins, alpha=0.7, label="trial 2 ISIs", color="#ea580c")
    ax_hist.set_xlabel("Interspike interval (ms)")
    ax_hist.set_ylabel("Count")
    ax_hist.set_title("ISI histogram")
    ax_hist.legend()
    ax_hist.grid(True, alpha=0.25)

    fig.tight_layout()
    fig.savefig(FIGURE_PATH, dpi=180)
    plt.close(fig)

    print(f"Saved figure: {FIGURE_PATH}")
    print(f"Trial 1 rate: {rate_1:.1f} Hz; ISIs: {isi_1.tolist()} ms")
    print(f"Trial 2 rate: {rate_2:.1f} Hz; ISIs: {isi_2.tolist()} ms")


if __name__ == "__main__":
    main()

