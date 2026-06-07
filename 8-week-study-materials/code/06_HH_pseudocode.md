# 06. Hodgkin-Huxley Pseudocode

## Concept Taught

This note explains the logic of a Hodgkin-Huxley-style update without deriving the full differential equations. The goal is to understand what the model updates at each small time step: membrane voltage, channel openness, ionic currents, and the next voltage.

## Key Symbols

- `V_m`: membrane potential in mV.
- `E_Na`, `E_K`, `E_L`: reversal potentials for sodium, potassium, and leak pathways in mV.
- `g_Na`, `g_K`, `g_L`: conductances for sodium, potassium, and leak pathways.
- `I_app`: applied input current.
- `C_m`: membrane capacitance.
- `dt`: small time step.

## Beginner-Friendly Update Logic

Think of the model as a repeated checklist.

```text
Start with:
    V_m near rest
    Na+ channels mostly closed and ready
    K+ channels mostly closed
    leak pathway always partly present

For each small time step:

    1. Read the current voltage V_m.

    2. Use V_m to update channel openness.
       If V_m depolarizes, Na+ activation tends to increase quickly.
       K+ activation tends to increase more slowly.
       Na+ inactivation increases after depolarization.

    3. Convert channel openness into conductances.
       More open Na+ channels -> larger g_Na.
       More open K+ channels -> larger g_K.
       Leak conductance g_L is usually constant.

    4. Compute the current through each pathway.
       Na+ current depends on g_Na and (V_m - E_Na).
       K+ current depends on g_K and (V_m - E_K).
       Leak current depends on g_L and (V_m - E_L).

    5. Add the currents together with applied current I_app.
       The total current tells whether V_m should move up or down.

    6. Update V_m by a small amount.
       Capacitance C_m controls how strongly current changes voltage.

    7. Save V_m for plotting.

Repeat until the simulated time is finished.
```

## What This Is Not

This is not the full mathematical derivation of the Hodgkin-Huxley model. It is the computational story: voltage affects channel openness, channel openness affects currents, and currents affect the next voltage.

## Misconception To Avoid

The equations are not the biological mechanism by themselves. The mechanism is ion channels changing conductance and pulling membrane voltage toward reversal potentials. The equations are a compact way to describe that mechanism.

## Tiny Flowchart

```text
V_m
  -> channel openness
  -> g_Na and g_K
  -> ionic currents
  -> total current
  -> next V_m
  -> repeat
```

