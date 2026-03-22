# Modern Pace Handicapping: A Definitive Guide to the Brohamer Methodology

**Source:** DeepSeek Racing Specialist
**Date:** March 8, 2026

**Note for TAT1:** This document is a supplemental text provided by DeepSeek. It is a comprehensive guide to the Brohamer methodology and should be read in conjunction with the primary synthesis document prepared by RC.

---

## Introduction

Tom Brohamer's *Modern Pace Handicapping* stands as one of the most influential works in the history of thoroughbred racing analysis. As a key proponent of the Sartin Methodology (often referred to as "The Sartin Methodology" or "Phase III"), Brohamer translated complex mathematical concepts into a practical, repeatable framework for identifying contenders through velocity-based pace analysis.

This guide synthesizes Brohamer's core teachings with insights from practitioners who have implemented these methods in real-world handicapping. It is structured for an advanced audience seeking to understand both the theoretical foundation and practical application of velocity-based pace figures.

## Part 1: Velocity-Based Pace Figures

### 1.1 Why Feet Per Second?

Brohamer's insistence on using feet per second (fps) as the foundational unit of measurement stems from a fundamental limitation of time-based figures: distance is fixed, but time is variable. A horse running on a slow track may earn a slower final time than a horse on a fast track, yet the slower-timed horse might have actually traveled at a higher velocity due to track conditions.

Feet per second provides a universal, surface-agnostic measure of a horse's true speed. By converting all performances into fps, the handicapper can make direct comparisons across different tracks, surfaces, and days. The formula is elegantly simple:

> **Velocity (fps) = Distance (feet) / Time (seconds)**

A standard length is considered 10 feet in these calculations, allowing beaten lengths to be converted into distance adjustments.

### 1.2 Fraction Distances: Sprints vs. Routes

The distance covered in each fractional segment differs based on race type. Brohamer divides races into three fractions (Fr1, Fr2, Fr3):

| Race Type | Fr1 Distance | Fr2 Distance | Fr3 Distance |
| :--- | :--- | :--- | :--- |
| Sprint (6f) | Gate to 2f (1,320 ft) | 2f to 4f (1,320 ft) | 4f to finish (1,320 ft) |
| Route (8f/1 mile) | Gate to 4f (2,640 ft) | 4f to 6f (1,320 ft) | 6f to finish (2,640 ft) |

For routes, note that the first and third fractions are double the distance of sprints, which has important implications for energy distribution calculations.

### 1.3 Calculating Fractional Velocities

The methodology for calculating each fraction's velocity requires careful attention to beaten lengths. Here is the precise step-by-step process:

**Step 1: Gather Raw Data**

For each horse, you need:

*   Time at first call (e.g., 22.2 seconds)
*   Time at second call (e.g., 45.3 seconds)
*   Final time (e.g., 70.5 seconds)
*   Beaten lengths at each call

**Step 2: Convert Beaten Lengths to Feet**

1 length = 10 feet (standard conversion)

For a horse that is 3 lengths behind at the first call:

*   Distance adjustment = 3 × 10 = 30 feet behind
*   Actual distance traveled to first call = 1,320 + 30 = 1,350 feet

**Step 3: Calculate Fractional Times**

*   Fr1 Time = Time at first call (already known)
*   Fr2 Time = Time at second call - Time at first call
*   Fr3 Time = Final time - Time at second call

**Step 4: Calculate Distance per Fraction with Beaten Length Adjustments**

*   **For Fr1:**
    *   Distance = Standard Fr1 distance + (BL at first call × 10)
*   **For Fr2:**
    *   Distance = Standard Fr2 distance + [(BL at second call - BL at first call) × 10]
*   **For Fr3:**
    *   Distance = Standard Fr3 distance + [(BL at finish - BL at second call) × 10]

**Critical Note on Beaten Lengths:** When a horse gains ground during a fraction, the adjustment becomes negative, effectively increasing the distance traveled. For example, if a horse is 5 lengths behind at the second call but only 1 length behind at the third call, the Fr3 distance calculation becomes:

> Standard Fr3 distance + [(1 - 5) × 10] = Standard Fr3 distance - 40 feet

This reflects that the horse ran a shorter path (relative to the leader) while making up ground.

**Step 5: Calculate FPS for Each Fraction**

*   Fr1 fps = Adjusted Fr1 distance / Fr1 time
*   Fr2 fps = Adjusted Fr2 distance / Fr2 time
*   Fr3 fps = Adjusted Fr3 distance / Fr3 time

