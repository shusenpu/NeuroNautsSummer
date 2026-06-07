# Chapter 7 Solutions: Channel Noise and Spike-Time Variability

## Vocabulary

1. **Answer:** Stochastic gating means channel opening and closing have probabilistic timing. Channel noise is variability caused by random timing of finite channel openings.  
   **Steps:** Define the timing rule first. Then connect many such events to variability.  
   **Why this answer makes sense:** Individual channel events are uncertain in exact timing but still follow biological rules.

2. **Answer:** Open fraction is time open divided by total recording time. CV is standard deviation divided by mean.  
   **Steps:** Write each as a ratio. Open fraction uses time open and total time. CV uses spread and mean.  
   **Why this answer makes sense:** Both quantities compare one measurement with a relevant total or average.

## Graph Reading

3. **Answer:** 0 pA likely represents closed, and -2 pA likely represents open.  
   **Steps:** In a simple single-channel trace, closed often means no current, or 0 pA. A step away from 0 pA indicates current through an open channel.  
   **Why this answer makes sense:** Opening a channel creates a measurable current step.

4. **Answer:** Condition B has more spike-time jitter.  
   **Steps:** Compare alignment across trials. Tightly aligned spikes mean low jitter. Spread-out spike times mean high jitter.  
   **Why this answer makes sense:** Jitter describes variation in timing across repeated trials.

## Short Explanation

5. **Answer:** Random channel timing still depends on channel structure, voltage, and conditions; random means the exact opening time is uncertain.  
   **Steps:** Name the mechanism. Then define what is uncertain.  
   **Why this answer makes sense:** A process can have causes and still be probabilistic.

6. **Answer:** Model output comes from assumptions and code, while direct biological evidence comes from measurements of real cells or tissue.  
   **Steps:** Identify the source of the graph. If it is simulated, call it model output. If it is recorded, call it biological evidence.  
   **Why this answer makes sense:** A model can support a mechanism but cannot by itself prove that every real neuron behaves the same way.

## Quantitative

7. **Answer:** The open fraction is 0.20.  
   **Steps:** Open fraction = time open / total time = 18 ms / 90 ms = 0.20.  
   **Why this answer makes sense:** The channel was open for one fifth of the recording time.

8. **Answer:** CV = 0.30.  
   **Steps:** CV = SD / mean = 12 ms / 40 ms = 0.30. The ms units cancel, so CV has no unit.  
   **Why this answer makes sense:** The interval spread is 30 percent of the mean interval.

## Challenge Extension

9. **Answer:** Near threshold, a small voltage fluctuation can change whether threshold is crossed now or later; far below threshold, the same fluctuation may still leave V_m below threshold.  
   **Steps:** Compare distance from threshold. Close distance means small noise can matter. Large distance means the same noise may not be enough.  
   **Why this answer makes sense:** Spike timing depends strongly on when V_m crosses threshold.

