# Tiny Code Snippets

These snippets are short enough to read aloud. They are not meant to replace the notebooks; they show the smallest useful calculation behind the book.

## mV Change

```python
start_mV = -70
end_mV = -55
change_mV = end_mV - start_mV

print(change_mV, "mV")
print("depolarized" if change_mV > 0 else "hyperpolarized")
```

**Interpretation:** -55 mV is less negative than -70 mV, so the change is +15 mV and the membrane depolarized.

## Threshold Detection

```python
V_m = [-70, -66, -61, -56, -54, -20, 25]
threshold = -55

for i, v in enumerate(V_m):
    if v >= threshold:
        print("threshold crossed at index", i, "with V_m =", v, "mV")
        break
```

**Interpretation:** The first crossing matters because it marks when spike feedback begins in the simplified story.

## Interspike Intervals

```python
spike_times_ms = [10, 24, 38, 53, 67]
isi_ms = []

for a, b in zip(spike_times_ms[:-1], spike_times_ms[1:]):
    isi_ms.append(b - a)

print(isi_ms)
print("mean ISI =", sum(isi_ms) / len(isi_ms), "ms")
```

**Interpretation:** ISIs turn spike timing into numbers that can be compared across trials.

## One LIF Update Step

```python
V_m = -70.0
rest = -70.0
tau_ms = 20.0
input_drive = 18.0
dt_ms = 0.1

leak = (rest - V_m) / tau_ms
dV = (leak + input_drive / tau_ms) * dt_ms
V_m = V_m + dV

print(round(V_m, 3), "mV")
```

**Interpretation:** This tiny update says voltage changes a little each time step because leak and input do not perfectly balance.