### 1.4 Example Calculation (6 Furlong Sprint)

Using the Brisnet example:

| Fraction | Distance (ft) | Time (sec) | FPS |
| :--- | :--- | :--- | :--- |
| Fr1 | 1,320 | 22.2 | 59.46 |
| Fr2 | 1,320 | 23.1 | 57.14 |
| Fr3 | 1,320 | 25.2 | 52.38 |

*Total race time: 70.5 seconds*

These base figures assume the horse was the leader at each call. For non-leaders, the distance adjustments described above would be applied.

## Part 2: The Core Velocity Ratings

Brohamer developed several compound ratings that synthesize the fractional velocities into meaningful performance measures.

### 2.1 Early Pace (EP)

*   **Definition:** EP measures a horse's velocity from the start to the second call (the first half of the race).
*   **What It Measures:** A horse's ability to position itself early and maintain speed through the middle stages.
*   **Formula:**
    *   EP = Distance to second call / Time to second call
    *   For a sprint: EP = 2,640 feet / Time at second call
    *   For a route: EP = 3,960 feet / Time at second call (gate to 6f)
*   **Example (sprint):** If a horse reaches the second call (4f) in 45.3 seconds:
    *   EP = 2,640 / 45.3 = 58.28 fps

### 2.2 Sustained Pace (SP)

*   **Definition:** SP represents the average of a horse's early pace and its final fraction, providing a measure of its ability to sustain speed throughout the race.
*   **What It Measures:** A horse's capacity to combine early position with a strong finish.
*   **Formula:**
    *   SP = (EP + Fr3 fps) / 2
*   **Example:** Using the figures from above:
    *   SP = (58.28 + 52.38) / 2 = 55.33 fps

### 2.3 Average Pace (AP)

*   **Definition:** AP is the average velocity across all three fractions.
*   **What It Measures:** Overall speed consistency throughout the race.
*   **Formula (Sprints):**
    *   AP = (Fr1 fps + Fr2 fps + Fr3 fps) / 3
*   **Formula (Routes):**
    *   AP = (EP + SP) / 2
*   **Example (sprint):**
    *   AP = (59.46 + 57.14 + 52.38) / 3 = 56.33 fps

### 2.4 Total Speed

*   **Definition:** Total Speed is simply the horse's average velocity for the entire race.
*   **What It Measures:** Raw speed without regard to pace distribution.
*   **Formula:**
    *   Total Speed = Total race distance / Final time
    *   For a 6f sprint: Total Speed = 7,920 feet / Final time

### 2.5 Factor X (FX)

*   **Definition:** Factor X is a sprint-specific rating that excludes the second fraction, emphasizing a horse's early speed and final kick while de-emphasizing its ability to carry speed around the turn.
*   **What It Measures:** A horse's "turn-independent" speed capability.
*   **Formula:**
    *   Factor X = (Fr1 fps + Fr3 fps) / 2
*   **Importance in Dirt Sprints:** Factor X is particularly valuable in dirt sprints because it helps identify horses that may be compromised by a poor turn time due to traffic or racing wide, but still possess the underlying speed to compete. A horse with a high Factor X but poor Fr2 may have encountered trouble on the turn and could be an overlay in its next start.
*   **Example:**
    *   Factor X = (59.46 + 52.38) / 2 = 55.92 fps

## Part 3: The Strategic Framework

### 3.1 The Track Decision Model

**Purpose and Function**

The Track Decision Model serves as a contextual lens through which raw velocity figures gain meaning. A horse's EP of 58.28 fps is meaningless without understanding what that figure typically achieves at today's track, distance, and surface.

Brohamer recognized that every track has its own "pace personality" based on:

*   Physical configuration (tight turns, long stretches)
*   Surface composition (deep sand, packed dirt, turf)
*   Rail position
*   Weather patterns

The Decision Model answers the question: "What pace profile wins here?"

**Building the Model**

To construct a Track Decision Model for a specific track, surface, and distance:

1.  **Collect Data:** Gather results from 30-50 recent races at that track/distance/surface combination.
2.  **Calculate Ratings:** For each winner and placed horse, compute EP, AP, and SP.
3.  **Rank Within Race:** For each race, rank the contenders (1 = fastest, 2 = second fastest, etc.) for each rating.
4.  **Average the Rankings:** Calculate the average winning rank for EP, AP, and SP.

**Example Decision Model for One-Mile Dirt Routes at Calder:**

| Finish | EP Rank | AP Rank | SP Rank | Total |
| :--- | :--- | :--- | :--- | :--- |
| Win Model | 4 | 3 | 2 | 9 |
| Place Model | 4 | 4 | 5 | 13 |

