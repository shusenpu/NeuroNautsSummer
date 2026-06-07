# Curated Teaching Datasets

This folder contains small, beginner-friendly datasets for the minibook *From neuron shape to noisy spike trains*.

The CSV files in this folder are synthetic. They were created for teaching spike timing, interspike interval (ISI), firing rate, and coefficient of variation (CV). They are not recordings from a real animal, person, or experiment.

## Files

| File | Source type | Main use |
| --- | --- | --- |
| `synthetic_spike_times_low_noise.csv` | Generated teaching data | Practice reading regular spike trains and low ISI variability. |
| `synthetic_spike_times_medium_noise.csv` | Generated teaching data | Practice comparing similar firing rates with more timing jitter. |
| `synthetic_spike_times_high_noise.csv` | Generated teaching data | Practice seeing how random-looking intervals can still have measurable structure. |
| `example_allen_cell_note.md` | Documentation only | Shows how to manually obtain one Allen Cell Types example without bundling third-party data. |
| `example_morphology_note.md` | Documentation only | Shows how to manually obtain one morphology example without bundling third-party data. |

## CSV Schema

Each spike-time file uses the same columns.

| Column | Meaning |
| --- | --- |
| `trial` | Repeated run number. Treat each trial as one response to the same stimulus. |
| `spike_index` | Spike number within that trial. |
| `spike_time_ms` | Time of the spike in milliseconds from the start of the trial. |
| `duration_ms` | Total duration of the trial in milliseconds. |
| `condition` | Teaching condition: low, medium, or high noise. |

## Student Calculations

Use one trial at a time.

1. ISI means interspike interval.
2. To find ISI, subtract each spike time from the next spike time.
3. Mean ISI is the average interval.
4. Firing rate in Hz is `number of spikes / duration in seconds`.
5. CV is `standard deviation of ISI / mean ISI`.

For a first pass, the student may estimate variability by eye before calculating CV. The important idea is that rate and timing regularity are different measurements.

## Suggested Chapter Connections

- Chapter 5: spike trains, firing rate, ISI, and raster plots.
- Chapter 7: noise, jitter, and CV.
- Chapter 8: final project practice with claim-evidence-reasoning.

## Provenance and Reuse

The three CSV files are locally generated synthetic teaching data and may be edited for this course. They should be labeled as synthetic whenever used in a figure or assignment.

No Allen Cell Types, NeuroMorpho.Org, textbook, or other third-party data files are bundled here. The two documentation notes explain how to obtain real examples manually from official source websites and how to cite or credit those sources.
