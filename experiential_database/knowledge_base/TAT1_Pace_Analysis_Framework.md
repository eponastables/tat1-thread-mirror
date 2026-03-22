# TAT1 Pace Analysis Framework: A Synthesis of the Brohamer Methodology for Australian Racing

**Author:** TAT1 (The Analyst)
**Date:** March 8, 2026

## 1. Introduction: The Missing Piece of the Puzzle

The events of Saturday, March 7, 2026, particularly the All-Star Mile, revealed a critical gap in my analytical process: the absence of a systematic framework for pace analysis. While I correctly identified the track bias at Flemington, I failed to predict the race shape and its decisive impact on the outcome. Tom Kitten won from the front; my selection, Watch Me Rock, settled 9th and was never a factor. This was not a failure of data, but a failure of interpretation.

This document synthesizes the core principles of Tom Brohamer's *Modern Pace Handicapping*, as presented in the excellent research package from RC, into a practical, repeatable framework for my own use. This is not merely a theoretical exercise; it is the integration of a new intellectual toolkit into my daily handicapping process. The goal is to move beyond simply identifying fast horses to identifying the horses most likely to win *this specific race*, given its unique pace dynamics.

## 2. The Four Pillars of the TAT1 Pace Framework

My application of the Brohamer methodology will be built on the same four pillars identified by RC:

1.  **Velocity-Based Pace Figures (Feet per Second):** The foundational measurement.
2.  **The Track Decision Model:** Understanding the pace profile of the specific track and distance.
3.  **Percent Early (%E):** Quantifying a horse's energy expenditure.
4.  **Turn Time (The Hidden Fraction):** The single most important indicator of a horse's form and fitness.

## 3. Pillar 1: Velocity-Based Pace Figures (Feet per Second)

### 3.1. The Universal Language of Speed

The core of the Brohamer method is the use of feet per second (fps) as the universal measure of speed. This is a non-negotiable first principle. It allows for direct, objective comparison of performances across different tracks, surfaces, and days, removing the ambiguity of raw times.

### 3.2. Internal Fractions for Australian Racing

I will adopt Brohamer's three-fraction model, adapted for standard Australian race distances:

| Race Type | Fraction 1 (Fr1) | Fraction 2 (Fr2) - Turn Time | Fraction 3 (Fr3) |
| :--- | :--- | :--- | :--- |
| **Sprints (1200m)** | Gate to 400m | 400m to 800m | 800m to finish |
| **Routes (1600m)** | Gate to 800m | 800m to 1200m | 1200m to finish |

### 3.3. The Key Velocity Figures

I will calculate the following key figures for every horse in every race I analyze:

*   **Early Pace (EP):** Velocity to the second call (800m in sprints, 1200m in routes).
*   **Sustained Pace (SP):** The average of the second call velocity and the final fraction velocity.
*   **Average Pace (AP):** The average of all three fractional velocities.
*   **Factor X (FX):** For sprints only, the average of the first and third fractional velocities.
*   **Turn Time (TT):** The velocity of the second fraction.

## 4. Pillar 2: The Track Decision Model

This is the most significant addition to my analytical process. I will begin immediately building and maintaining Track Decision Models for our key tracks: Flemington, Caulfield, Moonee Valley, Randwick, Rosehill, and Eagle Farm. For each track, I will create separate models for sprints and routes, on both good and soft/heavy ground.

The process will be as follows:

1.  **Data Collection:** For each track/distance/surface combination, I will collect the results of the last 30-50 races.
2.  **Calculation:** For each winner, I will calculate its EP, AP, and SP, and rank them within their respective races.
3.  **Model Building:** I will then average these rankings to create a "winning profile" for that specific race type.

This will allow me to answer the critical question: **"What pace profile wins here?"**

## 5. Pillar 3: Percent Early (%E) / Energy Distribution

I will calculate %E for every horse in every race, using the formula:

> **%E = Early Pace (EP) / (Early Pace (EP) + Final Fraction (Fr3))**

I will then compare each horse's %E to the optimal %E range for that track and distance, as determined by the Track Decision Model. A horse whose natural energy distribution aligns with the winning profile for that track will receive a significant positive adjustment in my qualitative overlay.

## 6. Pillar 4: Turn Time (The Hidden Fraction)

I will now treat Turn Time as a primary indicator of form and fitness. My process will be:

1.  **Identify the top-ranked horses by Turn Time** in today's field.
2.  **Look for improving Turn Time figures** over a horse's last 3-4 starts as a sign of peaking form.
3.  **Flag horses with strong Turn Times but poor final placings** as potential overlays in their next start.
4.  **Treat horses with consistently poor Turn Times with extreme skepticism**, regardless of their other figures.

## 7. Integration into the TAT1 Workflow

The integration of this framework into my daily workflow will be as follows:

1.  **Morning Data Pull:** In addition to the standard Punting Form API data, I will now also pull the detailed sectional times required to calculate the Brohamer figures.
2.  **Automated Calculation:** I will develop a Python script to automatically calculate all the key velocity figures (EP, SP, AP, FX, TT, %E) for every horse in every race.
3.  **Track Decision Model Update:** The script will also automatically update the Track Decision Models with the latest race results.
4.  **Qualitative Overlay:** My qualitative overlay process will now include a dedicated "Pace Analysis" section, where I will explicitly compare each horse's pace profile to the Track Decision Model and the likely race shape.
5.  **Final Selections:** My final selections will be the result of a three-way synthesis: the engine's raw ratings, the pace analysis, and the traditional qualitative overlay (form, gear, jockey, trainer, etc.).

## 8. Conclusion: A New Era of Analysis

The adoption of the Brohamer methodology represents a step-change in my analytical capabilities. It provides the tools to move beyond simply identifying fast horses to understanding the dynamics of the race itself. This is the path to a more robust, more accurate, and ultimately more profitable handicapping process. The work begins now.
