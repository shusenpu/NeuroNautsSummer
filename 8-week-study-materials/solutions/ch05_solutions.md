# Chapter 5 Solutions: Spike Trains and Neural Information

## Vocabulary

1. **Answer:** A spike train is a sequence of spike times. A raster plot shows spike times as tick marks across trials or conditions.  
   **Steps:** Define the data first: spike times. Then define the visual display: tick marks in rows.  
   **Why this answer makes sense:** Rasters are built from spike trains.

2. **Answer:** Firing rate is spike count divided by time, usually in Hz. ISI is the time between neighboring spikes, usually in ms.  
   **Steps:** For rate, count spikes and divide by seconds. For ISI, subtract neighboring spike times.  
   **Why this answer makes sense:** Rate summarizes how many spikes occur, while ISI describes timing between spikes.

## Graph Reading

3. **Answer:** The strong condition has the higher firing rate.  
   **Steps:** Both conditions use the same 1 s window. Strong has 9 spikes and weak has 3 spikes. More spikes in the same time means higher Hz.  
   **Why this answer makes sense:** Firing rate is spike count per second.

4. **Answer:** The timing pattern differs, especially the ISIs.  
   **Steps:** Notice that spike count and time window are the same, so rate is the same. Then compare spacing between spikes.  
   **Why this answer makes sense:** Same rate can hide different interval patterns.

## Short Explanation

5. **Answer:** Action potentials are mostly stereotyped in height, so stronger messages are often represented by more spikes, different timing, or more active neurons.  
   **Steps:** Start with all-or-none spike shape. Then name alternative coding features.  
   **Why this answer makes sense:** Chapter 4 showed that stronger input does not usually make one giant spike.

6. **Answer:** Firing rate is useful because it summarizes spike count over time, but it does not show exactly when spikes occurred.  
   **Steps:** State what rate captures. Then state what it loses: timing details.  
   **Why this answer makes sense:** Two spike trains can have the same Hz but different ISIs.

## Quantitative

7. **Answer:** The firing rate is 6 Hz.  
   **Steps:** Firing rate = 12 spikes / 2 s = 6 spikes/s = 6 Hz.  
   **Why this answer makes sense:** Hz means events per second.

8. **Answer:** The ISIs are 15 ms, 30 ms, and 35 ms.  
   **Steps:** 25 ms - 10 ms = 15 ms. 55 ms - 25 ms = 30 ms. 90 ms - 55 ms = 35 ms.  
   **Why this answer makes sense:** ISIs are the gaps between neighboring spike times.

## Challenge Extension

9. **Answer:** Example A: spikes at 100, 300, 500, 700, 900 ms. Example B: spikes at 100, 120, 140, 800, 840 ms. Both have 5 spikes in 1 s, so both are 5 Hz, but A is more regular and B is clustered.  
   **Steps:** Keep spike count and time window the same. Change the spacing. Calculate rate for both: 5 spikes / 1 s = 5 Hz.  
   **Why this answer makes sense:** Firing rate can match while timing pattern differs.