*Interpretation:* At Calder in one-mile dirt routes, the average winner has an EP rank of 4th, an AP rank of 3rd, and an SP rank of 2nd. This tells us that while early speed is helpful (4th), the ability to sustain pace (SP rank 2nd) is even more critical. The total of 9 is a benchmark—horses whose total of EP+AP+SP ranks is near 9 are well-aligned with the winning profile.

**Identifying the "Winning Profile"**

Once the model is built, you can evaluate today's contenders:

1.  Calculate EP, AP, and SP for each horse using an appropriate paceline.
2.  Rank them within today's field.
3.  Sum the ranks for each horse.
4.  Compare each horse's total to the model's winning total.

Horses whose rank totals closely match the model's winning total are statistically more likely to win. Those with totals significantly higher (worse ranks) face an uphill battle against the track's inherent bias.

### 3.2 Percent Early (%E) / Energy Distribution

**The Concept of Energy Distribution**

Brohamer and the Sartin Methodology introduced the revolutionary concept that how a horse expends its energy is as important as how fast it runs. A horse that burns too much energy early may have nothing left for the finish, while one that conserves too much may leave its run too late.

**Formula for Percent Early**

> Total Energy = EP + Fr3 fps
> %E = EP / Total Energy

**Example:**

> Total Energy = 58.28 + 52.38 = 110.66
> %E = 58.28 / 110.66 = 52.67%

This 52.67% means the horse expended approximately 52.7% of its total energy in the first half of the race, leaving 47.3% for the final fraction.

**What %E Signifies**

*   **High %E (54%+):** Early burner, likely to be on or near the lead. Vulnerable to late runners if pressed early.
*   **Mid %E (51-53%):** Balanced energy distribution. Adaptable to various pace scenarios.
*   **Low %E (below 50%):** Deep closer. Needs fast early pace to run into.

**Integrating %E with the Track Decision Model**

Just as with velocity ratings, Brohamer advocates building %E Models for each track/distance:

| %E Zone | Win Horses | Place Horses |
| :--- | :--- | :--- |
| Low %E | 50.9% | 51.4% |
| Median %E | 52.0% | 52.3% |
| High %E | 52.9% | 53.3% |

**Application:**

1.  Calculate each horse's %E from its best representative race.
2.  Compare to the track's %E ranges for winners.
3.  Horses whose %E matches the winning profile receive a positive adjustment.

### 3.3 Turn Time (The "Hidden Fraction")

**Why Turn Time Matters Most**

Brohamer and Sartin considered the second fraction (Turn Time) the most critical indicator of a horse's form and fitness for a profound reason: it's the only fraction where the horse must run on a curve while maintaining speed.

The turn imposes unique demands:

*   Balance and coordination under centrifugal force
*   Ability to maintain speed while changing leads
*   Mental focus to navigate tight quarters
*   Physical strength to hold position

A horse with a strong turn time demonstrates it can handle these demands while maintaining velocity. This is why turn time often separates genuine contenders from pretenders.

**Using Turn Time to Identify Peaking Form**

A horse rounding into peak form will typically show improving turn times over its last 3-4 starts, even if final times remain static. This pattern indicates:

*   Increasing fitness and stamina
*   Better balance and coordination
*   Growing confidence from the horse and jockey

**Example Progression:**

| Start | Fr2 (fps) | Final Time | Comment |
| :--- | :--- | :--- | :--- |
| 4 back | 56.2 | 71.0 | Just getting fit |
| 3 back | 56.8 | 71.2 | Turn time improving |
| 2 back | 57.4 | 70.8 | Sharp turn, better final |
| Last | 58.1 | 70.5 | Peak turn, career-best final |

**Uncovering Hidden Ability**

A horse with a strong turn time but modest final time may have encountered trouble in the stretch or raced on a tiring surface. The strong turn time reveals underlying ability that wasn't reflected in the final result.

*Example:* Horse runs Fr2 of 58.5 fps (top in field) but fades to 5th. Next start, with cleaner trip or better surface, this horse could win at a price.

**Eliminating False Contenders**

Conversely, a horse that appears strong on paper (good final times, classy connections) but shows consistently poor turn times is often a "false favorite." The poor turn time indicates an inability to handle the track's most demanding segment, making victory unlikely regardless of other factors.

**Caveats and Limitations**

