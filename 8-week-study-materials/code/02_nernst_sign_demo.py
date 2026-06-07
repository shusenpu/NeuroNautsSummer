"""
Concept taught:
    The Nernst equation connects an ion's outside/inside concentration ratio
    to the sign of that ion's equilibrium potential.

What the student should notice:
    - If outside/inside = 1, the concentration ratio alone gives 0 mV.
    - If outside/inside is below 1 for a +1 ion, the value is negative.
    - If outside/inside is above 1 for a +1 ion, the value is positive.

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
FIGURE_PATH = FIGURE_DIR / "02_nernst_sign_demo.png"


def nernst_mV(outside_mM, inside_mM, charge_z=1, factor_mV=61.0):
    """Approximate Nernst equilibrium potential at body temperature.

    This beginner form is enough for sign and calculator practice.
    It assumes a single ion and uses log10.
    """
    if outside_mM <= 0 or inside_mM <= 0:
        raise ValueError("Concentrations must be positive numbers.")
    if charge_z == 0:
        raise ValueError("Ion charge cannot be zero.")
    return (factor_mV / charge_z) * np.log10(outside_mM / inside_mM)


def main():
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    ratios = np.logspace(-2, 2, 400)
    equilibrium_mV = 61.0 * np.log10(ratios)

    # Illustrative values used throughout the book.
    k_out, k_in = 5.0, 140.0
    na_out, na_in = 145.0, 12.0
    e_k = nernst_mV(k_out, k_in)
    e_na = nernst_mV(na_out, na_in)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.semilogx(ratios, equilibrium_mV, linewidth=3, color="#0f766e")
    ax.axhline(0, color="#172033", linewidth=1.5)
    ax.axvline(1, color="#64748b", linewidth=1.5, linestyle="--")

    ax.scatter([k_out / k_in], [e_k], color="#ea580c", s=80, zorder=3)
    ax.text(k_out / k_in, e_k - 16, f"K+ example\n{e_k:.0f} mV", ha="center")

    ax.scatter([na_out / na_in], [e_na], color="#2563eb", s=80, zorder=3)
    ax.text(na_out / na_in, e_na + 8, f"Na+ example\n{e_na:.0f} mV", ha="center")

    ax.set_xlabel("[outside] / [inside]")
    ax.set_ylabel("Equilibrium potential (mV)")
    ax.set_title("Nernst sign demo for a +1 ion")
    ax.grid(True, which="both", alpha=0.25)
    ax.text(0.035, 55, "ratio below 1 -> negative", fontsize=11)
    ax.text(2.0, -60, "ratio above 1 -> positive", fontsize=11)
    fig.tight_layout()
    fig.savefig(FIGURE_PATH, dpi=180)
    plt.close(fig)

    print(f"Saved figure: {FIGURE_PATH}")
    print(f"Illustrative E_K = {e_k:.1f} mV")
    print(f"Illustrative E_Na = {e_na:.1f} mV")


if __name__ == "__main__":
    main()

