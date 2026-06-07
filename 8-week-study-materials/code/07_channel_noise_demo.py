"""
Concept taught:
    Channel noise comes from random opening and closing of a limited number of
    channels. More channels can make the open fraction smoother, while fewer
    channels can look noisier.

What the student should notice:
    - A single channel is either open or closed in this simple model.
    - A small population has a bumpy open fraction.
    - A larger population looks smoother because random events average out.

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
FIGURE_PATH = FIGURE_DIR / "07_channel_noise_demo.png"


def simulate_channel_population(number_of_channels, open_probability, time_steps, rng):
    """Simulate open/closed states for a population of channels.

    Each entry is True if the channel is open during that time step.
    This is a coin-flip model, not a full channel biophysics model.
    """
    open_states = rng.random((time_steps, number_of_channels)) < open_probability
    open_fraction = open_states.mean(axis=1)
    return open_states, open_fraction


def main():
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(7)
    time_ms = np.arange(0, 300, 1)
    open_probability = 0.25

    small_states, small_fraction = simulate_channel_population(
        number_of_channels=10,
        open_probability=open_probability,
        time_steps=len(time_ms),
        rng=rng,
    )
    large_states, large_fraction = simulate_channel_population(
        number_of_channels=200,
        open_probability=open_probability,
        time_steps=len(time_ms),
        rng=rng,
    )

    # Use the first channel from the small population as a single-channel trace.
    single_channel_open = small_states[:, 0].astype(float)

    fig, axes = plt.subplots(3, 1, figsize=(8, 6), sharex=True)

    axes[0].step(time_ms, single_channel_open, where="post", color="#172033", linewidth=1.5)
    axes[0].set_ylabel("Open?")
    axes[0].set_yticks([0, 1])
    axes[0].set_yticklabels(["closed", "open"])
    axes[0].set_title("One channel jumps between closed and open")
    axes[0].grid(True, alpha=0.25)

    axes[1].plot(time_ms, small_fraction, color="#ea580c", linewidth=2)
    axes[1].axhline(open_probability, color="#64748b", linestyle="--", linewidth=1.5)
    axes[1].set_ylabel("Open fraction")
    axes[1].set_title("10 channels: bumpy open fraction")
    axes[1].grid(True, alpha=0.25)

    axes[2].plot(time_ms, large_fraction, color="#0f766e", linewidth=2)
    axes[2].axhline(open_probability, color="#64748b", linestyle="--", linewidth=1.5)
    axes[2].set_ylabel("Open fraction")
    axes[2].set_xlabel("Time (ms)")
    axes[2].set_title("200 channels: smoother open fraction")
    axes[2].grid(True, alpha=0.25)

    fig.suptitle("Channel noise from random opening and closing")
    fig.tight_layout()
    fig.savefig(FIGURE_PATH, dpi=180)
    plt.close(fig)

    print(f"Saved figure: {FIGURE_PATH}")
    print(f"Mean open fraction for 10 channels: {small_fraction.mean():.2f}")
    print(f"Mean open fraction for 200 channels: {large_fraction.mean():.2f}")


if __name__ == "__main__":
    main()