The primary caveat with turn time analysis is over-valuing deep closers. A deep closer may have a modest turn time simply because it was saving ground 15 lengths back, not because it lacks ability. In such cases, the turn time must be interpreted in context of running position. Some practitioners argue that turn time should be adjusted for running position—a horse 8 lengths back on the turn is running a different race than one pressing the leader.

### 3.4 The Integrated Handicapping Process

Here is a step-by-step synthesis of the Brohamer method, walking through a hypothetical race:

**Race:** 6-furlong dirt sprint at Churchill Downs

**Step 1: Build/Update Track Models**

Before handicapping individual races, consult your pre-built Track Decision Model and %E Model for CD 6f dirt sprints. Let's assume:

*   Win Model: EP rank 3, AP rank 4, SP rank 2 (Total 9)
*   %E Zone for winners: 51.5% - 53.0%

**Step 2: Select Pacelines for Each Contender**

For each of the 10 horses, select the most representative recent race at similar distance/surface. For first-time starters or drastic class changes, use workouts or a race at a different distance with appropriate adjustments.

**Step 3: Calculate Velocity Figures**

For each horse, compute:

*   Fr1, Fr2, Fr3 fps
*   EP, AP, SP, Factor X (for sprints)
*   %E
*   Turn Time (Fr2)

**Step 4: Rank Contenders Within Today's Field**

| Horse | EP Rank | AP Rank | SP Rank | Total | %E | Turn Time (fps) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| A | 2 | 1 | 1 | 4 | 52.8% | 58.2 |
| B | 1 | 3 | 4 | 8 | 54.1% | 57.4 |
| C | 4 | 2 | 3 | 9 | 52.1% | 57.9 |
| D | 3 | 5 | 2 | 10 | 51.2% | 58.5 |
| E | 5 | 4 | 5 | 14 | 50.1% | 56.8 |

**Step 5: Apply Track Decision Model**

Compare each horse's total to the Win Model total of 9:

*   Horse A (total 4): Better than model - strong contender but maybe overqualified
*   Horse B (total 8): Very close to model - fits winning profile
*   Horse C (total 9): Perfect match - prime contender
*   Horse D (total 10): Slightly off model - needs help
*   Horse E (total 14): Unlikely winner

**Step 6: Apply %E Model**

Winning %E zone: 51.5-53.0%

*   Horse A: 52.8% ✓ In zone
*   Horse B: 54.1% ✗ Above zone - may burn out
*   Horse C: 52.1% ✓ In zone
*   Horse D: 51.2% ✗ Slightly below - may leave run late
*   Horse E: 50.1% ✗ Well below - pace dependent

**Step 7: Analyze Turn Time**

*   Horse D has the best turn time (58.5 fps) - hidden ability despite being slightly off %E model
*   Horse A and C both strong (58.2, 57.9)
*   Horse B's turn time (57.4) weaker than expected for a front-runner

**Step 8: Integrate and Identify Prime Contenders**

*   **Primary Contenders:**
    *   Horse C: Perfect model match, ideal %E, strong turn time - **TOP PICK**
    *   Horse A: Better-than-model figures, ideal %E, strong turn - win contender but may be overbet
*   **Secondary Contenders:**
    *   Horse D: Best turn time, slightly off %E model - major exotic contender and possible overlay if odds allow
*   **Eliminations:**
    *   Horse B: High %E, weaker turn time - vulnerable favorite
    *   Horse E: Poor across all measures - toss

**Step 9: Betting Decision**

*   Horse C at 4-1 or higher: Win bet
*   Horse D at 8-1 or higher: Small win bet or key in exotics
*   Exotic wagers: Key Horse C over/with Horses A and D

## Part 4: Advanced Nuances & Legacy

### 4.1 Advanced Considerations

**The First Fraction Controversy**

A significant debate among practitioners concerns the accuracy of first fraction calculations. The issue stems from run-up distances—the distance from the starting gate to the point where electronic timing begins.

At many tracks, the timing beam is not activated at the moment the gates open. Instead, it's placed at a variable distance (often 30-80 feet) past the gate. This means:

*   Horses are already moving when timing begins
*   First fraction times are artificially fast
*   True first fraction velocity is impossible to calculate without knowing the exact run-up distance

*Implications:*

*   Some handicappers use first fraction primarily for running style identification rather than velocity comparison.
*   Professional figures (like those from TrackMaster or HTR) apply track-specific run-up adjustments.
*   For shippers, comparing first fractions across tracks requires adjustment factors.

*Expert Consensus:* Use first fraction for positional analysis, rely on EP (which includes second fraction) for velocity comparisons.

**The Holmes Alternative**

Tommy Holmes proposed an alternative to Brohamer's Average Pace that some practitioners prefer. Holmes' formula uses:

*   Leader's time for first and second calls
*   The specific horse's final time

This approach gives more weight to the actual pace of the race rather than the horse's individual early fractions. Some argue this better identifies horses who perform well in fast-paced races.

*Debate:* Brohamer proponents counter that using the horse's own fractions is essential for understanding its individual energy distribution. The choice ultimately reflects whether you prioritize race context (Holmes) or individual capability (Brohamer).

**Paceline Selection Complexity**

The Brohamer method's accuracy depends critically on selecting the right paceline for each horse. Advanced practitioners develop sophisticated paceline selection criteria:

*   Recency weighting (more recent races weighted higher)
*   Surface/distance matching
*   Class level alignment
*   Track condition similarity
*   "Off form" detection and exclusion

Modern software (HTR, ALL-Ways) automates this with sophisticated algorithms, but manual handicappers must develop consistent rules.

### 4.2 Legacy and Modern Influence

**Influence on Commercial Data Providers**

Brohamer's work fundamentally shaped how pace data is presented to handicappers:

*   **Brisnet:** Provides "Brohamer Pace Ratings" including EP, SP, AP, and FX in their premium data products. Their "Ultimate PP" includes dedicated pace figures derived from the Brohamer methodology.
*   **TrackMaster:** Offers "Velocity Pace Ratings" that calculate feet-per-second figures for each fraction, directly implementing Brohamer's core concepts.
*   **HDW/TimeformUS:** Provides sectional times and velocity figures that allow handicappers to compute Brohamer-style ratings from raw data.
*   **HTR (Handicapper's Thoroughbred Racing Software):** Ken Massa, co-author of the original MPH software, built HTR around Brohamer/Sartin concepts. HTR's "FPS Screen" displays fractional velocities, EP, AP, SP, and %E for every horse, with automated track-to-track adjustments.
*   **ALL-Ways Handicapping Software:** Received explicit permission from both Howard Sartin and Tom Brohamer to include their methodology. ALL-Ways automatically calculates all Brohamer figures, maintains Track Decision Models, and presents results on the "Brohamer Plus Report".

**Modern Synthesis**

Today's sophisticated handicappers rarely calculate Brohamer figures manually. Instead, they:

*   Subscribe to data services that provide pre-calculated velocity figures
*   Use software that automatically maintains track models
*   Focus on interpretation and integration with other factors

However, understanding the underlying methodology remains essential for:

*   Evaluating software outputs critically
*   Recognizing when standard adjustments may be insufficient
*   Developing customized variations for specific tracks or race types

### 4.3 Brohamer's Philosophy in His Own Words

While direct quotes from Brohamer are scarce in available literature, his philosophy is consistently reflected in practitioner discussions:

> "The pace of the race is the engine that drives the final result. Without understanding how the race was run, you're just guessing." (paraphrased from multiple sources)

> "Most handicappers look at final time and see a number. We look at fractions and see a story—a story of energy, effort, and execution." (attributed in forum discussions)

> "The turn is where races are won and lost. Watch the turn, and you'll see who's really running." (commonly cited in Sartin Methodology materials)

The essence of Brohamer's approach is objectivity through quantification. By converting subjective observations (he ran well) into precise measurements (58.2 fps on the turn), the handicapper gains a repeatable, verifiable edge.

## Conclusion

Tom Brohamer's *Modern Pace Handicapping* represents a watershed moment in racing analysis. By introducing velocity-based measurement, the Track Decision Model, and energy distribution analysis, Brohamer gave handicappers tools to move beyond intuition into systematic, repeatable evaluation.

For the modern practitioner—whether using sophisticated software or manual calculation—the Brohamer methodology provides:

*   A universal language for comparing performances across tracks and conditions
*   Contextual frameworks (Decision Models) that transform raw numbers into actionable insights
*   Energy analysis that reveals how horses win, not just whether they win
*   Turn time focus that identifies the critical determinant of form and fitness

The methodology is not without challenges—first fraction inaccuracy, paceline selection complexity, and the learning curve of manual calculation—but its principles remain as valid today as when Brohamer first published them.

For those building automated systems (like EponaStables), the Brohamer framework offers a theoretically sound foundation for feature engineering. The core ratings (EP, SP, AP, FX), energy distribution (%E), and contextual modeling (Track Decision Models) can be implemented directly in predictive algorithms, providing mathematically rigorous inputs that reflect genuine racing dynamics.
